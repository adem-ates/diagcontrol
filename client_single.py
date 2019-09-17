#!/usr/bin/env python
# coding: utf8
# client program connecting to server which is listening on port 50007

import io
import socket
import struct
import pickle
import time
import os
from PIL import Image

# The remote host
HOST = '192.168.0.105' 

PORT = 5002           # The same port as used by the server

ss1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss1.connect((HOST, PORT))
connection = ss1.makefile('rb')

tdata = {"shutter_speed": '10000', "frame_rate": "10"}
jdata = pickle.dumps(tdata)
i=1
try:
  while True:
# Read the length of the image as a 32-bit unsigned int. If the
# length is zero, quit the loop
    image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
    if not image_len:
     break
# Construct a stream to hold the image data and read the image
# data from the connection-
    image_stream = io.BytesIO()
    image_stream.write(connection.read(image_len))
# Rewind the stream, open it as an image with PIL and do some
# processing on it
    image_stream.seek(0)
    image = Image.open(image_stream) # open image 
    print('Image is %dx%d' % image.size) # resolution of image will be printed
    image.save(time.strftime('image1_%Y_%m_%d_%H%M%S.png')) # save image with the walking variable i
    i = i+1 # set iteration plus one
# hier sehr simpler Trick, while schleife wartet hier auf eine Eingabe in der Shell
# erst dann schickt der client (Laptop) die Nachricht check an den server (rpi)
# sobald Nachricht geschickt und der rpi erhalten hat geht while schleife weiter und
# der rpi macht das nächste Fotong
    
    x =  input('0 weiter ohne Änderung, 1 ändern, 2 beenden')
    x = str(x)
     
    if x == '1':
     shs = input('shutterspeed')
     tdata = {"shutter_speed": shs, "frame_rate": '10'}
     jdata = pickle.dumps(tdata)     
     ss1.sendall(jdata)
    if x == '0':
     ss1.sendall(jdata) # die vorherigen Variablen bleiben bestehen
    if x == '2':
     break

finally:
 connection.close()
 ss1.close()
