[![Ver video](https://img.youtube.com/vi/0VXu4NlrAs8/0.jpg)](https://youtu.be/0VXu4NlrAs8)


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
