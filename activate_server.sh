#!/bin/sh

ssh rpi1@192.168.0.101 python  '/home/rpi1/server.py; exit' &

ssh rpi2@192.168.0.102 python  '/home/rpi2/server.py; exit' &

ssh rpi3@192.168.0.103 python  '/home/rpi3/server.py; exit' &

ssh rpi4@192.168.0.104 python  '/home/rpi4/server.py; exit' &

ssh rpi5@192.168.0.105 python  '/home/rpi5/server.py; exit' &

#ssh rpi6@192.168.0.106 python  '/home/rpi6/server.py; exit' &
