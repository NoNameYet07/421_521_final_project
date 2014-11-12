#! /usr/bin/python

# from http://playground.arduino.cc/interfacing/python
import serial

import picamera

ser = serial.Serial('/dev/ttyACM0', 9600)
f = open('output.txt', 'w')
while True:
  output_line = ser.readline() 
#  print output_line
  f.write(output_line)


# Problem could be from newline (try chomp operation--python strip (rstrip))
if output_line == "Yes":
	camera=picamera.PiCamera()
	camera.capture('image.jpg')
	print output_line
