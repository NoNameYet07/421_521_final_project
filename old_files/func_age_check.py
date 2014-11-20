def age_check(br_yr, cur_yr, cur_mo, cur_dt, br_mo, br_dt):

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
               
