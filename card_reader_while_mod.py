# bin/usr/python

# Setting up GPIO pins
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Identifies the pin numbers to the pi
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT) # Should sets pin #11 as an output...but doesnt work yet
GPIO.setup(3, GPIO.LOW) # Turns initial output for pin 3 off

# Setting up the current date

import time
timestr = time.strftime("%Y%m%d")

cur_yr=int(timestr[0:4]) #Using 4 digit year
cur_yr_2=int(timestr[2:4]) #Using 2 digit year
cur_mo=int(timestr[4:6])
cur_dt=int(timestr[6:8])

# Importing license data with card reader

while True:

#check to see if you swiped a license
	from swipe_parse import check_num

	if check_num==6360:
	      valid_license='Yes'
	else:
		valid_license='No'
		print 'Try swiping a drivers license'

# check to see that license is still valid

from swipe_parse import exp_yr, exp_mo

expired= 'Sorry your license has expired'

if valid_license=='Yes':

	if cur_yr_2>exp_yr:
		print expired
		valid_license='No'
	elif cur_yr_2==exp_yr:

		if cur_mo>exp_mo:
			print expired
			valid_license='No'

#Check to see if age is over 21

from swipe_parse import br_yr, br_mo, br_dt

under_21= 'Under 21. No beer for you'

if valid_license=='Yes':
	
	if cur_yr-br_yr<21:
		valid_license='No'
		print under_21
	elif cur_yr-br_yr==21:
		if cur_mo<br_mo:
			valid_license='No'
			print under_21
		elif cur_mo==br_mo:
			if cur_dt<br_dt:
				valid_license='No'
				print under_21
			elif cur_dt==br_dt:
				print 'Happy 21st  Birthday!'

# Identifying the person

from swipe_parse import first_name, last_name

print first_name
print last_name


# Check to see if person is registered user

import sys
import re

users=open("users_list.txt", 'r')
hit=0

if valid_license=='Yes':
	for line in users:
		if re.search(last_name, line, re.IGNORECASE):
			hit=hit+1
	if hit>=1:
		valid_license='Yes'
	else: 
		print 'Not registered user'
		valid_license='No'

# Opening the solenoid 

if valid_license=='Yes':
	GPIO.setup(3, GPIO.HIGH)
       	print 'Beer time!'
	sleep(2);
	GPIO.setup(3, GPIO.LOW)
