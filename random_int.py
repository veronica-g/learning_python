#!/usr/bin/env python3

import random
import time

# Single random-number generator "Roll the die"
#
# Steps:
# 1 - Greet and input the number of sides into a variable
# 2 - Print as many periods for "thinking time" but only a max of seven (it seemed good)
# 3 - Print the random value

def dots(x):
	if x>7:
		x=7
	for x in range(0, x):
		time.sleep(1)
		print('. ', end='', flush=True)
	time.sleep(1)
	return

sides=int(input("Hello, how many sides would you like on your die? "))
print('You have rolled a ', end='', flush=True)
dots(sides)
print(random.randint(1, sides))
