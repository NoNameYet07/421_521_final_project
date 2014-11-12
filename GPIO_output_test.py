#! /usr/bin /python


# Setting up pin configuration

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Identifies the pin numbers to the pi

GPIO.setup(7, GPIO.IN) # Sets pin #7 as the input pin for the button
GPIO.setup(3, GPIO.OUT) #Should set pin #11 as an output...but doesnt work yet
GPIO.setup(3, GPIO.LOW) # Should turn pin 11 on...could use for controlling the transistor

# Running the if statement controlling the camera--button press snaps a pic

while True: 

	if (GPIO.input(7)==True):
		print 'button' #prints button whenever it detects a button press
		GPIO.setup(3, GPIO.HIGH)
		sleep(1);
		GPIO.setup(3, GPIO.LOW)
