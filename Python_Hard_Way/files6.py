def break_words (stuff):
	words = stuff.split (' ')
	return words

def sort_words (stuff):
	words = sorted (stuff)
	return words

def print_first_word (words):
	#word = break_words (words)
	first_word = words.pop (0)
	print first_word

def print_last_word (words):
	word = words.pop (-1)
	print word

def sort_sentence (sentence):
	words = break_words (sentence)
	return sort_words (words)
	#return sorted (sentence)

def print_first_and_last (sentence):
	words = break_words (sentence)
	first = words.pop (0)
	last = words.pop (-1)
	print first, last

def print_first_and_last_sorted (sentence):
	words = sort_sentence (sentence)
	first = words.pop (0)
	last = words.pop (-1)
	print first, last