<div align="center">
<picture>
    <source srcset="https://imgur.com/5bYAzsb.png" media="(prefers-color-scheme: dark)">
    <source srcset="https://imgur.com/Os03JoE.png" media="(prefers-color-scheme: light)">
    <img src="https://imgur.com/Os03JoE.png" alt="Escudo UNAL" width="350px">
</picture>

<h3>Curso de Robótica 2026-I</h3>

<h1>PhantomX Pincher X100 con ROS 2 Jazzy</h1>

<h2>Proyecto Final</h2>

<h4>Jesus Alberto Rivera Molina - jriveramo@unal.edu.co<br>
    Isaac Montes Luna - imontesl@unal.edu.co</h4>

<p>
  <img alt="Ubuntu 24.04 LTS" src="https://img.shields.io/badge/Ubuntu-24.04%20LTS-E95420?logo=ubuntu&logoColor=white">
  <img alt="ROS 2 Jazzy" src="https://img.shields.io/badge/ROS%202-Jazzy-22314E?logo=ros&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white">
  <img alt="Dynamixel" src="https://img.shields.io/badge/Dynamixel-AX--12A%20%7C%20XL430-00979D">
</p>

</div>

# Sistema de Clasificacion Pick & Place - PhantomX Pincher

Este repositorio contiene los nodos y herramientas desarrolladas en ROS 2 para operar un brazo robotico PhantomX Pincher. El sistema integra vision artificial, cinematica inversa 3D y simulacion para identificar, recoger y clasificar objetos geometricos en sus respectivas canastas segun su color.

---

## Modulos Principales (Core)

### `sorting_node.py` (Nodo de Clasificacion)
Este es el nodo central del sistema, encargado de la ejecucion de los movimientos fisicos y la toma de decisiones del brazo robotico.
* **Maquina de Estados:** Implementa la logica automatizada de la tarea "Pick & Place", controlando las transiciones entre poses predefinidas como inicio (home), escaneo (scan), acercamiento (pre_pick/pre_drop), agarre (pick) y liberacion (drop).
* **Cinematica Inversa 3D:** Calcula matematicamente los angulos exactos de las articulaciones (cintura, hombro, codo, muneca) de forma analitica y continua para alcanzar las coordenadas (X, Y, Z) requeridas.
* **Integracion con Vision:** Se suscribe a los topicos de vision (`vision/coordenada_pieza` y `vision/color_pieza`) para saber a que posicion moverse y en que caneca (verde, azul, rojo o amarillo) depositar el objeto.
* **Rutina de Seguridad:** Cuenta con una funcion de recuperacion (`_execute_recovery_routine`) que abre la pinza y eleva el brazo a una zona segura en caso de que ocurra un error de calculo cinematico o de agarre.

---

## Entorno de Pruebas y Simulacion (Testing Tools)

### `test_routine_node.py` (Rutina de Diagnostico)
Script de validacion disenado para comprobar el correcto funcionamiento del hardware y la cinematica en toda el area de trabajo.
* **Secuencia de Calibracion:** Ejecuta automaticamente una prueba de 6 pasos en un orden estricto, visitando cada una de las 4 canecas: Amarilla, Azul, Verde y Roja.
* **Validacion de Trayectorias:** En cada paso, el brazo simula recoger un objeto del centroide de la plataforma blanca y lo traslada a la canasta de destino, comprobando que la cinematica inversa logre alcanzar fisicamente todos los puntos requeridos.

### `spawn_object.py` (Generador de Objetos 3D)
Comando de terminal interactivo utilizado para poblar el entorno de simulacion visual.
* **Insercion de Mallas STL:** Permite publicar figuras 3D como cubos o cilindros dentro del entorno virtual.
* **Posicionamiento Estricto:** Por defecto, coloca las figuras apoyadas sobre la plataforma blanca del robot, en el origen exacto (X=9.6cm, Z=2.75cm).
* **Configuracion Dinamica:** Acepta argumentos de linea de comandos para modificar rapidamente la forma (`--shape`), el color (`--color`), la escala (`--scale`), la posicion (X, Y, Z) y la rotacion (roll, pitch, yaw) del objeto simulado.

### `test_block_publisher.py` (Simulador de Deteccion Visual)
Herramienta disenada para probar la logica de clasificacion del sistema sin necesidad de tener la camara fisica conectada.
* **Mocking de Datos:** Publica coordenadas de prueba y colores directamente en los topicos de ROS 2 (`vision/coordenada_pieza` y `vision/color_pieza`), simulando que la camara encontro una pieza para que el robot inicie su rutina.
* **Feedback Visual:** Al enviar la deteccion simulada, despliega simultaneamente un marcador visual 3D (utilizando mallas STL de cubos, cilindros, triangulos o pentagonos) en la interfaz de RViz en la coordenada indicada, facilitando ver que objeto intentara agarrar el brazo.

### `go_to_tray_origin_node.py` (Nodo de Posicionamiento y Marcador)

Este script define el nodo `GoToTrayOriginNode`, el cual es un nodo de prueba diseñado para mover el brazo robótico exactamente al centro de la plataforma blanca y mantener una referencia visual activa en el simulador RViz.

* **Posicionamiento Exacto:** El nodo envía ángulos articulares predefinidos (cintura: 0.0 grados, hombro: +13.0 grados, codo: +129.0 grados, muñeca: +32.0 grados, pinza: 0.0 grados) mediante el tópico `/pincher/command`[cite: 7]. Esta configuración cinemática específica permite que el efector final alcance físicamente el origen de la bandeja.
* **Marcador Visual (Esfera Roja):** Configura un marcador tridimensional de tipo esfera (`Marker.SPHERE`) de color rojo brillante y 4 cm de diámetro. Este marcador se posiciona a 4 cm sobre el centro de la plataforma (X=0.096m, Y=0.0m, Z=0.04m) en el marco espacial "world", sirviendo como un objetivo visual nítido en RViz.
* **Bucle de Ejecución Continua (2 Hz):** Implementa un temporizador (`timer_callback`) que se dispara cada 0.5 segundos[cite: 7]. En cada iteración, el nodo actualiza la marca de tiempo y vuelve a publicar la posición de la esfera roja, los ángulos de las articulaciones y un mensaje de estado en `/pincher/status` indicando el movimiento hacia la `zonaRecoleccion_link`. Esto garantiza que tanto el simulador como el hardware mantengan la posición activa de forma constante.

# Nodo de Visión de Máquina con YOLOv8 para ROS 2 (PhantomX Pincher)

Este módulo es parte del paquete de control de un brazo robótico PhantomX Pincher en ROS 2 (Jazzy). Implementa un nodo de visión artificial que utiliza un modelo entrenado de YOLO (Ultralytics) para detectar piezas geométricas, calcular su centro en píxeles y realizar una transformación espacial para publicar sus coordenadas (X, Y) en centímetros relativas a la base del robot.


# Creación de un Dataset para Entrenamiento con Roboflow

## 1. Creación del proyecto y carga de datos

El primer paso consiste en crear un nuevo proyecto en **Roboflow** seleccionando el tipo **Object Detection**. En esta etapa se definen las clases u objetos que el modelo deberá reconocer, por ejemplo:

- Cubo
- Cilindro
- Rectangulo
- Pentagono

Posteriormente, se cargan las imágenes o videos capturados con la cámara del robot. Si se utiliza un video, Roboflow extrae automáticamente fotogramas a intervalos regulares para convertirlos en imágenes aptas para el entrenamiento.

---

## 2. Etiquetado de objetos (*Bounding Boxes*)

Una vez cargadas las imágenes, se procede al etiquetado manual mediante el editor de Roboflow.

Para cada objeto visible se dibuja una **caja delimitadora (Bounding Box)** que se ajusta lo mejor posible a sus contornos y se asigna la clase correspondiente.

Roboflow incorpora herramientas como **Label Assist**, que, después de etiquetar algunas imágenes, es capaz de predecir automáticamente la ubicación de los objetos en las imágenes restantes, reduciendo significativamente el tiempo de etiquetado.

---

## 3. Preprocesamiento y aumento de datos (*Data Augmentation*)

Esta etapa mejora la capacidad del modelo para generalizar y reconocer objetos en diferentes condiciones.

### Preprocesamiento

Se realizan automáticamente tareas como:

- Redimensionar todas las imágenes a un tamaño uniforme (generalmente **520 × 520 píxeles** para YOLO).
- Corregir la orientación de las imágenes cuando sea necesario.

### Aumento de datos

Roboflow genera nuevas versiones de las imágenes originales aplicando distintas transformaciones, entre ellas:

- Ajustes de brillo.
- Rotaciones.
- Adición de ruido.

Estas modificaciones permiten simular diferentes condiciones de iluminación, orientación de los objetos y calidad de la cámara, aumentando la robustez del modelo. Por ejemplo, un conjunto de **100 imágenes originales** puede ampliarse hasta aproximadamente **100 imágenes** para entrenamiento.

---

## 4. Generación y división del conjunto de datos

Una vez procesadas las imágenes, Roboflow organiza automáticamente el dataset y lo divide en tres subconjuntos:

| Conjunto | Porcentaje | Función |
|----------|-----------:|---------|
| **Train** | ~80 % | Utilizado para entrenar el modelo. |
| **Valid** | ~10 % | Empleado para evaluar el rendimiento durante el entrenamiento y ajustar parámetros. |
| **Test** | ~10 % | Reservado para medir el desempeño final del modelo con imágenes nunca vistas. |

Esta separación evita el sobreajuste y permite obtener una evaluación objetiva del detector.

---

## 5. Exportación en formato YOLOv8

Finalmente, se genera una versión del dataset y se selecciona la opción **Export**.

Roboflow organiza automáticamente todos los archivos con la estructura requerida por **Ultralytics YOLOv8**, entregando un archivo comprimido (`.zip`) que contiene:

```text
dataset/
├── images/
│   ├── train/
│   ├── valid/
│   └── test/
├── labels/
│   ├── train/
│   ├── valid/
│   └── test/
└── data.yaml
```

Donde:

- **images/** contiene las imágenes del conjunto de datos.
- **labels/** almacena los archivos `.txt` con las coordenadas de las cajas delimitadoras y las clases correspondientes.
- **data.yaml** especifica la ubicación del dataset y las clases que utilizará YOLOv8 durante el entrenamiento.

# Entrenamiento del modelo YOLOv8

## 1. Contenido del archivo exportado y configuración de `data.yaml`

Al descomprimir el archivo `.zip` exportado desde **Roboflow**, se obtiene la estructura completa del conjunto de datos, organizada en carpetas para entrenamiento, validación y prueba, además del archivo de configuración `data.yaml`.

```text
dataset/
├── images/
│   ├── train/
│   ├── valid/
│   └── test/
├── labels/
│   ├── train/
│   ├── valid/
│   └── test/
└── data.yaml
```

El archivo `data.yaml` es el encargado de proporcionar a YOLOv8 la información necesaria para localizar y utilizar correctamente el conjunto de datos. En él se especifica:

- La ubicación de las imágenes de entrenamiento, validación y prueba.
- El número total de clases que deberá aprender el modelo.
- El nombre de cada una de las clases definidas en el dataset.

Un ejemplo de este archivo es el siguiente:

```yaml
train: ../train/images
val: ../valid/images
test: ../test/images

nc: 3

names:
  0: cubo
  1: cilindro
  2: esfera
```

---

## 2. Entorno de entrenamiento: Google Colab

El entrenamiento de una red neuronal implica ejecutar millones de operaciones matemáticas para ajustar los parámetros del modelo. Aunque este proceso puede realizarse utilizando únicamente el procesador (**CPU**) de un computador, el tiempo de ejecución suele ser muy elevado.

Por esta razón, se emplea **Google Colab**, una plataforma en la nube que proporciona acceso gratuito a unidades de procesamiento gráfico (**GPU**). Estas están diseñadas para realizar cálculos paralelos de manera eficiente, reduciendo significativamente el tiempo de entrenamiento, que puede pasar de varias horas o incluso días a unos pocos minutos u horas, dependiendo del tamaño del conjunto de datos.

---

## 3. Configuración del entrenamiento

Una vez preparado el entorno de trabajo y cargado el conjunto de datos en Google Colab, el entrenamiento del modelo se inicia mediante el siguiente comando:

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=100 imgsz=520
```

Cada uno de los parámetros cumple una función específica:

| Parámetro | Descripción |
|-----------|-------------|
| `task=detect` | Indica que la tarea corresponde a detección de objetos. |
| `mode=train` | Especifica que el modelo se entrenará. |
| `model=yolov8n.pt` | Utiliza el modelo preentrenado **YOLOv8 Nano**, una versión ligera y rápida basada en aprendizaje por transferencia (*Transfer Learning*). |
| `data=data.yaml` | Carga la configuración del conjunto de datos definida en el archivo `data.yaml`. |
| `epochs=100` | Define que el modelo recorrerá el conjunto de entrenamiento 100 veces para optimizar sus parámetros. |
| `imgsz=520` | Establece una resolución de entrada de **640 × 640 píxeles** para todas las imágenes. |

El uso de un modelo preentrenado permite que la red neuronal aproveche conocimientos previamente adquiridos sobre características visuales generales, como bordes, texturas y formas, acelerando el proceso de aprendizaje y mejorando el rendimiento con un número reducido de imágenes.

---

## 4. Proceso de entrenamiento

El entrenamiento se desarrolla de forma iterativa a lo largo de las épocas (*epochs*).

Durante la primera época, el modelo realiza predicciones con un alto nivel de error, ya que aún no ha aprendido a identificar correctamente los objetos presentes en las imágenes. Estas predicciones se comparan con las etiquetas reales generadas en Roboflow y, a partir de esa diferencia, se calcula una función de pérdida (*Loss*), la cual cuantifica el error cometido.

Posteriormente, mediante algoritmos de optimización, la red neuronal ajusta sus parámetros internos para reducir dicho error. Este procedimiento se repite en cada época hasta que el modelo alcanza un desempeño cada vez más preciso.

En términos generales:

- El valor de **Loss** disminuye progresivamente.
- La precisión del modelo aumenta conforme avanza el entrenamiento.
- Las predicciones se aproximan cada vez más a las etiquetas reales del conjunto de datos.

---

## 5. Generación del modelo `best.pt`

Durante todo el entrenamiento, YOLOv8 guarda periódicamente diferentes versiones del modelo.

Al finalizar las épocas establecidas, el sistema evalúa cuál de esas versiones obtuvo el mejor desempeño utilizando el conjunto de **validación**, es decir, imágenes que no fueron empleadas directamente para el aprendizaje, sino únicamente para medir la capacidad de generalización del modelo.

La versión con mejores resultados se almacena en el archivo:

```text
best.pt
```

Este archivo contiene los **pesos entrenados** de la red neuronal y representa el modelo final que posteriormente será utilizado para realizar inferencias.

En aplicaciones robóticas, como la integración con **ROS 2**, el archivo `best.pt` se carga en el nodo encargado de la detección de objetos, permitiendo que el robot identifique y localice los elementos del entorno en tiempo real mediante la cámara.


##  Características Principales Del modelo 

- **Inferencia en Tiempo Real:** Detección de objetos usando un modelo personalizado (`best.pt`) de YOLO.
- **Transformación Espacial 2D:** Convierte el centro del bounding box (píxeles) a coordenadas del mundo real (centímetros).
- **Cumplimiento del Estándar REP 103:** El sistema de coordenadas está referenciado al `base_link` del robot:
  - **+X:** Hacia derecha del robot.
  - **+Y:** Hacia adelante del robot.
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
