import os
import re
import sys
import csv

#Create vector for Hindi words
tweets=[]
with open(sys.argv[1], 'rb') as tweetfile:
	reader1 = csv.reader(tweetfile)
	for row in reader1:
	    tweets+=row

words=[]
with open(sys.argv[2], 'rb') as uniquevalidwordsfile:
	reader2 = csv.reader(uniquevalidwordsfile)
	for row in reader2:
	    words+=row

vector = [[0 for x in range(len(words))] for y in range(len(tweets))]
tweetnumber=0
for tweet in tweets:
	wordnumber=0
	for word in words:
		count=tweet.count(word)
		vector[tweetnumber][wordnumber]=count
		wordnumber+=1
	tweetnumber+=1

with open(sys.argv[3], "wb") as f:
    writer = csv.writer(f)
    writer.writerows(vector)
