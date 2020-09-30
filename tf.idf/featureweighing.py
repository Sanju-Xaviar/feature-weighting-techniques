from __future__ import division
import csv
import re                                                       #for string processing
import math
import sys

n1=33220
n2=33220
n=n1+n2
c1=[]
nc=[]
cmh3=[]
cme3=[]
englishwords=[]
count=0



with open(sys.argv[1], 'rb') as tweetfile:
        reader1 = csv.reader(tweetfile)
        for row in reader1:
                c1+=row
                count+=1
                print count

count=0

with open(sys.argv[2], 'rb') as tweetfile:
        reader1 = csv.reader(tweetfile)
        for row in reader1:
                nc+=row
                count+=1
                print count

count=0
myfile = open(sys.argv[3], 'wb')        #To empty the file first
#myfile.close()

with open(sys.argv[4], 'rb') as tweetfile:
        reader1 = csv.reader(tweetfile)
        for row in reader1:
            englishwords+=row
            count+=1
print englishwords

for cmh1 in nc:
        cmh2=re.findall(r"[\w']+", cmh1)
        cmh3+=cmh2

for cme1 in c1:
        cme2=re.findall(r"[\w']+", cme1)
        cme3+=cme2

for word in englishwords:
    print word 
    #if word in c1:
    a=0
    for word1 in cme3:
	if word==word1:                                                 
	    a+=1
    print "a"+str(a)
    b=n-a                    
    print "b"+str(b)
    c=0
    for word1 in cmh3:
	if word==word1:
	    c+=1
    print "c"+str(c)
    d=n-c      
    try:          
	    idf=int(math.log((n/(a+c)),2))
    except ZeroDivisionError:
	    idf=0
    myfile = open(sys.argv[3], 'a')
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, delimiter=',')
    csvrow=[]
    csvrow.append(word)	
    csvrow.append(idf)
    csvrow.append(a)
    csvrow.append(b)
    csvrow.append(c)
    csvrow.append(d)
    wr.writerow(csvrow)
    #myfile.close()
