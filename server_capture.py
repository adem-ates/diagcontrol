# server programm listening for connection from client
# coding: utf8

import io
import socket
import struct
import time
import picamera
import pickle
from io import StringIO
from fractions import Fraction

host = ''
port = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((host, port))
client_socket.listen(1)
#client_s
conn, addr = client_socket.accept() # akzeptiert den Verbindungsaufbau vom client
connection = conn.makefile('wb')    # macht aus der Verbindung eine Datei und nennt die Datei connection 

ss =  100000
#sx = 10000
#print(type(ss))

while 1:
         print(ss)
         camera = picamera.PiCamera()
         #camera.resolution = (640, 480)
         camera.resolution = (2592,1944)
         #camera.zoom = (0.25, 0, 0.45, 1)
         camera.sensor_mode = 3          #Sensor Mode 3 ist für lange Belichtungszei
         camera.framerate = Fraction(1,6) #wichtig ist das angeben der framerate, 1_6fps ist Minimum deme$
         camera.shutter_speed = ss # jdata["shutter_speed"]  #Belichtungszeit eins Frames max: 6s (mu Sec
         camera.awb_mode = 'off' # Weissabgleich aus dafür weiter unten awb_gains, sonst gab es Faarbeffe$
         camera.drc_strength = 'off'
         camera.exposure_mode = 'off' # Belichtungszeit Modus aus, sonst gab es farbeffekte
         camera.awb_gains = 1.5 #Verstärungsfaktor auf die roten und blauen Pixel
         time.sleep(2)
         camera.iso = 800        #Iso Wert Max 800
         # Start a preview and let the camera warm up for 2 seconds
#        camera.start_preview()
         time.sleep(2)
# Note the start time and construct a stream to hold image data
# temporarily (we could write it directly to connection but in this
# case we want to find out the size of each capture first to keep
# our protocol simple)
         start = time.time()
         stream = io.BytesIO()
# das hier ist der punkt warum beim drücken der Eingabetaste am Laptop am Pi das Foto
# gemacht wird. die for Schleife wartet an dieser Stelle auf eine Nachricht vom Client
# sobald in der data variable etwas reingeschrieben wird geht die for schleife weiter
         camera.capture(stream, 'png')
#       for foo in camera.capture_continuous(stream, 'jpeg'):
# Write the length of the capture to the stream and flush to
# ensure it actually gets sent
         connection.write(struct.pack('<L', stream.tell()))
         connection.flush()
# Rewind the stream and send the image data over the wire
         stream.seek(0)
         connection.write(stream.read())
# If we've been capturing for more than 30 seconds, quit
#                if time.time() - start > 30:
#                       break
# Reset the stream for the next capture

# das hier ist der punkt warum beim drücken der Eingabetaste am Laptop am Pi das Foto
# gemacht wird. die for Schleife wartet an dieser Stelle auf eine Nachricht vom Client
# sobald in der data variable etwas reingeschrieben wird geht die for schleife weiter
#         stream.seek(0)
#         stream.truncate()
         stream.close()
         camera.close()
         data = conn.recv(1024) # der Trick war, dass man nicht die connection Datei genommen hat sondern$
         if data:
           #sdata = str(data)#, 'utf-8')
           jdata = pickle.loads(data)
           #print(jdata["shutter_speed"])
           ss =  int(jdata["shutter_speed"])
           continue
         if not data:
           break
# Write a length of zero to the stream to signal we're done
# hier muss ich noch etwas machen, da durch die Obige if Schleife
# der folgende Befehl ungenutzt bleibt

connection.close()   
client_socket.close()
