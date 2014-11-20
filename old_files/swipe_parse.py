#! bin/usr/python
from card_reader_while_mod import raw_text

text=raw_text.replace('\'', ' ').replace('\"', ' ').replace('\*', ' ')


# Parsing license info for analyzing if over 21
split_text_age=text.split('=')
dates_text=split_text_age[1]
text=raw_text.replace('\'', ' ').replace('\"', ' ').replace('\*', ' ')


# Separate out dates by year, month, and day
# characters in format of exp_yr (2), exp_mo (2), br_yr (4), br_mo (2), br_d (2

exp_yr=int(dates_text[0:2])
exp_mo=int(dates_text[2:4])

br_yr=int(dates_text[4:8])
br_mo=int(dates_text[8:10])
br_dt=int(dates_text[10:12])

# check drivers ID No
split_text_check=text.split(';')
check_text= split_text_check[1]
check_num=int(check_text[0:4])

# Identifying the person

split_text_name=text.split('^')
name_text= split_text_name[1]

names=name_text.replace('$', ' ').split(' ') # some DLs use $ and space$


