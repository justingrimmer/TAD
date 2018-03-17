##########################
###
###
###  Lecture 2, Macine Learning
###
###
###
##########################

###content from Frances Zlotnik's tutorial
#####whitespace in python

###Rewritten For Python 3.5 By Edwin Gavis

for x in range(0,10):
    print (x) 


for x in range(0,10):
    print (x) 

mylist = ["hello", "this", "is", "a", "list", "of", "strings"]
print (mylist[0])
print (mylist[1])

##There are four numeric data types in python, but 
#we will only regularly encounter two: ints and floats. 
#ints are whole numeric values; 
#floats are floating point numbers, or values with decimals. 
#This sounds like a trivial difference, but it's not.


x = 5
y = 3
x / y

###In most programming languages, including python versions before 3.0, dividing two ints will yield an int, but since ints can only be whole numbers, any remainder is truncated. The effect is that integer division will give the answer rounded down to the nearest whole number. You can avoid this by casting at least one of the inputs to a float.


float(x) / y


#print type(3)
#print type(3.0)


##

print (5 + 2)
print (5 - 2)
print (5 * 2)
print (5 / float(2))   #remember: integer division!
print (5 % 2)          #mod operator, returns the remainder of a division operation
print (5**2)           #expontiation




mybool = True
if mybool == True:
    print ("yes :D")
else: 
    print ("no :(")


mybool != True  



mybool2 = True

if mybool == True and mybool2 == True:
    print ("yes!")
else: 
    print ("no.")    


##string
a = "hello"
b = 'hello again'
print (type(a))
print (type(b))

#You can cast the contents of numeric variables to strings using str. Many functions, such as write, will only accept strings, so you will often need to do this type of casting on numeric variables. Note that you can't always tell whether something is a string just by looking at it.


x = 500
y = str(x)
print (x)
print (y)
print (type(x))
print (type(y))


##functions applied to string

##strings are immutable
fruit = "apple"
print (fruit.upper())
print (fruit)

fruit = fruit.upper()
print (fruit)

fruit[1]


fruit[0:3]


len(fruit)

##concatenating string

fruit + " and bananas"


x = 5
y = '5'

print (x+x)
print (y+y)


##string modifications

mystring = "I'd like to split this sentence into a list of words."
mystring.split(" ")

mystring.strip(".")


##default is whitespace

mystr = "  demonstration of whitespace stripping!!!!    ??      "
mystr.strip()


##replacing
mystr.replace(" ","")


####################Data structures

#Many tasks can be accomplished in several different ways, but selecting appropriate data structures can make a huge difference in the efficiency and speed of your code, and cut down on unnecessary work. You should choose the structure that is optimized for the particular task you need it to do. Some things to think about:

#What is the primary purpose of this collection? Does it simply need to store items, or does it need to be searchable?

#Will you need to modify the collection as you work with it, or will it remain static?

#Do you need to preserve the ordering of the elements?

#How big is your data? Many of the differences between these structures are trivial with small ammounts of data, but become important as your data grows.

#Some general tips:

#Searching is always more efficient with hashed objects. Searching a hashed object will always be faster than looping over an unhashed list.

#Take advantage of python's native hierarchical data structures. Dicts are extraordinarily efficient and useful (when appropriate) and it is well worth the effort to learn how to use them.

#Don't underestimate the difference that efficient code can make. Inefficient code on big data will eat up all of your RAM and cause your code to crash.

#Lists
#The workhorse data structure in python is the list. Lists are instantiated using square brackets, with elements separated by commas.


mylist = ["Central", "Florida", "is", "the", "true", "National", "champ"]


#Unlike vectors in R, python lists can contain heterogenous data types.

myHeterogenousList = ["string", 15, "another string", 2.0]

#Lists are nestable, and a list can contain any type of collection as an element, and you can easily iterate over list elements.

nestedList = ["apple", 2.0, [1,2,3], {'dictionaryKey': 'dictionaryValue'}, set(['setElement']) ]



for element in nestedList:
    print (type(element))


#You may come across example of list comprehension, which is a 
#handy syntax for creating a list from another list. 
#It is basically a one line for loop. For our purposes, 
#there is no reason to use this syntax instead of a for loop 
#unless you care about saving a little bit of typing. If you find it 
#confusing, just use a for loop. There are analagous methods 
#for sets and dicts as well.

veggies = ["carrot", "potato","spinach", "turnip"]
VEGGIES = [x.upper() for x in veggies]
print (VEGGIES)


print (veggies[1:3])
veggies.index("spinach")


#Lists are mutable, which means they can be modified and those changes will persist without being explicitly saved. You can add to the end of a list using append, or at a specific index using `insert

veggies.append("zucchini")
print (veggies)

##
veggies.insert(3, "kale")
print (veggies)

##
veggies.reverse()
print (veggies)


veggies.sort()
print (veggies)


##
veggies.remove("turnip")
print (veggies)

##pop will remove the last item from the list and return it.

a = veggies.pop()
print (a)
print (veggies)

##you can count the number of times a particular item occurs
veggies.append("potato")
veggies.count("potato")

##You can access alphabetical order in lists as well

print (min(veggies))
print (max(veggies))
print (len(veggies))


##Tuples are variant on lists; the main difference is that they are 
#immutable. If you have no need to change a list, or if you'd 
#like to to use a list but can't because your purpose 
#requires an immutable object (for instance, as a dictionary 
#key -- more on this below), use a tuple.

myTuple = (1, 2, 3, 4, 5)

#You can, however, search, index, and find attributes of tuples just as you would lists.


myTuple[1:3]

max(myTuple)

myTuple.index(3)


######Dictionaries
##Dictionaries or dicts are hierarchical data structures that 
##map items, consisting of keys and their corresponding values. 
##Unlike lists, dicts are hashed, which means they are much faster 
##and more efficient to search through. A dict is created with curly braces. There are a few ways of adding to a dictionary:





myDict = {"peanut butter": "jelly"}

#is equivalent to 
myDict = {}
myDict["peanut butter"] = "jelly"


##While values can be any data type or structure, keys may only be 
##immutable objects.


nums = {(1,2) : "one and two"}
nums


#The principle function of dicts is to facilitate quick searching of 
##associated values. If, say, I had a dict of phone numbers like 
##the following:

phoneNumbers = { 'joe' : 123456, 'mary': 5436789, 'phil': 2463579}

##I can find Joe's number by looking up the value associated with his name. As your data gets larger, this becomes much, much faster than looping over a list and checking whether each item is what you are looking for.



phoneNumbers['joe']

#is equivalent to
phoneNumbers.get("joe")

##Also get key value pairs
phoneNumbers.items()
phoneNumbers.keys()
phoneNumbers.values()


#Dicts can be nested, which means that they can contain other 
#dicts as values.


phoneNumbers["bill"] = {}
phoneNumbers["bill"]["home"] = 1234567
phoneNumbers["bill"]["cell"] = 9876543
phoneNumbers



##Dicts are unordered, which means they cannot be indexed. It 
##does not make sense to ask for the "first" or "last" item 
##in a dictionary because there is no inherent ordering to them.

#You can iterate over dictionaries using iteritems, but since they are unordered, 
##the order they will follow is not defined, and not reliable.

for a in phoneNumbers.items():
    print (a)

##################
####start webscraping.  


##let's start scraping.  We will tackle a simple problem first
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re, os

url  = urlopen('http://avalon.law.yale.edu/19th_century/gettyb.asp').read()
#print(url)


soup = BeautifulSoup(url)


text = soup.p.contents[0]


text_1 = text.lower()


text_2 = re.sub('\W', ' ', text_1)



from nltk import word_tokenize
from nltk import bigrams
from nltk import trigrams
from nltk import ngrams


text_3 = word_tokenize(text_2)

text_3_bi = bigrams(text_3)
text_3_tri = trigrams(text_3)
text_3_n = ngrams(text_3, 4)



stop_words = urlopen('http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/a11-smart-stop-list/english.stop').read()
stop_words = str(stop_words).split('\n')

##we can then identify the stop words and then eliminate them from the list

##this is code that executes a very simple for loop to check the list
text_4 = [x for x in text_3 if x not in stop_words]

##you can check what was removed with:

text_rem = [x for x in text_3 if x not in text_4]

##we're going to use a similar format to apply various stemming/lemmatizing/synonyms algorithms


from nltk.stem.lancaster import LancasterStemmer

st = LancasterStemmer()



from nltk.stem import PorterStemmer

pt = PorterStemmer()


from nltk.stem.snowball import EnglishStemmer

sb = EnglishStemmer()


from nltk.stem.wordnet import WordNetLemmatizer

wn = WordNetLemmatizer()


##let's examine the word ``better"
st.stem('better')
pt.stem('better')
sb.stem('better')
wn.lemmatize('better', 'a')

wn.lemmatize('families', 'n')

##
##applying the porter stemmer to the gettysburg address


text_5 = map(pt.stem, text_4)

##now creating a dictionary that will count the occurrence of the words

getty = {}
used = []
for word in text_5:
    if word in getty:
        getty[word] += 1
    if word not in getty and word not in used:
        getty[word] = 1
        used.append(word)

getty_count = list(getty.values())
getty_keys = list(getty.keys())


rfile = open('GettysburgFinal.txt', 'w')
rfile.write('stem, count')
rfile.write('\n')

for j in range(len(getty_keys)):
    rfile.write('%s,%s' %(getty_keys[j], getty_count[j]))
    rfile.write('\n')


rfile.close()


dtm = open('GettysburgFinalDTM.txt', 'w')


getty_words = 'Document'
getty_numbers = 'Address'
for m in range(len(getty_keys)):
    getty_words += ','
    getty_words += getty_keys[m]
    getty_numbers += ','
    getty_numbers += str(getty_count[m])


dtm.write(getty_words)
dtm.write('\n')
dtm.write(getty_numbers)


for m in range(len(getty_keys)):
    dtm.write(getty_keys[m])
    dtm.write(',')

dtm.write('\n')
dtm.write('address')

for m in range(len(getty_count)):
    dtm.write(str(getty_count[m]))
    dtm.write(',')

dtm.write('\n')

dtm.close()