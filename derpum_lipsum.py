#import random module
import random

#create dictionary 
derpy_list = ['derpy', 'derp', 'herp-derp', 'bederp', 'derpy', 'herp']

i = 1

firstword = random.choice(derpy_list)
cap = firstword.capitalize()
print cap,

i = 1

while i < 5:
	
	middle = random.choice(derpy_list)
		
	print middle,
		
	i = i + 1
	

lastword = random.choice(derpy_list)
print lastword + "."
