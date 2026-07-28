
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
