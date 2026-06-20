[![Ver video](https://img.youtube.com/vi/0VXu4NlrAs8/0.jpg)](https://youtu.be/0VXu4NlrAs8)

# Comparativa Técnica de Manipuladores Industriales: Motoman MH6 vs. ABB IRB 140 vs. EPSON T3-401S

Este documento presenta un cuadro comparativo detallado de las especificaciones técnicas de tres robots industriales con morfologías distintas. Esta información es útil para la caracterización física, el cálculo de matrices de transformación homógeneas (Denavit-Hartenberg) y la simulación cinemática/dinámica en **MATLAB**.

---

## Cuadro Comparativo Detallado

| Característica Técnica | Yaskawa Motoman MH6 | ABB IRB 140 | EPSON T3-401S |
| :--- | :--- | :--- | :--- |
| **Tipo de Estructura** | Antropomórfica (Articulado de 6 ejes) | Antropomórfica (Articulado de 6 ejes) | SCARA (Selective Compliance Assembly Robot Arm) |
| **Grados de Libertad (DoF)** | 6 | 6 | 4 |
| **Configuración de Juntas <br> *(Matriz en MATLAB)*** | `R-R-R-R-R-R` <br> (6 Revolutas) | `R-R-R-R-R-R` <br> (6 Revolutas) | `R-R-P-R` <br> (2 Revolutas, 1 Prismática, 1 Revoluta) |
| **Carga Máxima (Payload)** | 6.0 kg | 6.0 kg | 3.0 kg (Nominal: 1.0 kg) |
| **Alcance Máximo Horizontal** | 1422 mm | 810 mm (hasta eje 5) | 400 mm |
| **Carrera Vertical (Eje Z)** | N/A (Definido por su alcance articular) | N/A (Definido por su alcance articular) | 150 mm (Junta prismática J3) |
| **Repetibilidad** | ±0.08 mm | ±0.03 mm | ±0.02 mm (X, Y) / ±0.02 mm (Z) |
| **Velocidad Máxima por Eje** | **J1:** 220°/s <br> **J2:** 200°/s <br> **J3:** 220°/s <br> **J4:** 410°/s <br> **J5:** 410°/s <br> **J6:** 610°/s | **J1:** 200°/s <br> **J2:** 200°/s <br> **J3:** 260°/s <br> **J4:** 360°/s <br> **J5:** 360°/s <br> **J6:** 450°/s | **Tiempo de ciclo estándar:** 0.54 s <br> *(Velocidad angular combinada alta para Pick & Place)* |
| **Rango de Movimiento** | **J1:** ±170° <br> **J2:** -90° a +155° <br> **J3:** -175° a +250° <br> **J4:** ±180° <br> **J5:** -45° a +225° <br> **J6:** ±360° | **J1:** ±180° <br> **J2:** ±90° <br> **J3:** +110° a -230° <br> **J4:** ±200° (Estándar) <br> **J5:** ±115° <br> **J6:** ±400° | **J1:** ±132° <br> **J2:** ±141° <br> **J3:** 0 a 150 mm <br> **J4 (U):** ±360° |
| **Peso del Manipulador** | ~130 kg | ~98 kg | ~16 kg (All-in-One, controlador integrado) |
| **Controlador de Fábrica** | DX100 / DXM100 | IRC5 | Integrado (Software EPSON RC+) |
| **Aplicaciones Típicas** | • Soldadura por arco (Arc Welding)<br>• Ensamble mecánico<br>• Inyección de plásticos<br>• Manipulación de materiales pesados | • Cuidado de máquinas (Machine Tending)<br>• Rebabado y pulido<br>• Empaque y paletizado<br>• Aplicaciones en cuartos limpios | • Pick and Place de alta velocidad<br>• Ensamble de componentes electrónicos<br>• Automatización de laboratorios químicos<br>• Empaque farmacéutico primario |

---

## Notas de Relevancia para Simulación en MATLAB

Al implementar estos modelos robóticos mediante scripts de MATLAB, ten en cuenta las siguientes restricciones morfológicas:

### 1. Modelado de los Robots Antropomórficos (Motoman MH6 e IRB 140)
* Ambos comparten una configuración clásica de 6 Grados de Libertad con muñeca esférica.
* Al usar comandos como `rigidBodyTree` (Robotics System Toolbox) o la función `Link` (Peter Corke), todas las articulaciones deben ser configuradas como `'revolute'`.
* El **Motoman MH6** destaca por tener un alcance horizontal considerablemente mayor (casi el doble que el IRB 140), lo que expande drásticamente su matriz de espacio de trabajo (*Workspace*).

### 2. Modelado del Robot SCARA (EPSON T3-401S)
* A diferencia de los otros dos, el EPSON T3 posee únicamente 4 grados de libertad.
* En MATLAB, la tercera junta **(J3)** debe ser definida estrictamente como **`'prismatic'`** (prismática/lineal), configurando su movimiento en metros o milímetros en lugar de radianes/grados.
* El espacio de trabajo es cilíndrico. Es ideal para matrices de transformación bidimensionales en planos XY acoplados con una altura Z independiente.

# Configuración de Posición Home - EPSON T3-401S

## 1. Descripción física de la postura

cuando se manda al robot a su posición de inicio ejecutando el comando `Home`, se colocará en la siguiente posición exacta:

* **J1 (Base) = 204800 pulsos (90°):** El cuerpo o primer brazo del robot no apunta hacia el frente, sino que está apuntando completamente hacia la izquierda (alineado de forma paralela al eje Y positivo del robot).
* **J2 (Codo) = 0 pulsos (0°):** El segundo brazo está completamente estirado en línea recta respecto al primer brazo. No tiene ningún doblez en el codo.
* **J3 (Eje Z Vertical) = 0 pulsos (0 mm):** El eje vertical se encuentra en su punto más alto posible (retraído). La pinza o herramienta está levantada al máximo para evitar chocar con nada en la mesa de trabajo.
* **J4 (Eje U Rotación) = 0 pulsos (0°):** El giro final de la punta de la herramienta se encuentra en su ángulo de referencia inicial.

## 2. ¿Por qué el programador configuró el Home así?

Esta es una de las configuraciones de seguridad más utilizadas en celdas de manufactura automatizada por las siguientes razones:

1.  **Home Lateral de Seguridad (Side Park):** Al girar 90° a la izquierda y retraer el eje Z, el robot se "quita de en medio" de la zona central de trabajo. Esto permite que un operador humano pueda meter las manos al frente de la máquina de forma segura, o que pasen cajas/piezas por una banda transportadora central sin riesgo de que choquen con el robot mientras este descansa.

2.  **Prevención de colisiones al arrancar:** Al iniciar el día o tras un paro de emergencia, si el operario presiona "Home", el robot primero subirá el eje Z (porque está en `0`) y luego girará hacia la izquierda. Esto garantiza que la herramienta no arrastrará ni golpeará ningún componente o producto que se haya quedado a medio procesar en la mesa de trabajo.

# Procedimiento para Movimientos Manuales (Jogging) - EPSON T3-401S

Para realizar movimientos manuales en el robot **EPSON T3-401S**, se utiliza la interfaz virtual del software **EPSON RC+** desde una computadora conectada al manipulador. El epson del laboratorio carece de una consola física (*Teach Pendant*), por lo que todo el control se realiza mediante software.

---

## Paso 1: Abrir la ventana de Movimiento Manual (Jog & Teach)

1. Encienda el controlador y el robot. Posteriormente, ejecute el software **EPSON RC+** en su computadora.
2. Asegúrese de que el entorno esté conectado en modo **Online** con el robot.
3. En la barra de herramientas superior, haga clic en el icono **Jog & Teach** (representado por un robot con una mano) o presione la combinación de teclas `Ctrl + J`.
4. Se abrirá la ventana de control denominada *Jog & Teach*.

---

## Paso 2: Encender Motores (Motor ON)

Por motivos de seguridad, los servomotores arrancan en estado desenergizado. Antes de desplazar el robot, es necesario habilitarlos:

1. En la ventana de *Jog & Teach*, localice el botón etiquetado como **Motor On**.
2. Al hacer clic, se escucharán los frenos físicos liberándose en la base del manipulador y el indicador de estado en la pantalla cambiará a color **verde**.

---

## Paso 3: Selección del Modo de Operación (Coordenadas)

En la sección **Mode** o **Coordinate System**, se debe conmutar el tipo de trayectoria matemática que ejecutará el robot:

### Opción A: Modo Articulaciones (Joint)
* **Descripción:** Cada control físico o virtual actúa sobre un motor de forma independiente, ignorando la geometría cartesiana del espacio.
* **Comportamiento de los ejes:**
  * **J1 / J2:** Rotan de forma independiente el brazo de la base y el codo (valores en grados).
  * **J3:** Desplaza el vástago vertical hacia arriba o hacia abajo (valores en milímetros).
  * **J4:** Rota la herramienta en el extremo (eje U) en grados.

### Opción B: Modo Cartesiano (Base / World)
* **Descripción:** El software calcula la cinemática inversa en tiempo real para que el extremo de la herramienta se desplace en líneas rectas perfectas siguiendo el plano tridimensional de la celda de trabajo.

---

## Paso 4: Ejecución de Movimientos, Traslaciones y Rotaciones

Una vez seleccionado el modo, se habilitará el panel de botones con direcciones positivas
