#######
#######
####### HW 3 Key
#######
####### Adopted from Code from Frances Zlotnik



library(foreign)
uni_raw<- read.csv("unigrams.csv")
tri_raw<- read.csv("trigrams.csv")

#convert frequencies to rates
#take off id label and filenames
uni<- subset(uni_raw[,-c(1,2)])
tri<- subset(tri_raw[,-c(1,2)])

#calculate rates. 
for (i in 1:nrow(uni)){
    s<- sum(uni[i,])
    uni[i,]<- uni[i,]/s
}


#much faster, but returns a different type of data structure which requires a little more work to use
#norm<- function(x){
#    x<- x/sum(x)
#    return(x)
#}

#m<- t(apply(uni,1, function(x) norm(x)))

#add id back on
uni<-cbind(uni_raw$file, uni_raw$id, uni)
colnames(uni)[1:2]<- c("file", "id")

#same for trigrams
for (j in 1:nrow(tri)){
    s<- sum(tri[i,])
    tri[i,]<- tri[i,]/s
}
tri<-cbind(tri_raw$file, tri_raw$id, tri)
colnames(tri)[1:2]<- c("file","id")

#we will need these for our discriminant methods
#number of sessions and shelby docs
sessionsN<-table(uni$id)[1]
shelbyN<-table(uni$id)[2]

#unigrams
muShelbyU <- colMeans(uni[uni$id=="Shelby",-c(1,2)], na.rm=T)
muSessionsU<- colMeans(uni[uni$id=="Sessions",-c(1,2)], na.rm=T)
varShelbyU<- apply(uni[uni$id=="Shelby", -c(1,2)], 2, var)
varSessionsU<- apply(uni[uni$id=="Sessions", -c(1,2)], 2, var)




#trigrams
muShelbyT <- colMeans(tri[tri$id=="Shelby",-c(1,2)], na.rm=T)
muSessionsT<- colMeans(tri[tri$id=="Sessions",-c(1,2)], na.rm=T)
varShelbyT<- apply(tri[tri$id=="Shelby", -c(1,2)], 2, var)
varSessionsT<- apply(tri[uni$id=="Sessions", -c(1,2)], 2, var)
Mosteller and Wallace LDA
#unigrams
ldWeightsU<- (muShelbyU - muSessionsU) / (varShelbyU + varSessionsU)

#trigrams
ldWeightsT<- (muShelbyT - muSessionsT) / (varShelbyT + varSessionsT)

#trim weights - not necessary here
#ldWeightsU[abs(ldWeightsU)< 0.025]<- 0
#ldWeightsT[abs(ldWeightsT)< 0.025]<- 0

#ldWeightsT!="-Inf"]
ldWeightsU<- sort(ldWeightsU)
ldWeightsT<- sort(ldWeightsT)

#get 20 most discriminating words
LDmostSessionsU<- head(ldWeightsU, 10)
LDmostShelbyU<- tail(ldWeightsU, 10)
LDmostSessionsT<- head(ldWeightsT, 10) 
LDmostShelbyT<- tail(ldWeightsT, 10)


#plot
LDdiscrimU<-c(LDmostSessionsU, LDmostShelbyU)
LDdiscrimT<- c(LDmostSessionsT, LDmostShelbyT)
Standardized mean difference
#unigrams
numU<- muShelbyU - muSessionsU
denomU<- sqrt((varShelbyU/shelbyN) + (varSessionsU/sessionsN))
stdDiffU<-numU / denomU

#trigrams
numT<- muShelbyT - muSessionsT
denomT<- sqrt((varShelbyT/shelbyN) + varSessionsT/shelbyN)
stdDiffT<- numT/denomT

sdWeightsU<- sort(stdDiffU[stdDiffU!="-Inf"])
sdWeightsT<- sort(stdDiffT[stdDiffT!="-Inf"])

SDmostSessionsU<- head(sdWeightsU,10)
SDmostShelbyU<- tail(sdWeightsU, 10)
SDmostSessionsT<- head(sdWeightsT, 10)
SDmostShelbyT<- tail(sdWeightsT, 10)

SDdiscrimU<- c(SDmostSessionsU, SDmostShelbyU)
SDdiscrimT<- c(SDmostSessionsT, SDmostShelbyT)
Standardized Log Odds
#unigrams
totShelbyU<- sum(colSums(uni_raw[uni_raw$id=="Shelby", -c(1,2)]))
piShelbyU<- (colSums(uni_raw[uni_raw$id=="Shelby", -c(1,2)]) + 1)/(totShelbyU + (ncol(uni_raw)-1))
totSessionsU<- sum(colSums(uni_raw[uni_raw$id=="Sessions", -c(1,2)])) 
piSessionsU<- (colSums(uni_raw[uni_raw$id=="Sessions", -c(1,2)]) + 1)/(totSessionsU + (ncol(uni_raw)-1))

logOddsRatioU<- log(piShelbyU/ (1- piShelbyU)) - log(piSessionsU/ (1-piSessionsU))
varLogOddsU<- (1/(colSums(uni_raw[uni_raw$id=="Shelby", -c(1,2)]) + 1)) + (1/(colSums(uni_raw[uni_raw$id=="Sessions", -c(1,2)]) + 1)) 

stdLogOddsU<- logOddsRatioU/ sqrt(varLogOddsU)


#trigrams
totShelbyT<- sum(colSums(tri_raw[tri_raw$id=="Shelby", -c(1,2)]))
piShelbyT<- (colSums(tri_raw[tri_raw$id=="Shelby", -c(1,2)]) + 1)/(totShelbyT + (ncol(tri_raw)-1))
totSessionsT<- sum(colSums(tri_raw[tri_raw$id=="Sessions", -c(1,2)])) 
piSessionsT<- (colSums(tri_raw[tri_raw$id=="Sessions", -c(1,2)]) + 1)/(totSessionsT + (ncol(tri_raw)-1))

logOddsRatioT<- log(piShelbyT/ (1- piShelbyT)) - log(piSessionsT/ (1-piSessionsT))
varLogOddsT<- (1/(colSums(tri_raw[tri_raw$id=="Shelby", -c(1,2)]) + 1)) + (1/(colSums(tri_raw[tri_raw$id=="Sessions", -c(1,2)]) + 1)) 

stdLogOddsT<- logOddsRatioT/ sqrt(varLogOddsT)

sloWeightsU<- sort(stdLogOddsU)
sloWeightsT<- sort(stdLogOddsT)

sloSessionsMostU<- head(sloWeightsU,10)
sloShelbyMostU<- tail(sloWeightsU, 10)
sloSessionsMostT<- head(sloWeightsT, 10)
sloShelbyMostT<- tail(sloWeightsT, 10)

sloDiscrimU<- c(sloSessionsMostU, sloShelbyMostU)
sloDiscrimT<- c(sloSessionsMostT, sloShelbyMostT)
Unigram Plots
Plotting words with the largest (absolute value) weights.

index<- seq(1, 20, 1)

plot(LDdiscrimU, index, pch="", xlab="weight", ylab="", yaxt="n", main="Most discriminating words\n Linear Discriminant Analysis")
text(LDdiscrimU, index , label=names(LDdiscrimU), cex=.7)



############now answering questions
##1) Yes.  Principal components explain a fixed amount of variation.  If each 
##component explains the same amount, then the variance is low and the 
##principal component does a poor job---because each dimension explains about the same
##amount of information.  If variance is high, that occurs because one dimension is much larger than the average
##in this case, a small number of principal components is explaining more of the variation

##
prin_comp<- prcomp(dtm, scale = T)
plot(prin_comp$x[,1:2], pch='')
text(prin_comp$x[,1:2], labels = rownames(dtm))

###examine prin_comp$rotation[,1] and prin_cmp$rotation[,2]

documents<- list()
for(z in 1:nrow(dtm)){
	temp<- which(dtm[z,]>0)
	documents[[z]]<- rbind(temp,dtm[z,temp])
}
library(stm)
out<- prepDocuments(documents, colnames(dtm))
K<- 8
stm.out<- stm(out$documents, out$vocab, K = K, init = 'Spectral')

labelTopics(stm.out)

shelbs<- which(unis[,1]=='Shelby')
sess<- which(unis[,1]=='Session')

apply(stm.out$theta[shelbs,], 2, mean)
apply(stm.out$theta[sess,], 2, mean)








