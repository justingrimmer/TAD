##########################
###
###
###  Lecture 3, Macine Learning
###
###
###
##########################




library(tm)
##loading the synder emails 
emails <- read.delim('SnyderText.txt')

emails2 = tolower(emails[,1])

corp<- Corpus(VectorSource(emails2))

dtmSW = DocumentTermMatrix(corp, control = list(tolower=TRUE, stripWhitespace=TRUE, stopwords = TRUE ))

square.mat<- as.matrix(dtmSW)

###we can perform the same operations in python (and allow for more customization, but this will suffice for now)

##the function dist() allows for calculation of distances

##check the help file on distance.  note that it takes as an argument any square matrix
##the methods refer to different distance metrics.  The default is Euclidean

?dist

##use the method to calculate the euclidean distance between the documents.
store<- dist(square.mat)

##this creates an object of class distance. you can make a matrix with 
store<- as.matrix(store)

##what is the dimension of the matrix? 
dim(store)


##for each email identify the email that is ``closest" (smallest distance) (other than the email itself)
##store the email number in a vector 

##hint, use a for loop and the order function, but be sure to not select the same document

prox<- c()
for(z in 1:nrow(dtmSW)){
	prox[z]<- order(store[z,])[2]

	}
##now, write a function to compute the cosine similarity between two vectors.

cosine<- function(x, y){
	x.norm<- x/sqrt(x%*%x)
	y.norm<- y/sqrt(y%*%y)
	out<- x.norm%*%y.norm
	return(out)
	
	}

##use the function to compute the similarity between all the emails
##you'll 

store_sim<- matrix(NA, nrow = nrow(store), ncol = nrow(store))

for(z in 1:nrow(store)){
	for(y in 1:nrow(store)){
		store_sim[z,y]<- store[y,z]<- cosine(square.mat[z,], square.mat[y,])
		}
		}
		
##now, find the most similar documents for each email and store it in a vecor

prox_cos<- c()
for(z in 1:70){
	prox_cos[z]<- order(store_sim[z,], decreasing=T)[2]
	}

