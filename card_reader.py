# bin/usr/python

# Setting up GPIO pins
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Identifies the pin numbers to the pi
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT) # Should sets pin #11 as an output...but doesnt work yet
GPIO.setup(3, GPIO.LOW) # Turns initial output for pin 3 off

# Setting up the current date

#while True.....do setup stuff first...
import time
timestr = time.strftime("%Y%m%d")

cur_yr=int(timestr[0:4]) #Using 4 digit year
cur_yr_2=int(timestr[2:4]) #Using 2 digit year
cur_mo=int(timestr[4:6])
cur_dt=int(timestr[6:8])

# Importing license data with card reader
import getpass

raw_text=getpass.getpass('Swipe card now:   ').strip()
example_text=raw_text.replace('\'', ' ').replace('\"', ' ').replace('\*', ' ')
#example_text='%MNEXCELSIOR^SAMANTHA JEAN PAULSEN^1501 KNOB HILL LN^?;636038744124870415=14101994062214?+" 55331      D               F069140   BRN                          *Y*)E     ?'

# Parsing license info for analyzing if over 21
split_text=example_text.split('=')
dates_text= split_text[1]

# Separate out dates by year, month, and day
# characters in format of exp_yr (2), exp_mo (2), br_yr (4), br_mo (2), br_d (2

exp_yr=int(dates_text[0:2])
exp_mo=int(dates_text[2:4])

br_yr=int(dates_text[4:8])
br_mo=int(dates_text[8:10])
br_dt=int(dates_text[10:12])

over_21='Beer Time!'
under_21='No beer for you!'
expired='Your license is expired'

# check to see that license is still valid

valid_license='No'

if cur_yr_2>exp_yr:
	print expired
elif cur_yr==exp_yr:
	if cur_mo>exp_mo:
		print expired
else:
	valid_license='Yes'

#Check to see if age is over 21
if valid_license=='Yes':

	if cur_yr-br_yr>21:
		print over_21

	elif cur_yr-br_yr==21:
		if cur_mo>br_mo:
			print over_21
		elif cur_mo==br_mo:
			if cur_dt>br_dt:
				print over_21
			
		elif cur_dt==br_dt:
			print 'Happy 21st  Birthday!'
		else:
			print under_21
			valid_license='No'
	else:		
		print under_21
		valid_license='No'
else:
	print under_21
	valid_license='No'

# Identifying the person

split_text_name=example_text.split('^')
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
		print 'Registered User'
		valid_license='Yes'
	else: 
		print 'Not registered user'
		valid_license='No'

# Opening the solenoid 

if valid_license=='Yes':
	GPIO.setup(3, GPIO.HIGH)
        sleep(2);
	GPIO.setup(3, GPIO.LOW)
