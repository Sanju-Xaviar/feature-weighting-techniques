import csv
import re
import os
import sys

#read a file
f = open(sys.argv[1],'r')
f=f.read().splitlines()
print f
op=[]
c=0
f1=open(sys.argv[2],'w')
for ele in f:
	result=' '.join(ele)
	result=result.replace(" ","")
	print result
	c=c+1
	print c
	a=[result[i:i+5] for i in range (len(result)-5+1)]
	for item in a:
		f1.write(item)
		f1.write(" ")
	f1.write('\n') 
