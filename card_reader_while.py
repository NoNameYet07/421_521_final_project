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
import getpass

while True:
	raw_text=getpass.getpass('Swipe card now:   ').strip()
	text=raw_text.replace('\'', ' ').replace('\"', ' ').replace('\*', ' ')



### Check to make sure card is drivers license

# Parsing license info for analyzing if over 21
	split_text_age=text.split('=')
	dates_text=split_text_age[1]

# Separate out dates by year, month, and day
# characters in format of exp_yr (2), exp_mo (2), br_yr (4), br_mo (2), br_d (2

	exp_yr=int(dates_text[0:2])
	exp_mo=int(dates_text[2:4])

	br_yr=int(dates_text[4:8])
	br_mo=int(dates_text[8:10])
	br_dt=int(dates_text[10:12])


# Check to make sure card is a drivers license


	split_text_check=text.split(';')
	check_text= split_text_check[1]
	check_num=int(check_text[0:4])

	if check_num==6360:
	      valid_license='Yes'
	else:
		valid_license='No'
		print 'Try swiping a drivers license'

# check to see that license is still valid

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

	split_text_name=text.split('^')
	name_text= split_text_name[1]

	names=name_text.replace('$', ' ').split(' ') # some DLs use $ and spaces in names

	first_name=names[0]
	last_name=names[-1]

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
