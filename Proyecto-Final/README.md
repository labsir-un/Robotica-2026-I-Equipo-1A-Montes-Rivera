# Sistema de Clasificacion Pick & Place - PhantomX Pincher

Este repositorio contiene los nodos y herramientas desarrolladas en ROS 2 para operar un brazo robotico PhantomX Pincher. El sistema integra vision artificial, cinematica inversa 3D y simulacion para identificar, recoger y clasificar objetos geometricos en sus respectivas canastas segun su color.

---

## Modulos Principales (Core)

### `sorting_node.py` (Nodo de Clasificacion)
Este es el nodo central del sistema, encargado de la ejecucion de los movimientos fisicos y la toma de decisiones del brazo robotico[cite: 2].
* **Maquina de Estados:** Implementa la logica automatizada de la tarea "Pick & Place", controlando las transiciones entre poses predefinidas como inicio (home), escaneo (scan), acercamiento (pre_pick/pre_drop), agarre (pick) y liberacion (drop)[cite: 2].
* **Cinematica Inversa 3D:** Calcula matematicamente los angulos exactos de las articulaciones (cintura, hombro, codo, muneca) de forma analitica y continua para alcanzar las coordenadas (X, Y, Z) requeridas[cite: 2].
* **Integracion con Vision:** Se suscribe a los topicos de vision (`vision/coordenada_pieza` y `vision/color_pieza`) para saber a que posicion moverse y en que caneca (verde, azul, rojo o amarillo) depositar el objeto[cite: 2].
* **Rutina de Seguridad:** Cuenta con una funcion de recuperacion (`_execute_recovery_routine`) que abre la pinza y eleva el brazo a una zona segura en caso de que ocurra un error de calculo cinematico o de agarre[cite: 2].

---

## Entorno de Pruebas y Simulacion (Testing Tools)

### `test_routine_node.py` (Rutina de Diagnostico)
Script de validacion disenado para comprobar el correcto funcionamiento del hardware y la cinematica en toda el area de trabajo[cite: 5].
* **Secuencia de Calibracion:** Ejecuta automaticamente una prueba de 6 pasos en un orden estricto, visitando cada una de las 4 canecas: Amarilla, Azul, Verde y Roja[cite: 5].
* **Validacion de Trayectorias:** En cada paso, el brazo simula recoger un objeto del centroide de la plataforma blanca y lo traslada a la canasta de destino, comprobando que la cinematica inversa logre alcanzar fisicamente todos los puntos requeridos[cite: 5].

### `spawn_object.py` (Generador de Objetos 3D)
Comando de terminal interactivo utilizado para poblar el entorno de simulacion visual[cite: 3].
* **Insercion de Mallas STL:** Permite publicar figuras 3D como cubos o cilindros dentro del entorno virtual[cite: 3].
* **Posicionamiento Estricto:** Por defecto, coloca las figuras apoyadas sobre la plataforma blanca del robot, en el origen exacto (X=9.6cm, Z=2.75cm)[cite: 3].
* **Configuracion Dinamica:** Acepta argumentos de linea de comandos para modificar rapidamente la forma (`--shape`), el color (`--color`), la escala (`--scale`), la posicion (X, Y, Z) y la rotacion (roll, pitch, yaw) del objeto simulado[cite: 3].

### `test_block_publisher.py` (Simulador de Deteccion Visual)
Herramienta disenada para probar la logica de clasificacion del sistema sin necesidad de tener la camara fisica conectada[cite: 4].
* **Mocking de Datos:** Publica coordenadas de prueba y colores directamente en los topicos de ROS 2 (`vision/coordenada_pieza` y `vision/color_pieza`), simulando que la camara encontro una pieza para que el robot inicie su rutina[cite: 4].
* **Feedback Visual:** Al enviar la deteccion simulada, despliega simultaneamente un marcador visual 3D (utilizando mallas STL de cubos, cilindros, triangulos o pentagonos) en la interfaz de RViz en la coordenada indicada, facilitando ver que objeto intentara agarrar el brazo[cite: 4].

# Nodo de Visión de Máquina con YOLOv8 para ROS 2 (PhantomX Pincher)

Este módulo es parte del paquete de control de un brazo robótico PhantomX Pincher en ROS 2 (Jazzy). Implementa un nodo de visión artificial que utiliza un modelo entrenado de YOLO (Ultralytics) para detectar piezas geométricas, calcular su centro en píxeles y realizar una transformación espacial para publicar sus coordenadas (X, Y) en centímetros relativas a la base del robot.

##  Características Principales

- **Inferencia en Tiempo Real:** Detección de objetos usando un modelo personalizado (`best.pt`) de YOLO.
- **Transformación Espacial 2D:** Convierte el centro del bounding box (píxeles) a coordenadas del mundo real (centímetros).
- **Cumplimiento del Estándar REP 103:** El sistema de coordenadas está referenciado al `base_link` del robot:
  - **+X:** Hacia adelante del robot.
  - **+Y:** Hacia la izquierda del robot.
- **Publicación de Tópicos ROS 2:**
  - `/vision/coordenada_pieza` (`geometry_msgs/Point`): Coordenadas para la cinemática inversa.
  - `/vision/imagen_procesada` (`sensor_msgs/Image`): Video en vivo con las detecciones dibujadas.

##  Requisitos e Instalación

Para evitar conflictos con las dependencias del sistema en Ubuntu (PEP 668), se recomienda usar un entorno virtual para las dependencias de IA.

### 1. Configuración del Entorno Virtual y YOLO

```bash
# Crear entorno virtual que permita ver los paquetes de ROS 2
python3 -m venv --system-site-packages venv_vision
source venv_vision/bin/activate

# Instalar Ultralytics e ignorar la versión 2.x de NumPy (evita crash de matplotlib)
pip install ultralytics
pip install "numpy<2"
```

### 2. Integración al Workspace de ROS 2

El script principal (`vision_node.py`) debe ubicarse dentro de tu paquete de ROS 2 (ej. `pincher_control`).

Asegúrate de registrar el nodo en el archivo `setup.py` del paquete:

```python
entry_points={
    'console_scripts': [
        'vision_node = pincher_control.vision_node:main'
    ],
},
```

Luego, compila el paquete de forma limpia:

```bash
cd ~/ros2_ws
rm -rf build/ install/ log/   # Limpieza recomendada si hay errores con setuptools
colcon build --packages-select pincher_control
```

##  Calibración Espacial (Píxeles a Centímetros)

El código asume una cámara fija. Para que la cinemática inversa funcione correctamente, debes configurar los parámetros de calibración dentro de `vision_node.py` en base a tu entorno físico:

```python
# Píxeles en la imagen que corresponden al centro físico de la base del robot (0,0)
self.BASE_PIXEL_X = 320.0  
self.BASE_PIXEL_Y = 440.0  

# Factor de conversión (ej. medir cuántos píxeles se mueve el objeto al desplazarlo 10cm)
self.CM_POR_PIXEL_X = 0.05  
self.CM_POR_PIXEL_Y = 0.05
```

##  Ejecución

Para iniciar el nodo, debes activar tanto el entorno de ROS 2 como el entorno virtual de Python:

```bash
# 1. Cargar ROS 2 y el workspace
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash

# 2. Cargar el entorno virtual de visión
source ~/vision_robot/venv_vision/bin/activate

# 3. Ejecutar el nodo
ros2 run pincher_control vision_node
```
