#import random module
import random, sys 

#create dictionary 
derpy_list = ['derpy', 'derp', 'herp-derp', 'bederp', 'derpy', 'herp', 'herpy']


def main():
	ask = raw_input("sentence [s] or paragraph [p] > " )

	#if the first letter is 's'
	if ask[0].lower() == "s":
		#call sentence function
		sentence()
	#if first letter is 'p'
	elif ask[0].lower() == "p":
		number_of_graphs = raw_input("How many paragraphs? ")
		paragraph(number_of_graphs)
	elif ask[0].lower() == "q":
		sys.exit()
	#no response start over
	else:
		print "Sorry, incorrect response"
		main()

def sentence():

	#selects first word from dictionary
	firstword = random.choice(derpy_list)
	
	# capitalizes first word
	cap = firstword.capitalize()
	print cap,

	#set random sentence length
	sentence_length = random.randint(1, 10)

	#body of sentence
	
	i = 1
	for i in range(sentence_length):
		
		middle = random.choice(derpy_list)
		print middle,
		
		i = i + 1
	
	#selects last word in sentence and adds period
	lastword = random.choice(derpy_list)
	print lastword + ".",


def paragraph(how_many_graphs):

	# set outer loop: how many graphs, taken from raw_input 
	for i in range(int(how_many_graphs)):	

			
		#set inner loop: random sentence length
		paragraph_length = random.randint(3, 12)
		
		i = 1
		
		#use randomly set paragraph length to determine how many times to call sentence function 
		for i in range(paragraph_length):
			#call sentence function
			sentence()
		
		#print new paragraph
		print "\n"				
		
		#iterate inner loop				
		i = i + 1
	
	#iterate outer loop	
	i = i + 1

#call main function
main()


