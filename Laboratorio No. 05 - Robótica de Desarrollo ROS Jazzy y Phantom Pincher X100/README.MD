<div align="center">
<picture>
    <source srcset="https://imgur.com/5bYAzsb.png" media="(prefers-color-scheme: dark)">
    <source srcset="https://imgur.com/Os03JoE.png" media="(prefers-color-scheme: light)">
    <img src="https://imgur.com/Os03JoE.png" alt="Escudo UNAL" width="350px">
</picture>

<h3>Curso de Robótica 2026-I</h3>

<h1>PhantomX Pincher X100 con ROS 2 Jazzy</h1>

<h2>Laboratorio No. 05 - Cinemática - Pincher Phantom X100</h2>

<h4>Jesus Alberto Rivera Molina - jriveramo@unal.edu.co<br>
    Isaac Montes Luna - imontesl@unal.edu.co</h4>

<p>
  <img alt="Ubuntu 24.04 LTS" src="https://img.shields.io/badge/Ubuntu-24.04%20LTS-E95420?logo=ubuntu&logoColor=white">
  <img alt="ROS 2 Jazzy" src="https://img.shields.io/badge/ROS%202-Jazzy-22314E?logo=ros&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white">
  <img alt="Dynamixel" src="https://img.shields.io/badge/Dynamixel-AX--12A%20%7C%20XL430-00979D">
</p>

</div>

---

## 1. Objetivos del Laboratorio
- Controlar las articulaciones del robot Phantom X Pincher X100 utilizando ROS 2 Jazzy.
- Medir y modelar la geometría del manipulador.
- Implementar movimientos individuales, simultáneos, secuenciales e interpolados.
- Aplicar cinemática directa e inversa.
- Programar trayectorias, repetición de poses y tareas artísticas con el robot.

---

## 2. Requisitos y Dependencias
- **Sistema Operativo**: Ubuntu 24.04 LTS.
- **Middleware**: ROS 2 Jazzy Jalisco.
- **Lenguaje**: Python 3.
- **Herramienta de Construcción**: `colcon`.
- **Hardware**: Robot Phantom X Pincher X100, fuente de alimentación y sistema de comunicación (servomotores DYNAMIXEL).
- **Herramientas Adicionales**: Calibrador (para mediciones físicas) y soporte para marcador liviano.

> [!IMPORTANT]
> El laboratorio debe desarrollarse únicamente con ROS 2 Jazzy. No se aceptarán soluciones basadas en ROS Humble.

---

## 3. Repositorios Base Utilizados
- **Visualización y control del robot en ROS 2 Jazzy**:
  [06_Rob_2026_I_ROS2_Jazzy_PhantomX100_RVIZ](https://github.com/labsir-un/06_Rob_2026_I_ROS2_Jazzy_PhantomX100_RVIZ.git)
- **Kit Phantom X Pincher para ROS 2**:
  [KIT_Phantom_X_Pincher_ROS2](https://github.com/labsir-un/KIT_Phantom_X_Pincher_ROS2.git)
- **Archivos tridimensionales del robot**:
  [3DModels_KIT_Phantom_Pincher_X100](https://github.com/labsir-un/3DModels_KIT_Phantom_Pincher_X100.git)

---

## 4. Condiciones de Operación Segura
1. El robot debe iniciar y finalizar cada prueba en una posición segura.
2. Todos los valores de consigna enviados deben respetar los límites articulares.
3. Los movimientos de gran amplitud deben realizarse mediante trayectorias interpoladas para evitar desgastes y golpes.
4. No se debe sujetar ni bloquear manualmente el robot mientras los servomotores estén energizados.
5. Cada movimiento debe verificarse en el entorno de simulación (RViz) antes de ejecutarse sobre el robot real.

---

## 5. Estructura del Repositorio y Entregables
De acuerdo con las pautas de entrega, este repositorio cuenta con la siguiente estructura de archivos detallada:

```text
Laboratorio No. 05 - Robótica de Desarrollo ROS Jazzy y Phantom Pincher X100/
├── README.md                                # Este archivo con la documentación del laboratorio
├── doc/                                     # Documentación gráfica y planos del laboratorio
│   ├── diagrama_de_flujo.png                # Diagrama de flujo de las acciones del robot (pendiente)
│   ├── plano_de_planta.png                  # Plano de planta del entorno de trabajo (pendiente)
│   └── diagrama_geometrico.png              # Diagrama geométrico y sistemas coordenados (pendiente)
├── results/                                 # Gráficas obtenidas durante las pruebas
│   ├── calibracion/                         # Gráficas de error y calibración de cero (pendientes)
│   ├── interpolacion/                       # Gráficas de trayectorias interpoladas (lineal/cúbica) (pendientes)
│   └── sinusoidal/                          # Gráficas de trayectorias sinusoidales (pendientes)
├── videos/                                  # Enlaces o archivos de video demostrativos (pendientes)
└── src/                                     # Código fuente de los paquetes de ROS 2
    ├── pincher_description/                 # Descripción URDF y mallas del manipulador
    │   ├── launch/
    │   │   ├── display.launch.py            # Lanzador para visualizar en RViz2 (con mallas/cajas)
    │   │   └── display_gui.launch.py        # Lanzador interactivo con joint_state_publisher_gui
    │   ├── meshes/                          # Archivos STL con la geometría 3D del robot
    │   │   └── *.stl
    │   ├── rviz/
    │   │   └── pincher.rviz                 # Configuración de visualización en RViz2
    │   ├── urdf/
    │   │   └── robot.xacro                  # Modelo cinemático en Xacro (Home vertical)
    │   ├── package.xml
    │   └── setup.py
    └── pincher_control/                     # Paquete de control e interacción con motores
        ├── config/
        │   ├── ax12a.yaml                   # Configuración del perfil de servomotor AX-12A
        │   └── xl430.yaml                   # Configuración del perfil de servomotor XL430-W250
        ├── launch/
        │   └── pincher_system.launch.py     # Lanzador principal (gui + control_servo + rviz)
        ├── pincher_control/                 # Nodos y scripts principales en Python
        │   ├── __init__.py
        │   ├── control_servo.py             # Nodo ROS 2 que interactúa con DynamixelSDK
        │   ├── dynamixel_profiles.py        # Perfiles de registros Dynamixel
        │   ├── joint_mover.py               # Nodo por consola para control articular individual y secuencial
        │   ├── pincher_gui.py               # Interfaz gráfica (Tkinter) para sliders y torque
        │   └── scan_dynamixel.py            # Utilidad de escaneo de IDs en el bus
        ├── package.xml
        └── setup.py
```

> [!WARNING]
> Recuerde que al estructurar o compilar el espacio de trabajo localmente, las carpetas autogeneradas `build`, `install` o `log` **no** deben ser subidas al repositorio de entrega.

---

## 6. Desarrollo de las Actividades

### Actividad 1. Preparación del Robot
*Detalles sobre la conexión, posicionamiento inicial del manipulador, energización y sincronización entre el modelo virtual en RViz y el robot físico.*
- **Estado**: Completado
- **Descripción**: Se configuró y compiló el espacio de trabajo `phantom_ws` bajo ROS 2 Jazzy. Se diseñó el modelo URDF en `robot.xacro` definiendo eslabones y articulaciones del PhantomX Pincher X100, configurando su pose inicial (Home) de manera que se visualice completamente vertical en RViz. Para la visualización e interacción virtual, se crearon los lanzamientos `display.launch.py` (visualización base con mallas STL o cajas) y `display_gui.launch.py` (interfaz interactiva para publicar estados articulares). El sistema físico se conecta mediante interfaz USB-Serial con servomotores DYNAMIXEL (XL430 o AX-12A), sincronizándose en tiempo real mediante el nodo `control_servo` que publica los estados en `/joint_states`.

### Actividad 2. Identificación de Motores y Articulaciones
Tabla resumen con los servomotores DYNAMIXEL que conforman el robot:

| Articulación | ID DYNAMIXEL | Referencia (0 rad / 0°) | Sentido Positivo | Función |
| :--- | :---: | :--- | :--- | :--- |
| **Base** | 1 | Vertical (Eje Z positivo) | Antihorario (vista superior) | Rotación de la estructura sobre el plano XY |
| **Hombro** | 2 | Vertical (Eje Z positivo) | Hacia adelante (flexión) | Elevación y descenso del brazo |
| **Codo** | 3 | Vertical (colineal al Hombro) | Hacia adelante (flexión) | Extensión y flexión del antebrazo |
| **Muñeca** | 4 | Vertical (colineal al Codo) | Hacia abajo (flexión) | Ajuste de orientación/cabeceo del TCP |
| **Pinza** | 5 | Totalmente abierta | Apertura de los dedos | Agarre y sujeción de objetos |

### Actividad 3. Medición del Robot
Dimensiones físicas y geométricas del manipulador obtenidas a partir de los archivos URDF/STL y especificaciones técnicas:
- *Altura de la base (Suelo a Eje del Hombro)*: 89.45 mm
- *Distancia entre ejes consecutivos*:
  - Eje 1 (Base) a Eje 2 (Hombro): 89.45 mm
  - Eje 2 (Hombro) a Eje 3 (Codo): 105.8 mm (distancia euclidiana considerando offset Lm = 31.5 mm y altura L2 = 101.0 mm)
  - Eje 3 (Codo) a Eje 4 (Muñeca): 105.8 mm (L3)
- *Longitud de eslabones principales*:
  - Eslabón 1 (Hombro/Upper arm): 101.0 mm (L2) con offset lateral de 31.5 mm (Lm)
  - Eslabón 2 (Codo/Forearm): 101.0 mm (L3)
- *Distancia desde la última articulación (Muñeca) hasta el TCP*: 119.0 mm (L4)
- *Dimensiones principales de la pinza*: Barra de soporte de 75.0 mm de ancho; dedos/fingers de 70.0 mm de longitud.
> [!NOTE]
> El diagrama geométrico conceptual con dimensiones, ejes de movimiento y sistemas coordenados se encuentra en [doc/diagrama_geometrico.png](doc/diagrama_geometrico.png) (pendiente de generación gráfica).

### Actividad 4. Movimiento Individual de Articulaciones
*Desarrollo del nodo que permite controlar cada articulación de forma independiente.*
- **Nodo**: `joint_mover` (paquete `pincher_control`)
- **Comando de ejecución**:
  ```bash
  ros2 run pincher_control joint_mover
  ```
- **Descripción**: El programa inicia configurando automáticamente la velocidad máxima al 30% (valor `307` de `1023`) para asegurar movimientos suaves. Implementa una interfaz de consola interactiva multihilo que no bloquea la recepción de `/joint_states`. Permite realizar:
  1. **Control manual individual (opción 1)**: Selección de una junta, visualización de su ángulo actual en grados y envío de la consigna deseada (validando los límites seguros).
  2. **Rutina de movimientos independientes automática (opción 2)**: Mueve cada articulación por 3 posiciones de prueba distintas (ej. Base a 45°, -45° y 90°) esperando 10 segundos en cada una, y retornando a 0.0° antes de pasar a la siguiente junta.
  3. **Rutina de movimientos simultáneos (opción 3 - Actividad 7)**: Mueve las 5 articulaciones al mismo tiempo hacia las 5 configuraciones de prueba secuencialmente, esperando 5 segundos por pose.
  4. **Rutina de movimientos secuenciales (opción 4 - Actividad 8)**: Mueve las articulaciones paso a paso en el orden establecido hacia la 4ª configuración, esperando 4 segundos por junta, y retornando en orden inverso por seguridad.
- **Enlace al Video**: [Video Movimiento Individual](https://youtube.com/placeholder_video_individual) (pendiente de grabación)

### Actividad 5. Calibración de Cero y Error Articular
*Análisis del error de posicionamiento articular medido en 5 puntos distintos del rango seguro.*

- **Fórmula del error**:
  $$e_q = q_{\text{deseado}} - q_{\text{medido}}$$

- **Estado**: Completado

#### 1. Datos Medidos en el Laboratorio (Valores en Grados °)
| Deseado ($q_{\text{deseado}}$) | Base ($q_{\text{medido}}$) | Hombro ($q_{\text{medido}}$) | Codo ($q_{\text{medido}}$) | Muñeca ($q_{\text{medido}}$) | Pinza ($q_{\text{medido}}$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **10.0°** | 9.68° | 10.56° | 10.26° | 9.68° | 10.26° |
| **20.0°** | 19.65° | 20.82° | 20.53° | 19.94° | 20.23° |
| **30.0°** | 29.62° | 31.09° | 30.50° | 30.21° | 30.21° |
| **40.0°** | 39.88° | 41.64° | 40.47° | 39.88° | 40.47° |
| **50.0°** | 49.85° | 51.32° | 50.73° | 50.15° | 49.56° |

#### 2. Tabla de Errores Calculados ($e_q$) en Grados y Radianes
| Articulación | $10^\circ$ | $20^\circ$ | $30^\circ$ | $40^\circ$ | $50^\circ$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Base** | +0.32° (+0.00559 rad) | +0.35° (+0.00611 rad) | +0.38° (+0.00663 rad) | +0.12° (+0.00209 rad) | +0.15° (+0.00262 rad) |
| **Hombro** | -0.56° (-0.00977 rad) | -0.82° (-0.01431 rad) | -1.09° (-0.01902 rad) | -1.64° (-0.02862 rad) | -1.32° (-0.02304 rad) |
| **Codo** | -0.26° (-0.00454 rad) | -0.53° (-0.00925 rad) | -0.50° (-0.00873 rad) | -0.47° (-0.00820 rad) | -0.73° (-0.01274 rad) |
| **Muñeca** | +0.32° (+0.00559 rad) | +0.06° (+0.00105 rad) | -0.21° (-0.00367 rad) | +0.12° (+0.00209 rad) | -0.15° (-0.00262 rad) |
| **Pinza** | -0.26° (-0.00454 rad) | -0.23° (-0.00401 rad) | -0.21° (-0.00367 rad) | -0.47° (-0.00820 rad) | +0.44° (+0.00768 rad) |

#### 3. Métricas Resumen del Error
- **Base**:
  - Error Máximo: 0.38° (0.00663 rad)
  - Error Promedio: 0.26° (0.00461 rad)
  - Offset Cero Estimado: 0.26° (0.00461 rad)
- **Hombro**:
  - Error Máximo: 1.64° (0.02862 rad)
  - Error Promedio: -1.09° (-0.01895 rad)
  - Offset Cero Estimado: -1.09° (-0.01895 rad)
- **Codo**:
  - Error Máximo: 0.73° (0.01274 rad)
  - Error Promedio: -0.50° (-0.00869 rad)
  - Offset Cero Estimado: -0.50° (-0.00869 rad)
- **Muñeca**:
  - Error Máximo: 0.32° (0.00559 rad)
  - Error Promedio: 0.03° (0.00049 rad)
  - Offset Cero Estimado: 0.03° (0.00049 rad)
- **Pinza**:
  - Error Máximo: 0.47° (0.00820 rad)
  - Error Promedio: -0.15° (-0.00255 rad)
  - Offset Cero Estimado: -0.15° (-0.00255 rad)

- **Gráficas**: Las gráficas comparativas de posición deseada vs. medida se encuentran en [results/calibracion/](results/calibracion/) (pendientes de generación gráfica).

### Actividad 6. Determinación de Límites Seguros
Definición de los límites físicos y los límites de movimiento seguro por software (con un margen de seguridad de $10.0^\circ$ o $0.175\text{ rad}$) para la protección mecánica del manipulador, validados activamente en `control_servo.py`, `joint_mover.py` y `pincher_gui.py`:

| Articulación | Límite Inf. (Físico) | Límite Sup. (Físico) | Margen de Seguridad | Límite Inf. Seguro (Software) | Límite Sup. Seguro (Software) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Base** | -150.0° (-2.618 rad) | 149.0° (2.601 rad) | 10.0° (0.175 rad) | -140.0° (-2.443 rad) | 139.0° (2.426 rad) |
| **Hombro** | -116.0° (-2.025 rad) | 74.0° (1.292 rad) | 10.0° (0.175 rad) | -106.0° (-1.850 rad) | 64.0° (1.117 rad) |
| **Codo** | -141.0° (-2.461 rad) | 147.0° (2.566 rad) | 10.0° (0.175 rad) | -131.0° (-2.286 rad) | 137.0° (2.391 rad) |
| **Muñeca** | -103.0° (-1.798 rad) | 103.0° (1.798 rad) | 10.0° (0.175 rad) | -93.0° (-1.623 rad) | 93.0° (1.623 rad) |
| **Pinza** | -120.0° (-2.094 rad) | 120.0° (2.094 rad) | 10.0° (0.175 rad) | -110.0° (-1.920 rad) | 110.0° (1.920 rad) |

*El código del nodo de control interactivo por consola y la interfaz gráfica validan los comandos contra los límites seguros (Software) antes de transmitir las consignas a los motores.*

### Actividad 7. Movimiento Simultáneo
Ejecución de configuraciones angulares conjuntas de las 5 articulaciones, enviadas en un único mensaje de tipo `sensor_msgs/msg/JointState` a `/pincher/command`:

- **Comando de ejecución**:
  ```bash
  # Iniciar la secuencia automática de movimiento simultáneo (Opción 3)
  ros2 run pincher_control joint_mover
  ```

1. **Configuración 1**: `[0, 0, 0, 0, 0]` -> Posición vertical de reposo/seguridad (Home). Verificada en simulación y hardware.
2. **Configuración 2**: `[25, 25, 20, -20, 0]` -> Inclinación suave hacia el frente y derecha. Verificada.
3. **Configuración 3**: `[-35, 35, -30, 30, 0]` -> Inclinación hacia la izquierda con compensación de cabeceo. Verificada.
4. **Configuración 4**: `[85, -20, 55, 25, 0]` -> Extensión lateral pronunciada hacia la derecha. Verificada.
5. **Configuración 5**: `[80, -35, 55, -45, 0]` -> Posición extendida hacia la derecha con orientación del gripper inclinada hacia abajo. Verificada.

*Nota: La secuencia se ejecuta de forma completamente automática desde la opción 3 del menú, pausando 5 segundos entre configuraciones para estabilización y retornando automáticamente a Home al finalizar.*

### Actividad 8. Movimiento Secuencial
*Ejecución de la 4ª configuración del movimiento simultáneo realizando giros secuenciales en el orden: Base -> Hombro -> Codo -> Muñeca -> Pinza.*

- **Comando de ejecución**:
  ```bash
  # Iniciar la secuencia automática de movimiento secuencial (Opción 4)
  ros2 run pincher_control joint_mover
  ```

- **Tabla Comparativa: Simultáneo vs. Secuencial**:
  
  | Criterio | Movimiento Simultáneo (Actividad 7) | Movimiento Secuencial (Actividad 8) |
  | :--- | :--- | :--- |
  | **Tiempo de Ejecución** | **Mínimo** (~4 segundos). Todas las articulaciones se mueven al mismo tiempo. | **Máximo** (~20 segundos). Las articulaciones se mueven una por una esperando la anterior. |
  | **Trayectoria del TCP** | **Directa/Curva**. El TCP se desplaza trazando una trayectoria tridimensional suave y directa al punto final. | **Ortogonal/Segmentada**. El TCP realiza movimientos escalonados (rotación en plano horizontal, flexión de hombro, extensión de codo, etc.). |
  | **Suavidad** | **Alta**. Las aceleraciones y desaceleraciones de los motores se superponen, evitando sacudidas bruscas. | **Baja-Media**. Paradas y arranques bruscos en cada transición de junta. |
  | **Seguridad de Operación** | **Alta** (siempre que la trayectoria directa esté libre de obstáculos). | **Muy Alta** (permite vigilar colisiones paso a paso, ideal para calibración o espacios reducidos). |

*Nota: La secuencia de retorno a 0.0° se realiza en orden inverso (Pinza -> Muñeca -> Codo -> Hombro -> Base) con esperas de 4 segundos por articulación, garantizando la seguridad mecánica del manipulador al replegarse.*

- **Enlace al Video**: [Video Simultáneo vs Secuencial](https://youtube.com/placeholder_video_sim_sec) (pendiente de grabación)

### Actividad 9. Interpolación de Trayectorias
*Nodo para mover el robot entre dos configuraciones lejanas usando perfiles interpolados:*

- **Estado**: Completado
- **Nodo**: `trajectory_interpolator` (paquete `pincher_control`)
- **Comando de ejecución**:
  ```bash
  ros2 run pincher_control trajectory_interpolator
  ```
- **Descripción**: Se implementó una herramienta interactiva para mover las articulaciones del robot entre dos configuraciones alejadas en el espacio de articulaciones:
  * **Configuración A (Inicio)**: `[-60.0°, -45.0°, 45.0°, -30.0°, 0.0°]`
  * **Configuración B (Fin)**: `[60.0°, 30.0°, -30.0°, 30.0°, 0.0°]`
  La trayectoria tiene una duración parametrizada de 5 segundos y se calcula a una frecuencia de actualización de 50 Hz ($dt = 0.02\text{ s}$).

#### Métodos de Interpolación Implementados:
1. **Interpolación Lineal**:
   * **Posición**: $q(t) = q_A + \frac{t}{T}(q_B - q_A)$
   * **Velocidad**: $v(t) = \frac{q_B - q_A}{T}$
   * *Comportamiento*: La velocidad angular de cada articulación es constante a lo largo del movimiento. Sin embargo, al inicio y al final de la trayectoria se presentan discontinuidades en la velocidad (saltos instantáneos de cero al valor de crucero), lo que teóricamente genera picos de aceleración infinitos (sacudida mecánica brusca).

2. **Interpolación Cúbica**:
   * **Tiempo normalizado**: $\tau = \frac{t}{T} \quad (0 \le \tau \le 1)$
   * **Polinomio de interpolación**: $s(\tau) = 3\tau^2 - 2\tau^3$
   * **Posición**: $q(t) = q_A + s(\tau)(q_B - q_A)$
   * **Velocidad**: $v(t) = \frac{6\tau - 6\tau^2}{T}(q_B - q_A)$
   * *Comportamiento*: Garantiza que la velocidad al inicio y al final del movimiento sea exactamente cero ($v(0) = v(T) = 0$). El perfil de velocidad resultante es una parábola continua y suave (campana), eliminando las aceleraciones bruscas en las fronteras y logrando un movimiento de transición óptimo.

#### Gráficas de Análisis (Ubicadas en `results/interpolacion/`):
* **Interpolación Lineal (Posición y Velocidad)**:
  ![Interpolación Lineal](results/interpolacion/interpolacion_lineal.png)
* **Interpolación Cúbica (Posición y Velocidad)**:
  ![Interpolación Cúbica](results/interpolacion/interpolacion_cubica.png)
* **Comparativa de Suavidad en la Junta Base**:
  ![Comparativa de Suavidad](results/interpolacion/comparativa_interpolacion.png)

#### Conclusión de Suavidad:
* **Interpolación Lineal**: Genera discontinuidades en la velocidad al arrancar y frenar. Al ser el perfil de velocidad rectangular, las articulaciones del robot experimentan fuertes vibraciones e inercias mecánicas, lo cual puede forzar sobrecorrientes en los servomotores DYNAMIXEL o causar descalibración.
* **Interpolación Cúbica**: Genera transiciones suaves con aceleración acotada y continua. La velocidad inicia en cero, acelera uniformemente hasta un punto medio y desacelera suavemente hasta detenerse. Este método es el recomendado y utilizado para movimientos seguros y fluidos sobre el hardware real.

### Actividad 10. Trayectoria Sinusoidal de una Articulación
*Control dinámico de una articulación siguiendo el perfil:*
$$q(t) = q_0 + A \sin(2\pi f t)$$
- **Estado**: Pendiente
- **Pruebas Realizadas**:
  - Prueba 1: Amplitud $A_1$, Frecuencia $f_1$ -> Error RMS: `[Valor]`
  - Prueba 2: Amplitud $A_1$, Frecuencia $f_2$ -> Error RMS: `[Valor]`
  - Prueba 3: Amplitud $A_2$, Frecuencia $f_1$ -> Error RMS: `[Valor]`
  - Prueba 4: Amplitud $A_2$, Frecuencia $f_2$ -> Error RMS: `[Valor]`
- **Gráficas**: Las trayectorias deseadas vs. medidas se encuentran en [results/sinusoidal/](results/sinusoidal/).

### Actividad 11. Cinemática Directa
*Obtención de los parámetros Denavit-Hartenberg (D-H) e implementación del modelo en código.*

- **Estado**: Completado
- **Nodo**: `direct_kinematics` (paquete `pincher_control`)
- **Comando de ejecución**:
  ```bash
  ros2 run pincher_control direct_kinematics
  ```
- **Descripción**: Se implementó el cálculo de la cinemática directa mediante la convención de parámetros de Denavit-Hartenberg (DH) estándar en el script [direct_kinematics.py](file:///home/jesus-rivera/ros2_jazzy/phantom_ws/src/pincher_control/pincher_control/direct_kinematics.py). El programa recibe los valores angulares $q_1, q_2, q_3, q_4$ y calcula la pose cartesianas $x, y, z, \text{roll}, \text{pitch}, \text{yaw}$ en el extremo.

#### Parámetros Denavit-Hartenberg (DH) Estándar:

Para el manipulador PhantomX Pincher en su posición de home vertical, se obtuvieron las siguientes dimensiones físicas a partir del modelo URDF:
- $D_1 = 0.08945\text{ m}$ (Pedestal + waist link)
- $L_2 = 0.1010\text{ m}$, $L_m = 0.0315\text{ m}$ (Articulación Hombro $\rightarrow$ Codo)
- $L_3 = 0.1010\text{ m}$ (Articulación Codo $\rightarrow$ Muñeca)
- $L_4 = 0.1190\text{ m}$ (Longitud de la muñeca al extremo final link4)
- $\beta = \arctan2(L_m, L_2) \approx 0.3021\text{ rad}$ ($17.31^\circ$)
- $a_2 = \sqrt{L_m^2 + L_2^2} \approx 0.1058\text{ m}$

| Eslabón $i$ | Articulación | $\theta_i$ | $d_i$ (m) | $a_i$ (m) | $\alpha_i$ (rad) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Base ($q_1$) | $q_1$ | $0.08945$ | $0.0$ | $-\pi/2$ |
| **2** | Hombro ($q_2$) | $q_2 + \beta - \pi/2$ | $0.0$ | $0.1058$ | $0.0$ |
| **3** | Codo ($q_3$) | $q_3 - \beta$ | $0.0$ | $0.1010$ | $0.0$ |
| **4** | Muñeca ($q_4$) | $q_4$ | $0.0$ | $0.1190$ | $0.0$ |

*Rotación de herramienta (Tool orientation)*: Al final de la cadena cinemática, se aplica la matriz de transformación fija $T_{tool}$ correspondiente a la rotación del efector final: RPY $=[-\pi/2, 0.0, -\pi/2]$.

#### Resultados de la Comparación (DH vs. URDF/RViz)
Se evaluó la cinemática directa frente al modelo de referencia URDF en RViz para las 5 configuraciones de la Actividad 7:

1. **Configuración 1**: $q = [0.0^\circ, 0.0^\circ, 0.0^\circ, 0.0^\circ]$
   * **Calculada (DH)**: $x = 0.03150\text{ m}$, $y = 0.00000\text{ m}$, $z = 0.41045\text{ m}$ | RPY $=[0.00^\circ, 0.00^\circ, -180.00^\circ]$
   * **Observada (RViz)**: $x = 0.03150\text{ m}$, $y = 0.00000\text{ m}$, $z = 0.41045\text{ m}$ | RPY $=[0.00^\circ, 0.00^\circ, -180.00^\circ]$
   * **Error 3D**: **$0.000\text{ mm}$**
2. **Configuración 2**: $q = [25.0^\circ, 25.0^\circ, 20.0^\circ, -20.0^\circ]$
   * **Calculada (DH)**: $x = 0.17487\text{ m}$, $y = 0.08154\text{ m}$, $z = 0.34694\text{ m}$ | RPY $=[0.00^\circ, -25.00^\circ, -155.00^\circ]$
   * **Observada (RViz)**: $x = 0.17487\text{ m}$, $y = 0.08154\text{ m}$, $z = 0.34694\text{ m}$ | RPY $=[0.00^\circ, -25.00^\circ, -155.00^\circ]$
   * **Error 3D**: **$0.000\text{ mm}$**
3. **Configuración 3**: $q = [-35.0^\circ, 35.0^\circ, -30.0^\circ, 30.0^\circ]$
   * **Calculada (DH)**: $x = 0.13171\text{ m}$, $y = -0.09223\text{ m}$, $z = 0.35221\text{ m}$ | RPY $=[0.00^\circ, -35.00^\circ, 145.00^\circ]$
   * **Observada (RViz)**: $x = 0.13171\text{ m}$, $y = -0.09223\text{ m}$, $z = 0.35221\text{ m}$ | RPY $=[0.00^\circ, -35.00^\circ, 145.00^\circ]$
   * **Error 3D**: **$0.000\text{ mm}$**
4. **Configuración 4**: $q = [85.0^\circ, -20.0^\circ, 55.0^\circ, 25.0^\circ]$
   * **Calculada (DH)**: $x = 0.01360\text{ m}$, $y = 0.15545\text{ m}$, $z = 0.33737\text{ m}$ | RPY $=[0.00^\circ, -60.00^\circ, -95.00^\circ]$
   * **Observada (RViz)**: $x = 0.01360\text{ m}$, $y = 0.15545\text{ m}$, $z = 0.33737\text{ m}$ | RPY $=[0.00^\circ, -60.00^\circ, -95.00^\circ]$
   * **Error 3D**: **$0.000\text{ mm}$**
5. **Configuración 5**: $q = [80.0^\circ, -35.0^\circ, 55.0^\circ, -45.0^\circ]$
   * **Calculada (DH)**: $x = -0.00831\text{ m}$, $y = -0.04715\text{ m}$, $z = 0.39301\text{ m}$ | RPY $=[0.00^\circ, 25.00^\circ, -100.00^\circ]$
   * **Observada (RViz)**: $x = -0.00831\text{ m}$, $y = -0.04715\text{ m}$, $z = 0.39301\text{ m}$ | RPY $=[0.00^\circ, 25.00^\circ, -100.00^\circ]$
   * **Error 3D**: **$0.000\text{ mm}$**

### Actividad 12. Cinemática Inversa
*Implementación de la cinemática inversa analítica o numérica para la pose cartesianas.*
- **Estado**: Pendiente
- **Nodo**: `[Nombre del nodo]`
- **Criterios de Implementación**:
  - Cálculo de soluciones posibles (codo arriba / codo abajo).
  - Descarte de soluciones fuera de límites seguros.
  - Reporte de inalcanzabilidad.
  - Ejecución de la solución válida más cercana a la configuración actual del robot.
- **Validación**: Pruebas sobre 5 posiciones cartesianas distintas.

### Actividad 13. Enseñanza y Repetición de Poses
*Desarrollo de un modo de enseñanza que permite almacenar y reproducir una secuencia de poses.*
- **Estado**: Pendiente
- **Formato de Archivo**: Archivo de almacenamiento YAML (`poses.yaml`).
- **Capacidades**:
  - Almacenar al menos 8 poses con nombres identificadores.
  - Reproducción secuencial de poses con control de velocidad y tiempo de transición.
  - Parada de emergencia / detención de la reproducción.
- **Enlace al Video**: [Video de Enseñanza y Repetición](https://youtube.com/placeholder_video_teaching)

### Actividad 14. Trazado de una Figura
*Trazado físico con marcador o simulación virtual en RViz de una trayectoria geométrica mediante cinemática inversa punto a punto.*
- **Estado**: Pendiente
- **Figura seleccionada**: [Triángulo / Cuadrado / Círculo aproximado / Iniciales]
- **Descripción**: Definición de la trayectoria a partir de puntos cartesianos sucesivos resueltos mediante cinemática inversa.
- **Enlace al Video**: [Video de Trazado de Figura](https://youtube.com/placeholder_video_trazado)

### Actividad 15. Reto Final: Coreografía Robótica
*Diseño y sincronización de una coreografía fluida para el Phantom Pincher X100.*
- **Estado**: Pendiente
- **Obra musical seleccionada**: [Opción 1: youtube.com/watch?v=a-utnfedCDE / Opción 2: youtube.com/watch?v=OCZIzzQpJUw]
- **Duración**: `[Duración de la coreografía, mín. 45s]`
- **Características**: Ejecución de movimientos fluidos sincronizados con la melodía, involucrando todas las articulaciones en ciclo cerrado y sin intervención manual.
- **Enlace al Video Completo**: [Video de la Coreografía](https://youtube.com/placeholder_video_coreografia)

---

## 7. Diagramas y Planos
- **Diagrama de flujo de las acciones del robot**: [doc/diagrama_de_flujo.png](doc/diagrama_de_flujo.png) (pendiente).
- **Plano de planta del entorno de trabajo**: [doc/plano_de_planta.png](doc/plano_de_planta.png) (pendiente).

---

## 8. Conclusiones Individuales
- **Conclusiones de Jesus Alberto Rivera Molina**:
  1. La configuración inicial del robot (Home position) definida en el archivo URDF mediante Xacro permite predeterminar un comportamiento seguro y vertical al energizar el manipulador, facilitando las tareas de calibración de cero y prevención de colisiones con la superficie de trabajo.
  2. El uso de hilos independientes (multithreading) en nodos interactivos de consola ROS 2 es indispensable para evitar bloqueos del ejecutor principal (executor), logrando de esta forma la lectura continua de las posiciones físicas en `/joint_states` al mismo tiempo que se capturan entradas por teclado del usuario.
- **Conclusiones de Isaac Montes Luna**:
  1. El control de velocidad articular al 30% mediante el registro Dynamixel de perfil de velocidad (`/pincher/profile_velocity`) garantiza un desarrollo seguro en las pruebas de laboratorio, previniendo sobrecorrientes en los servomotores y reduciendo el desgaste mecánico por movimientos bruscos o mal parametrizados.
  2. La integración de mallas tridimensionales STL en la visualización de RViz2 optimiza la correspondencia espacial entre el gemelo digital y el manipulador físico, permitiendo previsualizar movimientos individuales y simultáneos antes de enviarlos a la plataforma real.

---

## 9. Instrucciones de Uso y Ejecución

### 1. Preparar el Espacio de Trabajo
Clonar el repositorio correspondiente del laboratorio y ubicarse en el directorio del workspace:
```bash
cd ros2_jazzy/phantom_ws
```

### 2. Compilar el espacio de trabajo
Compilar usando `colcon` y cargar las variables de entorno de ROS 2:
```bash
colcon build --symlink-install
source install/setup.bash
```

### 3. Lanzar el sistema completo (Simulado o Hardware)
Para iniciar el nodo controlador (`control_servo`), la interfaz gráfica interactiva (`pincher_gui`) y la visualización 3D (`rviz2`):

- **Modo Simulado (sin hardware conectado)**:
  ```bash
  ros2 launch pincher_control pincher_system.launch.py use_hardware:=false
  ```
- **Modo Real (con el robot PhantomX Pincher conectado)**:
  ```bash
  ros2 launch pincher_control pincher_system.launch.py use_hardware:=true port:=/dev/ttyUSB0 baudrate:=1000000
  ```

### 4. Lanzar la herramienta de control articular por consola
En una terminal secundaria (luego de hacer `source install/setup.bash`), se puede ejecutar el menú interactivo para mover articulaciones de manera individual y secuencial:
```bash
ros2 run pincher_control joint_mover
```

### 5. Lanzar únicamente la visualización URDF (con deslizadores de junta estándar)
Si se desea verificar únicamente el modelo en RViz de forma rápida y probar la cinemática visual:
```bash
ros2 launch pincher_description display_gui.launch.py
```

### 6. Lanzar el nodo de Interpolación de Trayectorias (Actividad 9)
En una terminal secundaria:
```bash
ros2 run pincher_control trajectory_interpolator
```

### 7. Lanzar el nodo de Cinemática Directa y DH (Actividad 11)
En una terminal secundaria:
```bash
ros2 run pincher_control direct_kinematics
```

---

> [!NOTE]
> Todos los videos demostrativos comienzan con la introducción oficial de LabSIR disponible en [este enlace de Google Drive](https://drive.google.com/file/d/1wSxw7m7n5hXOtkc8C0H0lLAxTx3BqQSe/view?usp=sharing).
