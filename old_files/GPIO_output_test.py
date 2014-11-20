#! /usr/bin /python


# Setting up pin configuration

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Identifies the pin numbers to the pi

GPIO.setup(7, GPIO.IN) # Sets pin #7 as the input pin for the button
GPIO.setup(3, GPIO.OUT) # Should sets pin #11 as an output...but doesnt work yet
GPIO.setup(3, GPIO.LOW) # Turns initial output for pin 3 off

# Running the if statement controlling an LED--pressing the button turns the LED on

while True: 

	if (GPIO.input(7)==True):
		print 'button' #prints button whenever it detects a button press
		GPIO.setup(3, GPIO.HIGH)
		sleep(1);
		GPIO.setup(3, GPIO.LOW)
