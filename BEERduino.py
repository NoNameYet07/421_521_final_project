# bin/usr/python

#User defined variables----------------------------------------

open_time=2 # number of seconds the solenoid will remain open

beer_ABV= 0.05  # Alcoohol by volume for the current keg
ABV_ratio=beer_ABV/0.05

intoxicated=0.16 # BAC cutoff level

# Setting up other things--------------------------------------

# Setup GPIO pins

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Identifies the pin numbers to the pi
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT) # Should sets pin #3 as an output...but doesnt work yet
GPIO.setup(3, GPIO.LOW) # Turns initial output for pin 3 off

# Import necessary functions
import time
timestr = time.strftime("%Y%m%d %H%M%S")

from CheckLicense import check_license
from Calc_BAC import calc_BAC
                                 
import getpass
import sys
import re

# Setting up font classes
class color:
    BOLD='\033[1m'
    END= '\033[0m'
    GREEN= '\033[92m'
    



# Setting a while loop to run continuously and a try statement for error handling------------------

while True:
    #try:
    
# Operating modes---------------------------------------------------------------

    mode_req=raw_input("Enter Mode(normal, party, barkeep): ")

# Describe the different modes here

    if mode_req=="party":
         passwd=getpass.getpass("Enter password:")
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

        raw_text=getpass.getpass(color.GREEN + 'Swipe card now:   ' + color.END).strip() 

        check_license_out=check_license(raw_text)
            
        valid_license=check_license_out[0] 
        first_name=check_license_out[1]
        last_name=check_license_out[2]
        DL_num=check_license_out[3]
        
    # Check to see if person is registered user

        users=open("users_list.txt", 'r')

        hit=0
               
        if valid_license=='Yes':
              for line in users:
                      if re.search(DL_num, line, re.IGNORECASE):
                              hit=hit+1
              if hit>=1:
                      valid_license='Yes'
              else: 
                      print 'Not registered user'
                      valid_license='No'

    # Calculating the current BAC
    
        BAC1_raw=calc_BAC(raw_text)
        BAC1=format(BAC1_raw, '.3f')
       

    # Opening the solenoid to dispense beer
        if valid_license=='Yes':
              GPIO.setup(3, GPIO.HIGH)
              print 'Beer time!'
              sleep(open_time);
              GPIO.setup(3, GPIO.LOW)

              with open("swipes.txt", "a") as myfile:
                      myfile.write(last_name+","+first_name+" ")
                      myfile.write(DL_num+" ")
                      myfile.write(mode+" ")
                      myfile.write(time.strftime("%Y-%m-%d")+" ")
                      myfile.write(str(time.time())+"\n")

    # Calculating the BAC after finishing this beer
              BAC2_raw=calc_BAC(raw_text)
              BAC2=format(BAC2_raw, '.3f')

              print color.BOLD + "Your current BAC is",BAC1,"after this beer your BAC will be",BAC2 + color.END
              print " "
        
        # except (NameError, IndexError, ValueError):
        #    print "error"
        #    continue

#Party mode operations--------------------------------------------------------------------------------------------
                                     
    while mode=="party":
        try:
             print '{0} mode!' .format(mode)

             raw_text=getpass.getpass(color.GREEN + 'Swipe card now:   ' + color.END).strip() 

             check_license_out=check_license(raw_text)
                
             valid_license=check_license_out[0] 
             first_name=check_license_out[1]
             last_name=check_license_out[2]
             DL_num=check_license_out[3]

        # Calculating the current BAC
             BAC1_raw=calc_BAC(raw_text)
             BAC1=format(BAC1_raw, '.3f')


            # Opening the solenoid 

             if valid_license=='Yes':
                     GPIO.setup(3, GPIO.HIGH)
                     print 'Beer time!'
                     sleep(open_time);
                     GPIO.setup(3, GPIO.LOW)

                     with open("swipes.txt", "a") as myfile:
                         myfile.write(last_name+","+first_name+" ")
                         myfile.write(DL_num+" ")
                         myfile.write(mode+" ")
                         myfile.write(time.strftime("%Y-%m-%d")+" ")
                         myfile.write(str(time.time())+"\n")

        # Calculating the BAC after finishing this beer
        
                     BAC2_raw=calc_BAC(raw_text)
                     BAC2=format(BAC2_raw, '.3f')

                     print color.BOLD + "Your current BAC is",BAC1,"after this beer your BAC will be",BAC2 + color.END
                     print " "


        except (NameError, IndexError, ValueError):
             print "error"
             continue
                                  
#Barkeep mode operations-------------------------------------------------------------------------------------------
     
    while mode=="barkeep":
        #try:
        print '{0} mode!' .format(mode)

        raw_text=getpass.getpass(color.GREEN + 'Swipe card now:   ' + color.END).strip() 

        check_license_out=check_license(raw_text)
            
        valid_license=check_license_out[0] 
        first_name=check_license_out[1]
        last_name=check_license_out[2]
        DL_num=check_license_out[3]

    # Calculating the current BAC
        BAC1_raw=calc_BAC(raw_text)
        BAC1=format(BAC1_raw, '.3f')

        blacklist=open("blacklist.txt", 'r')

        hit=0
        
        if valid_license=='Yes':
             for line in blacklist:
                     if re.search(last_name, line, re.IGNORECASE):
                             hit=hit+1
                     if re.search(first_name, line, re.IGNORECASE):
                             hit=hit+1
             if hit>=2:
                     print "No beer for you!"
                     blacklisted='Yes'
             else: 
                     blacklisted='No'

                             
    #Opening the solenoid 
        if blacklisted=='No' and valid_license=='Yes':
            if BAC1 < intoxicated:
                GPIO.setup(3, GPIO.HIGH)
                print 'Beer time!'
                print BAC
                sleep(open_time);
                GPIO.setup(3, GPIO.LOW)

                with open("swipes.txt", "a") as myfile:
                     myfile.write(last_name+","+first_name+" ")
                     myfile.write(DL_num+" ")
                     myfile.write(mode+" ")
                     myfile.write(time.strftime("%Y-%m-%d")+" ")
                     myfile.write(str(time.time())+"\n")

    #Calculating the BAC after finishing this beer
                     BAC2_raw=calc_BAC(raw_text)
                     BAC2=format(BAC2_raw, '.3f')
                     print color.BOLD + "Your current BAC is",BAC1,"after this beer your BAC will be",BAC2 + color.END
                     print " "


            else:
                print "Sorry, BAC is too high"
                print " "
                

    
       

               
        #except (NameError, IndexError, ValueError):
         #    print "error"
          #   continue
                    
   # except (NameError, IndexError, ValueError):
        #print "error"
       # continue
#end ---------------------------------------------------------------------------
        
