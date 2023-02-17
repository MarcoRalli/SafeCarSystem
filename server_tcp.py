import os
import cv2
import socket
import numpy as np





HOST = "169.254.108.159"  # Ethernet Interface Address PC
PORT = 65432
#HOST = "127.0.0.1"  # The server's hostname or IP address
#PORT = 80  # Port to listen on (non-privileged ports are > 1023)

#@dest_folder = 'image'
def get_raspberry_image(dest_folder):
    all_data = b''
    i = len(os.listdir(dest_folder)) + 1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(8760)
                #print(f"Received {data!r}")
                #print("dimensione dati ricevuti: ",len(data))

                if not data: #it is true when data == b'' 
                    break
                #all_data.extend(data) NOT WORKS
                all_data = b"".join([all_data, data])
                #print("dimensione temporanea all_data: ",len(all_data))
                #conn.send(data)


    #print("dimensione immagine: ",len(all_data))
    image = np.asarray(bytearray(all_data))
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    path_captured_image = dest_folder + 'img%d.jpg' %i
    #print("percorso immagine: " + path_captured_image)
    cv2.imwrite(path_captured_image, image)
    

    return path_captured_image




 # convert to numpy array
#image = np.asarray(bytearray(data))
    
# RGB to Grayscale
#image = cv2.imdecode(image, 0)
    
# display image
#cv2.imshow("output", image)

#decimg=cv2.imdecode(data,0)
#cv2.imshow('SERVER',decimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows() 