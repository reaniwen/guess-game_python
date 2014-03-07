#!/usr/bin/python
# Filename: guess-game.py 

import random

def guess(guessnum):
		if guessnum == number:
			print "step end"
			print 'Congratulations, you guessed it.' 
			print "(but you do not win any prizes!)" 
			print 'done'
		elif guessnum < number:
			#higher'
			print 'No, it is a little higher than that' 
			guessnum = int(raw_input('Enter an integer between 1 to 6: '))
			guess(guessnum)
		else:
			#lower'
			print 'No, it is a little lower than that' 
			guessnum = int(raw_input('Enter an integer between 1 to 6: '))
			guess(guessnum)


number = random.randint(1,6)
print number
guessnum = int(raw_input('Enter an integer between 1 to 6: '))
guess(guessnum)