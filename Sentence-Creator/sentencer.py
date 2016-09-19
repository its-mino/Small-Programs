import random

def getWords(file_name):
	f = open(file_name, 'r')
	words = []
	for index, i in enumerate(f):
		words.append(i.strip())
	f.close()
	return words

#nouns
nouns = getWords('nouns.txt') #2334 words

#verbs
verbs = getWords('verbs.txt') #634 words

noun = nouns[random.randint(0,2333)]
verb = verbs[random.randint(0,633)]

if verb[len(verb)-1] == 'e':
	l = list(verb)
	del(l[len(l)-1])
	verb = ''.join(l)

if noun[len(noun)-1] == 's':
	print 'The ' + noun + ' are ' + verb + 'ing.'
else:
	print 'The ' + noun + ' is ' + verb + 'ing.'
