import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

class YOLOv8Node(Node):
   def __init__(self):
      super().__init__('yolov8_node')
      self.bridge = CvBridge()
      self.sub = self.create_subscription(Image, '/main_camera/image_raw', self.image_callback, 10)
      self.model = YOLO('yolov8n.pt')  # Ganti ke model kamu
      self.get_logger().info("YOLOv8 node started")

   def image_callback(self, msg):
      frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
      results = self.model(frame)[0]
      annotated = results.plot()
      cv2.imshow("YOLOv8 Detection", annotated)
      cv2.waitKey(1)

def main(args=None):
   rclpy.init(args=args)
   node = YOLOv8Node()
   rclpy.spin(node)
   node.destroy_node()
   rclpy.shutdown()

if __name__ == '__main__':
   main()
