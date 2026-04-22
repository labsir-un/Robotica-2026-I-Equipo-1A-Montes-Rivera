<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Descripción del Proyecto</title>

<style>
    body {
        font-family: 'Segoe UI', Tahoma, sans-serif;
        background: #f5f7fa;
        margin: 0;
        padding: 20px;
    }

    .container {
        max-width: 1000px;
        margin: auto;
    }

    .card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        transition: transform 0.2s;
    }

    .card:hover {
        transform: translateY(-5px);
    }

    h1 {
        text-align: center;
        color: #2c3e50;
    }

    h2 {
        color: #34495e;
        border-left: 5px solid #3498db;
        padding-left: 10px;
    }

    h3 {
        color: #2c3e50;
        margin-top: 15px;
    }

    p {
        color: #555;
        line-height: 1.6;
    }

    ul, ol {
        color: #444;
        padding-left: 20px;
    }

    li {
        margin-bottom: 8px;
    }

    .tag {
        display: inline-block;
        background: #3498db;
        color: white;
        padding: 5px 10px;
        border-radius: 8px;
        font-size: 12px;
        margin-right: 5px;
    }

    .code-block {
        background: #2d3436;
        color: #dfe6e9;
        padding: 15px;
        border-radius: 10px;
        font-family: monospace;
        overflow-x: auto;
    }

    .highlight {
        background: #ecf0f1;
        padding: 10px;
        border-radius: 10px;
    }

</style>
</head>

<body>

<div class="container">

<h1>🤖 Decoración Automatizada con Robot Industrial</h1>

<div class="card">
    <h2>📌 Descripción general</h2>
    <p>
        El sistema implementa una solución automatizada para la decoración de una torta virtual utilizando un robot industrial programado en RAPID. Se integran trayectorias, señales digitales y control de una banda transportadora.
    </p>

    <div>
        <span class="tag">RAPID</span>
        <span class="tag">RobotStudio</span>
        <span class="tag">Automatización</span>
    </div>
</div>

<div class="card">
    <h2>⚙️ Arquitectura del sistema</h2>
    <ul>
        <li>Definición de posiciones <code>robtarget</code></li>
        <li>Control central en <code>main()</code></li>
        <li>Trayectorias modulares <code>Path_x</code></li>
        <li>Ejecución continua con <code>WHILE TRUE</code></li>
    </ul>
</div>

<div class="card">
    <h2>🔌 Control por entradas digitales</h2>

    <h3>DI_01 – Inicialización</h3>
    <ul>
        <li>Activa <code>DO_01</code></li>
        <li>Movimiento a HOME</li>
        <li>Desactiva salida</li>
    </ul>

    <h3>DI_02 – Proceso principal</h3>
    <ul>
        <li>Activa <code>DO_02</code></li>
        <li>Control de banda transportadora</li>
        <li>Ejecución completa de trayectorias</li>
    </ul>

    <div class="code-block">
Path_140 → Path_260 → Path_10 → Path_170 → Path_20 → Path_180 → ...
    </div>

    <h3>DI_03 – Mantenimiento</h3>
    <ul>
        <li>Posición segura</li>
        <li>Espera de 5 segundos</li>
        <li>Retorno a HOME</li>
    </ul>
</div>

<div class="card">
    <h2>📍 Trayectorias del robot</h2>
    <ul>
        <li><b>MoveJ:</b> movimiento articular</li>
        <li><b>MoveL:</b> movimiento lineal</li>
        <li><b>MoveC:</b> movimiento circular</li>
    </ul>

    <p class="highlight">
        Cada Path representa una parte del dibujo o decoración sobre la superficie.
    </p>
</div>

<div class="card">
    <h2>🛠️ Herramienta y referencia</h2>
    <ul>
        <li><code>MyNewTool</code>: marcador</li>
        <li><code>Workobject_1</code>: plano de la torta</li>
    </ul>
</div>

<div class="card">
    <h2>📏 Control de profundidad</h2>
    <ul>
        <li>Z = 0 → dibujar</li>
        <li>Z negativo → levantar herramienta</li>
    </ul>
</div>

<div class="card">
    <h2>🚀 Estrategia</h2>
    <ul>
        <li>Modularidad</li>
        <li>Reutilización</li>
        <li>Control por eventos</li>
        <li>Simulación industrial real</li>
    </ul>
</div>

<div class="card">
    <h2>🏭 Aplicaciones</h2>
    <ul>
        <li>Decoración de alimentos</li>
        <li>Pintura automatizada</li>
        <li>Procesos industriales</li>
    </ul>
</div>

</div>

</body>
</html>

