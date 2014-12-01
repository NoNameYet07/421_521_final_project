#! usr/bin/python


# Setting up the current date
import time
timestr = time.strftime("%Y%m%d%H%M%S")


cur_yr=int(timestr[0:4]) #Using 4 digit year
cur_yr_2=int(timestr[2:4]) #Using 2 digit year
cur_mo=int(timestr[4:6])
cur_dt=int(timestr[6:8])



# To check license things...outputs valid_license if user is over 21 and license is valid

def check_license(n): # Checks for age and validity of license

    raw_text=n
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


    # Check to make sure card is a drivers license and obtainign DL number

    split_text_check=text.split(';')
    check_text= split_text_check[1]
    check_num=int(check_text[0:4])

    DL_num=check_text[6:14] #Save DL number for identification

    
    
    
    if check_num==6360:
        valid_license='Yes'
    else:
        valid_license='No'
        print 'Try swiping a drivers license'

    # check to see that license is still valid

    xpired= 'Sorry your license has expired'

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

    
    return (valid_license, first_name, last_name, DL_num)

# Function to calculate BAC ----------------------------------------------

def calc_BAC(n): # Calculates BAC based on physical info and # beers consumed

    import sys
    import re

    raw_text=n
    text=raw_text.replace('\'', ' ').replace('\"', ' ').replace('\*', ' ')

    #Splitting text to identify weight and gender

    phys_text=text.split('+') # Remove first half of code

    phys_NoSpace=re.sub(' ','',phys_text[1]) #Removing extra spaces

    phys_split=re.split('(\d+)',phys_NoSpace,flags=re.IGNORECASE) # split out whenever letters and numbers are together

    phys_info=phys_split[3]

#Finding the DL number
    split_text_check=text.split(';')
    check_text= split_text_check[1]
    check_num=int(check_text[0:4])

    DL_num=check_text[6:14] #Save DL number for identification

# Assigning weight obtained from DL

    weight_lb=int(phys_info[4:7])
    weight=weight_lb/2.2

# Assigning gender constant for BAC fomula

    if int(phys_info[0])==1 or 'F':
        gen_const= 0.58
    elif int(phys_info[0])==2 or 'M':
        gen_const= 0.49

# Assigning standard BAC constants 

    Body_H2O=0.806
    g_const=1.2
    t_const=0.015


        
## These variables will be defined elsewhere....

    users=open("swipes.txt", 'r')
   
    drink_list=[]
    BAC=0
    beer_size=16/12
    for line in users:
        if re.search(DL_num, line, re.IGNORECASE):
            unix_time=line.split(' ')[-1]

            time_diff_hrs=(time.time()-float(unix_time))/3600
            
            contributing_BAC=(Body_H2O*g_const*beer_size)/(weight*gen_const)-t_const*time_diff_hrs

            if contributing_BAC >0:
                    BAC=BAC + contributing_BAC


    
    return BAC

