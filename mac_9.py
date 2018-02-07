##########################
###
###
###  Day 3 Lecture, Text as Data Workshop
###
###
###
##########################
##convert to sets.  

import re, os
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

out = open('/users/justingrimmer/Dropbox/HouseData/NewListPress.csv', 'r')

press = out.readlines()


pos_words = urlopen('http://www.unc.edu/~ncaren/haphazard/positive.txt').read().split('\n')
neg_words = urlopen('http://www.unc.edu/~ncaren/haphazard/negative.txt').read().split('\n')

from nltk import PorterStemmer
from nltk import word_tokenize
st = PorterStemmer()



pos_stem = set(map(st.stem, pos_words))
neg_stem = set(map(st.stem, neg_words))




stop_words = urlopen('http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/a11-smart-stop-list/english.stop').read().split('\n')

stop_stemmed = map(st.stem, stop_words)

#pos_stem = [x for x in pos_stem if x not in stop_stemmed]
#neg_stem = [x for x in neg_stem if x not in stop_stemmed]


##now going through a big collection of press releases

output = open('/users/justingrimmer/dropbox/teaching/text/tad14/class4/ScorePress.csv', 'w')

output.write('Document,Num_Words,Pos_Words,Neg_Words')
output.write('\n')

def get_overlap(s,reference_set):
	return len(s&reference_set)
	
for z in range(1, len(press)):
	temp = press[z].strip('\n').split(',')[-1]
	start = open(temp, 'r').read()
	start2 = start.lower()
	start3 = re.sub('\W', ' ', start2)
	start4 = word_tokenize(start3)
	start5 = map(pt.stem, start4)
	num_words = len([x for x in start5 if x not in stop_stemmed])
	pos_words = len([x for x in start5 if x in pos_stem])
	neg_words = len([x for x in start5 if x in neg_stem])
	part = str(z) + str(num_words) + ',' + str(pos_words) +',' + str(neg_words)
	output.write(part)
	output.write('\n')
	if z %100 == 0:
		print z


output.close()

##this creates the figures, we can then use the output.




