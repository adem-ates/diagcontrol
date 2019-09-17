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
#for i in range (1,6)
 #HOST_%s = ('192.168.0.%s' %i )

HOST1 = '192.168.0.101' 
HOST2 = '192.168.0.102'
HOST3 = '192.168.0.103'
HOST4 = '192.168.0.104'
HOST5 = '192.168.0.105'
##HOST6 = '192.168.0.106'

PORT = 5001           # The same port as used by the server

ss1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss1.connect((HOST1, PORT))
connection1 = ss1.makefile('rb')

ss2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss2.connect((HOST2, PORT))
connection2 = ss2.makefile('rb')

ss3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss3.connect((HOST3, PORT))
connection3 = ss3.makefile('rb')

ss4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss4.connect((HOST4, PORT))
connection4 = ss4.makefile('rb')

ss5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss5.connect((HOST5, PORT))
connection5 = ss5.makefile('rb')

##ss6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##ss6.connect((HOST6, PORT))
##connection6 = ss6.makefile('rb')

tdata = {"shutter_speed": '10000', "frame_rate": "10"}
jdata = pickle.dumps(tdata)
i=1
try:
  while True:
# Read the length of the image as a 32-bit unsigned int. If the
# length is zero, quit the loop
    image_len1 = struct.unpack('<L', connection1.read(struct.calcsize('<L')))[0]
    image_stream1 = io.BytesIO()
    image_stream1.write(connection1.read(image_len1))
    image_stream1.seek(0)
    image1 = Image.open(image_stream1) # open image 
    print('Image1 is %dx%d' % image1.size) # resolution of image will be printed
    image1.save(time.strftime('rpi1_%Y_%m_%d_%H%M%S.jpg')) # save image with the walking variable i
    if not image_len1:
     break
# Construct a stream to hold the image data and read the image
# data from the connection-
    image_len2 = struct.unpack('<L', connection2.read(struct.calcsize('<L')))[0]
    image_stream2 = io.BytesIO()
    image_stream2.write(connection2.read(image_len2))
    image_stream2.seek(0)
    image2 = Image.open(image_stream2) # open image 
    print('Image2 is %dx%d' % image2.size) # resolution of image will be printed
    image2.save(time.strftime('rpi2_%Y_%m_%d_%H%M%S.jpg')) # save image with the walking variable i
    
    image_len3 = struct.unpack('<L', connection3.read(struct.calcsize('<L')))[0]
    image_stream3 = io.BytesIO()
    image_stream3.write(connection3.read(image_len3))
    image_stream3.seek(0)
    image3 = Image.open(image_stream3) # open image 
    print('Image3 is %dx%d' % image3.size) # resolution of image will be printed
    image3.save(time.strftime('rpi3_%Y_%m_%d_%H%M%S.jpg')) # save image with the walking variable i
    
    image_len4 = struct.unpack('<L', connection4.read(struct.calcsize('<L')))[0]
    image_stream4 = io.BytesIO()
    image_stream4.write(connection4.read(image_len4))
    image_stream4.seek(0)
    image4 = Image.open(image_stream4) # open image 
    print('Image4 is %dx%d' % image4.size) # resolution of image will be printed
    image4.save(time.strftime('rpi4_%Y_%m_%d_%H%M%S.jpg')) # save image with the walking variable i
    
    image_len5 = struct.unpack('<L', connection5.read(struct.calcsize('<L')))[0]
    image_stream5 = io.BytesIO()
    image_stream5.write(connection5.read(image_len5))
    image_stream5.seek(0)
    image5 = Image.open(image_stream5) # open image 
    print('Image5 is %dx%d' % image5.size) # resolution of image will be printed
    image5.save(time.strftime('rpi5_%Y_%m_%d_%H%M%S.jpg')) # save image with the walking variable i
    print('default shutterspeed (ss) is: 10000mus')
##    image_len6 = struct.unpack('<L', connection6.read(struct.calcsize('<L')))[0]
##    image_stream6 = io.BytesIO()
##    image_stream6.write(connection6.read(image_len6))
##    image_stream6.seek(0)
##    image6 = Image.open(image_stream6) # open image 
##    print('Image6 is %dx%d' % image6.size) # resolution of image will be printed
##    image6.save(time.strftime('rpi6_%Y_%m_%d_%H%M%S.jpg')) # save image with the walking variable i
    

    i = i+1 # set iteration plus one
    
# hier sehr simpler Trick, while schleife wartet hier auf eine Eingabe in der Shell
# erst dann schickt der client (Laptop) die Nachricht check an den server (rpi)
# sobald Nachricht geschickt und der rpi erhalten hat geht while schleife weiter und
# der rpi macht das nächste Foto
    
    x =  input('0 keep default ss, 1 change ss, 2 close socket connection: ')
    x = str(x)
     
    if x == '1':
     shs = input('shutterspeed')
     tdata = {"shutter_speed": shs, "frame_rate": "10"}
     jdata = pickle.dumps(tdata)     
     
     ss1.sendall(jdata)
     ss2.sendall(jdata)
     ss3.sendall(jdata)
     ss4.sendall(jdata)
     ss5.sendall(jdata)
##     ss6.sendall(jdata)
    
    if x == '0': # die vorherigen Variablen bleiben bestehen
     ss1.sendall(jdata) 
     ss2.sendall(jdata)
     ss3.sendall(jdata)
     ss4.sendall(jdata)
     ss5.sendall(jdata)
##     ss6.sendall(jdata)
    if x == '2':
     break

finally:
 connection1.close()
 connection2.close()
 connection3.close()
 connection4.close()
 connection5.close()
## connection6.close()
 ss1.close()
 ss2.close()
 ss3.close()
 ss4.close()
 ss5.close()
## ss6.close()
