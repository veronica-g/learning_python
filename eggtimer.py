#!/usr/bin/env python3

import time
#----------------
#Function definitions
#----------------

def first_wait_period():
	x=6											# Alton recommends eight minutes. So we do
												# six here + 2 1m functions later for msgs
												
	for n in range(0, x):						# Do this loop x times (x mins)
		print('There are',x+2,'minutes left.')	# Print a running count of the time left
		time.sleep(60)							# Sleep one minute per loop iteration
		
		x=x-1									# Iterate
		
	return										# End of function


def min_seven():								# With two minutes left,
	print('Only two minutes left now!')			# egg the user on
	time.sleep(60)
	return


def min_eight():								# One minute
	print('Just sixty seconds to go!')			# warning!
	time.sleep(60)
	return

def egg_timer():
        print('The Alton Brown egg timer!')
        input('Boil egg(s) in kettle. Hit enter when the kettle shuts itself off')

        first_wait_period()
        min_seven()
        min_eight()

        print('Hooray your eggs are cooked, enjoy!')
        return

#----------------
# Main program
#----------------

egg_timer()
