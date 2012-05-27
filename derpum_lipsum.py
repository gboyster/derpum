#import random module
import random

#create dictionary 
derpy_list = ['derpy', 'derp', 'herp-derp', 'bederp', 'derpy', 'herp', 'herpy']


def main():
	ask = raw_input("sentence [s] or paragraph [p] > " )

	if ask[0].lower() == "s":
		sentence()
	elif ask[0].lower() == "p":
		number_of_graphs == raw_input("How many paragraphs?")
		print number_of_graphs
		'''
		if number_of_graphs == 1
			single_paragraph():
				else:
					main()
		'''
	else:
		print "hi"

def sentence():

	#selects first word from dictionary
	firstword = random.choice(derpy_list)
	
	# capitalizes first word
	cap = firstword.capitalize()
	print cap,

	#set random sentence length
	sentence_length = random.randint(1, 10)

	i = 1
	for i in range(sentence_length):
		
		middle = random.choice(derpy_list)
		print middle,
		
		i = i + 1
	
	#selects last word in sentence and adds period
	lastword = random.choice(derpy_list)
	print lastword + ".",


def single_paragraph():

	#set random sentence length
	paragraph_length = random.randint(3, 6)
	
	i = 1
	for i in range(paragraph_length):
		
		sentence()
					
	i = i + 1

	
main()