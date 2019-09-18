#!/bin/sh

x="sudo shutdown now"

ssh rpi1@192.168.0.101 "$x" 

ssh rpi2@192.168.0.102 "$x" 

ssh rpi7@192.168.0.103 "$x"  

ssh rpi4@192.168.0.104 "$x" 

ssh rpi5@192.168.0.105 "$x" 

ssh rpi6@192.168.0.106 "$x" 