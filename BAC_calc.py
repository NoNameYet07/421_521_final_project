
import re

text=raw_input()

# Splitting text to identify weight and gender

phys_text=text.split('+') # Remove first half of code

phys_NoSpace=re.sub(' ','',phys_text[1]) #Removing extra spaces

phys_split=re.split('(\d+)',phys_NoSpace,flags=re.IGNORECASE) # split out whenever letters and numbers are together

phys_info=phys_split[3]

# Assigning gender constant

if int(phys_info[0])==1:
    gen_const= 0.58
elif int(phys_info[0])==2:
    gen_const= 0.49

# Assigning other BAC constants 

Body_H2O=0.806
g_const=1.2
t_const=0.015

# Assigning weight

weight_lb=int(phys_info[4:7])
weight=weight_lb/2.2

## These variables will be defined elsewhere....

no_drinks=1
std_drinks=no_drinks*(16/12)

hours=0




# Calculating BAC

BAC=(Body_H2O*g_const*std_drinks)/(weight*gen_const)-t_const*hours
print BAC



#start = time.clock()
#... do something
#elapsed = (time.clock() - start)