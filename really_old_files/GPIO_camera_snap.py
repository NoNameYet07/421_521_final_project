#! /usr/bin /python


# Setting up the picamera
import picamera
camera= picamera.PiCamera()

# Importing the time for naming image files
import time 
timestr = time.strftime("%Y%m%d-%H:%M:%S")

# Setting up pin configuration

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Identifies the pin numbers to the pi

GPIO.setup(7, GPIO.IN) # Sets pin #7 as the input pin for the button
GPIO.setup(11, GPIO.OUT) #Should set pin #11 as an output...but doesnt work yet
GPIO.setup(11, GPIO.HIGH) # Should turn pin 11 on...could use for controlling the transistor

# Running the if statement controlling the camera--button press snaps a pic

while True: 

	if (GPIO.input(7)==True):
		print 'button' #prints button whenever it detects a button press
		
	        camera.capture('photos/ID_Pic_'+timestr+'.jpg')
		print 'done' 
		sleep(1);
