#! usr/bin/python
import time

# Current time
timestr = time.strftime("%Y%m%d%H%M%S")
cur_yr=int(timestr[0:4]) #Using 4 digit year
cur_yr_2=int(timestr[2:4]) #Using 2 digit year
cur_mo=int(timestr[4:6])
cur_dt=int(timestr[6:8])

def check_license(raw_text):
    '''Checks for age and validity of license.
    Input:
        raw_text (str) - raw input from driver's license
    Returns (dict):
        isValid (bool) - whether the user is over 21
        first_name (str) - user's first name
        last_name (str) - last name
        DL_num (int) - user's DL number'''
    class color:
        BOLD='\033[1m'
        END= '\033[0m'

    text=raw_text.replace('\'', ' ').replace('\"', ' ').replace('\*', ' ')

    # Check to make sure the swiped card is a drivers license and obtainign DL number
    check_text_check=text.split(';')[1]
    check_num=int(check_text[0:4]) # Indicator of drivers' licenses
    DL_num=check_text[6:14] #Save DL number for identification

    if check_num==6360:
        isValid=True
    else:
        isValid=False
        print 'Try swiping a drivers license'

    # Parsing license info to determine validity of license and age of user
    dates_text=text.split('=')[1]

    # Separate out dates by year, month, and day
    exp_yr=int(dates_text[0:2])
    exp_mo=int(dates_text[2:4])
    br_yr=int(dates_text[4:8])
    br_mo=int(dates_text[8:10])
    br_dt=int(dates_text[10:12])
    
    # check to see that license is still valid
    expired_msg = 'Sorry your license has expired!'
    if isValid:
        if cur_yr_2>exp_yr:
            print expired_msg
            isValid=False
        elif cur_yr_2==exp_yr:
            if cur_mo>exp_mo:
                    print expired_msg
                    isValid=False

    #Check to see if the user is over 21
    under_21_msg= 'You appear to be under 21 - no beer for you!'
    if isValid:
        if cur_yr-br_yr<21:
            isValid=False
            print under_21_msg
        elif cur_yr-br_yr==21:
            if cur_mo<br_mo:
                isValid=False
                print under_21_msg
            elif cur_mo==br_mo:
                if cur_dt<br_dt:
                    isValid=False
                    print under_21_msg
                elif cur_dt==br_dt:
                    print 'Happy 21st Birthday!'

    # Identifying the user's  name
    name_text=text.split('^')[1]
    names=name_text.replace('$', ' ').split(' ') # some DLs use $ and spaces in names
    first_name=names[0]
    last_name=names[-1]
    print color.BOLD + first_name, " ", last_name + color.END
    return {'isValid':isValid, 'first_name':first_name, 'last_name':last_name, 'DL_num':DL_num}
