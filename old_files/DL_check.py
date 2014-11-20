#! bin/usr/python

import getpass

raw_text=getpass.getpass('Swipe card now:   ').strip()
example_text=raw_text.replace('\'', ' ').replace('\"', ' ').replace('\*', ' ')

split_text=example_text.split(';')
check_text= split_text[1]

check_num=int(check_text[0:4])

print check_num

if check_num==6360:
	print 'woo'
else: print 'no'
