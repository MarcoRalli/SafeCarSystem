import socket
import cv2
import os
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.resolution = (300, 200)
image_path = ''
for i in range(1):
    sleep(2)
    image_path = '/home/pi/Desktop/image%s.jpg' %i
    camera.capture(image_path)
camera.stop_preview()
print("Attuale image_path: ",image_path)

# Load image (it is loaded as BGR by default)
image = cv2.imread(image_path)
# Conver array to RGB
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image encoding
success, encoded_image = cv2.imencode('.jpg', image)
# convert encoded image to bytearray
content_bytes = encoded_image.tobytes()
print("dimensione immagine: ",len(content_bytes))




#HOST = "127.0.0.1"  # The server's hostname or IP address
#PORT = 80
HOST = "169.254.108.159"
PORT = 65432  # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.send(b"Hello, world") #senza il 'b' iniziale da problemi
    s.send(content_bytes)
    #data = s.recv(2400935)

#print(f"Received {data!r}")
print("photo sent")