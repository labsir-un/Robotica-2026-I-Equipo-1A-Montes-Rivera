<h2> Decoración Automatizada con Robot Industrial</h2>
<p>
Sistema automatizado para la decoración de una torta virtual usando un robot industrial programado en RAPID.
Integra trayectorias, entradas/salidas digitales y control de banda transportadora.
</p>

<hr>

<h3> Arquitectura del sistema</h3>
<ul>
<li>Definición de posiciones <code>robtarget</code></li>
<li>Control principal en <code>main()</code></li>
<li>Trayectorias modulares <code>Path_x</code></li>
<li>Ejecución continua con <code>WHILE TRUE</code></li>
</ul>

<hr>

<h3> Control por entradas digitales</h3>

<h4>DI_01 – Inicialización</h4>
<ul>
<li>Activa <code>DO_01</code></li>
<li>Movimiento a HOME (<code>Path_120</code>)</li>
<li>Desactiva la salida</li>
</ul>

<h4>DI_02 – Proceso principal</h4>
<ul>
<li>Activa <code>DO_02</code></li>
<li>Controla la banda transportadora</li>
<li>Ejecuta todas las trayectorias de decoración</li>
</ul>

<pre>
Path_140 → Path_260 → Path_10 → Path_170 → Path_20 → Path_180 → ...
</pre>

<h4>DI_03 – Mantenimiento</h4>
<ul>
<li>Movimiento a posición segura (<code>Home_2</code>)</li>
<li>Espera 5 segundos</li>
<li>Retorno a HOME</li>
</ul>

<hr>

<h3> Trayectorias del robot</h3>
<ul>
<li><b>MoveJ:</b> movimiento articular</li>
<li><b>MoveL:</b> movimiento lineal</li>
<li><b>MoveC:</b> movimiento circular</li>
</ul>

<p>
Cada <code>Path</code> representa una parte del dibujo o decoración.
</p>

<hr>

<h3> Herramienta y referencia</h3>
<ul>
<li><code>MyNewTool</code>: marcador</li>
<li><code>Workobject_1</code>: superficie de la torta</li>
</ul>

<hr>

<h3> Control de profundidad</h3>
<ul>
<li>Z = 0 → dibujar</li>
<li>Z negativo → levantar herramienta</li>
</ul>

<hr>

<h3> Estrategia</h3>
<ul>
<li>Modularidad</li>
<li>Reutilización</li>
<li>Control por eventos</li>
<li>Simulación industrial</li>
</ul>

<hr>

<h3> Aplicaciones</h3>
<ul>
<li>Decoración automatizada</li>
<li>Pintura industrial</li>
<li>Procesos robotizados</li>
</ul>
