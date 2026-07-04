import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, tty, termios
import time

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.escuchar_teclado)

    def move_turtle(self, letra_recibida):
        if letra_recibida == 'c':
            for _ in range(4):
                # 1. AVANZAR RECTO (Sin girar)
                msg = Twist()
                msg.linear.x = 2.0   
                msg.angular.z = 0.0  # <-- Cero rotación
                self.publisher_.publish(msg)
                time.sleep(1.0)      
                
                # 2. GIRAR 90 GRADOS EN SU LUGAR (Sin avanzar)
                msg = Twist()
                msg.linear.x = 0.0   # <-- Cero avance
                msg.angular.z = 1.57 # <-- Giro de 90 grados
                self.publisher_.publish(msg)
                time.sleep(1.0)      
                
            # 3. DETENER LA TORTUGA AL FINALIZAR
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('¡Tecla "c" detectada! Moviendo la tortuga')

    def escuchar_teclado(self):
        
        settings = termios.tcgetattr(sys.stdin)
        
        while rclpy.ok():
            tty.setraw(sys.stdin.fileno())
            select.select([sys.stdin], [], [], 0.1)
            key = sys.stdin.read(1)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
            
            # 2. Le enviamos la tecla detectada directamente a la función
            if key != '': # Solo para asegurarnos de que sí se presionó algo
                self.move_turtle(key)
            elif key == '\x03': 
                break
        
            
        



def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()