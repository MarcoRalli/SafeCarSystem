import socket
import cv2
import numpy as np




HOST = "169.254.108.159"  # Ethernet Interface Address PC
PORT = 65432
#HOST = "127.0.0.1"  # The server's hostname or IP address
#PORT = 80  # Port to listen on (non-privileged ports are > 1023)

all_data = b''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(4096)
            #print(f"Received {data!r}")
            print("dimensione dati ricevuti: ",len(data))

            if not data: #it is true when data == b'' 
                break
            #all_data.extend(data) NOT WORKS
            all_data = b"".join([all_data, data])
            print("dimensione temporanea all_data: ",len(all_data))
            #conn.send(data)


print("dimensione immagine: ",len(all_data))
image = np.asarray(bytearray(all_data))
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imwrite(r'C:\Users\39339\Desktop\photo1.jpeg', image)




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