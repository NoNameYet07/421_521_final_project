# bin/usr/python

# Setting up GPIO pins
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Identifies the pin numbers to the pi
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT) # Should sets pin #3 as an output...but doesnt work yet
GPIO.setup(3, GPIO.LOW) # Turns initial output for pin 3 off

import time
timestr = time.strftime("%Y%m%d %H%M%S")

# Import functions to analyze license validity from CheckLicense.py
from CheckLicense import check_license, calc_BAC

                                 
import getpass
import sys
import re

# Operating modes
while True:
    #try:
    mode_req=raw_input("Enter Mode(normal, party, barkeep): ")

    if mode_req=="party":
         passwd=getpass.getpass("Enter password: ")
         if passwd=="admin":
                 mode="party"
                 
    if mode_req=="normal":
         passwd=getpass.getpass("Enter password: ")
         if passwd=="admin":
                 mode="normal"

    if mode_req=="barkeep":
         passwd=getpass.getpass("Enter password: ")
         if passwd=="admin":
                 mode="barkeep"

            
#Normal mode operations--------------------------------------------------------------------------------------------
    while mode=='normal':
            #try:
        print '{0} mode!' .format(mode)

        raw_text=getpass.getpass('Swipe card now:   ').strip() 

        check_license_out=check_license(raw_text)
            
        valid_license=check_license_out[0] 
        first_name=check_license_out[1]
        last_name=check_license_out[2]
        DL_num=check_license_out[3]
        
# Check to see if person is registered user

        users=open("users_list.txt", 'r')
        hit=0
        print DL_num
        
        if valid_license=='Yes':
              for line in users:
                      if re.search(DL_num, line, re.IGNORECASE):
                              hit=hit+1
              if hit>=1:
                      valid_license='Yes'
              else: 
                      print 'Not registered user'
                      valid_license='No'
# Calculating the BAC
    
        BAC=calc_BAC(raw_text)
        print BAC

    # Opening the solenoid 
        if valid_license=='Yes':
              GPIO.setup(3, GPIO.HIGH)
              print 'Beer time!'
              sleep(2);
              GPIO.setup(3, GPIO.LOW)
              with open("swipes.txt", "a") as myfile:
                      myfile.write(last_name+","+first_name+" ")
                      myfile.write(DL_num+" ")
                      myfile.write(mode+" ")
                      myfile.write(time.strftime("%Y-%m-%d")+" ")
                      myfile.write(str(time.time())+"\n")

       # except (NameError, IndexError, ValueError):
        #    print "error"
        #    continue

    #Party mode operations--------------------------------------------------------------------------------------------
                                     
    while mode=="party":
        try:
         print '{0} mode!' .format(mode)

         raw_license_text=getpass.getpass('Swipe card now:   ').strip()
         check_license_out=check_license(raw_license_text) 

         valid_license=check_license_out[0] 
         first_name=check_license_out[1]
         last_name=check_license_out[2] 


        # Opening the solenoid 

         if valid_license=='Yes':
                 GPIO.setup(3, GPIO.HIGH)
                 print 'Beer time!'
                 sleep(2);
                 GPIO.setup(3, GPIO.LOW)
                 with open("swipes_normal.txt", "a") as myfile:
                         myfile.write(last_name)
                         myfile.write(",")
                         myfile.write(first_name)
                         myfile.write(",")
                         myfile.write(time.strftime("%Y%m%d%H%M%S\n"))

        except (NameError, IndexError, ValueError):
             print "error"
             continue
                                  
    #Barkeep mode operations-------------------------------------------------------------------------------------------
     
    while mode=="barkeep":
        try:
            print '{0} mode!' .format(mode)

            check_license_out=check_license(getpass.getpass('Swipe card now:   ').strip()) 

            valid_license=check_license_out[0] 
            first_name=check_license_out[1]
            last_name=check_license_out[2] 
            #usr_chksum = #chksum(firstname_lastname)
            #'{0}beer_score' .format(usr_chksum) 
            #Check to see if person is blacklisted
            blacklist=open("blacklist.txt", 'r')
            hit=0

            if valid_license=='Yes':
                 for line in blacklist:
                         if re.search(last_name, line, re.IGNORECASE):
                                 hit=hit+1
                         if re.search(first_name, line, re.IGNORECASE):
                                 hit=hit+1
                 if hit>=2:
                         print "We don't serve your kind here."
                         blacklisted='Yes'
                 else: 
                         blacklisted='No'

            #Calculate BAC
                         
            #Opening the solenoid 
            if blacklisted=='No':
                if BAC < intoxicated:
                    GPIO.setup(3, GPIO.HIGH)
                    print 'Beer time!'
                    print BAC
                    sleep(2);
                    GPIO.setup(3, GPIO.LOW)
                    with open("swipes_barkeep.txt", "a") as myfile:
                         myfile.write(last_name)
                         myfile.write(",")
                         myfile.write(first_name)
                         myfile.write("_")
                         myfile.write(time.strftime("%Y-%m-%d %H:%M%S\n"))
                else:
                    print 'Your BAC is {0}' .format(BAC)
                    print "You are too drunk, beer time is over"
                 
        except (NameError, IndexError, ValueError):
             print "error"
             continue
                    
   # except (NameError, IndexError, ValueError):
        print "error"
       # continue
#end ---------------------------------------------------------------------------
        
