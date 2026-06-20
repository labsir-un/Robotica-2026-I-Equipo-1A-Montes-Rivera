[![Ver video](https://img.youtube.com/vi/0VXu4NlrAs8/0.jpg)](https://youtu.be/0VXu4NlrAs8)


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Configuración Home - EPSON T3-401S</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 30px;
            background-color: #f4f7f6;
        }
        h1 {
            color: #1a365d;
            border-bottom: 3px solid #2b6cb0;
            padding-bottom: 10px;
            font-size: 28px;
        }
        h2 {
            color: #2c5282;
            margin-top: 30px;
            font-size: 20px;
        }
        p {
            margin-bottom: 15px;
        }
        code {
            background-color: #edf2f7;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 0.95em;
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin: 20px 0;
        }
        .articulaciones li {
            background: #fff;
            margin-bottom: 12px;
            padding: 15px 20px;
            border-left: 5px solid #3182ce;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        }
        .articulaciones li strong {
            color: #2b6cb0;
            display: block;
            margin-bottom: 5px;
            font-size: 1.1em;
        }
        .resumen {
            background-color: #ebf8ff;
            border-left: 5px solid #3182ce;
            color: #2c5282;
            padding: 15px 20px;
            margin: 25px 0;
            border-radius: 4px;
            font-weight: 600;
        }
        .razones li {
            background: #fff;
            margin-bottom: 15px;
            padding: 18px 20px;
            border-left: 5px solid #319795;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        }
        .razones li strong {
            color: #2c7a7b;
            font-size: 1.05em;
        }
    </style>
</head>
<body>

    <h1>Configuración Home</h1>

    <h2>2. Descripción física de la postura actual de tu robot</h2>
    <p>Con esta configuración guardada en el comando <code>HomeDef</code>, cuando mandes al robot a "Home" (ejecutando el comando <code>Home</code>), se colocará en la siguiente posición exacta:</p>
    
    <ul class="articulaciones">
        <li>
            <strong>J1 (Base) = 204800 pulsos (90°)</strong>
            El cuerpo o primer brazo del robot no apunta hacia el frente, sino que está apuntando completamente hacia la izquierda (alineado de forma paralela al eje Y positivo del robot).
        </li>
        <li>
            <strong>J2 (Codo) = 0 pulsos (0°)</strong>
            El segundo brazo está completamente estirado en línea recta respecto al primer brazo. No tiene ningún doblez en el codo.
        </li>
        <li>
            <strong>J3 (Eje Z Vertical) = 0 pulsos (0 mm)</strong>
            El eje vertical se encuentra en su punto más alto posible (retraído). La pinza o herramienta está levantada al máximo para evitar chocar con nada en la mesa.
        </li>
        <li>
            <strong>J4 (Eje U Rotación) = 0 pulsos (0°)</strong>
            El giro final de la punta de la herramienta se encuentra en su ángulo de referencia inicial.
        </li>
    </ul>

    <div class="resumen">
        En resumen: Verás al robot completamente estirado hacia tu izquierda y con el eje Z totalmente arriba.
    </div>

    <h2>3. ¿Por qué el programador configuró el Home así?</h2>
    <p>Esta es una de las configuraciones de seguridad más utilizadas en celdas de manufactura automatizada por las siguientes razones:</p>
    
    <ul class="razones">
        <li>
            <strong>Home Lateral de Seguridad (Side Park):</strong> 
            Al girar 90° a la izquierda y retraer el eje Z, el robot se "quita de en medio" de la zona central de trabajo. Esto permite que un operador humano pueda meter las manos al frente de la máquina de forma segura, o que pasen cajas/piezas por una banda transportadora central sin riesgo de que choquen con el robot mientras este descansa.
        </li>
        <li>
            <strong>Prevención de colisiones al arrancar:</strong> 
            Al iniciar el día o tras un paro de emergencia, si el operario presiona "Home", el robot primero subirá el eje Z (porque está en 0) y luego girará hacia la izquierda. Esto garantiza que la herramienta no arrastrará ni golpeará ningún componente que se haya quedado a medio procesar en la mesa de trabajo.
        </li>
    </ul>

</body>
</html>
