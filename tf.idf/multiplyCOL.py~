import csv
from collections import defaultdict
import math
import sys
count=0
tweets={}
myfile = open(sys.argv[1], 'wb')        #To empty the file first
myfile.close()
#with open('featureweighingtraining1.csv', 'rb') as tweetfile: # to get full column
#myfile = open('a.csv', 'wb')
#myfile.close()
#wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, delimiter=',')

myfile = open(sys.argv[1], 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, delimiter=',')
with open(sys.argv[2], 'rb') as tweetfile:					
	reader1 = csv.reader(tweetfile)
	j=0
	#z=0
	for row in reader1:
		print j
		#j=j+1
		with open(sys.argv[3], 'rb') as tweetfile1:
			reader2 =csv.reader(tweetfile1)
			#reader2.next()
			i=0
			ax=[]
			for row1 in reader2:
				if i==j:
					k=0
					for col in row1:
						print "k:",k,"j:",j	
						print int(row[1])*int(col)
						ax.append(int(row[1])*int(col))
						k=k+1
					wr.writerow(ax)
				i=i+1
				'''
				print "i:",i,"j:",j
				#print row1[i]
				print int(row[1])*int(row1[j])
				ax.append(int(row[1])*int(row1[j]))
				i=i+1
				#if i==2:
					#print row1[1024]
			wr.writerow(ax)'''
		j=j+1
			
'''infile = sys.argv[1]
outfile = sys.argv[4]

with open(infile) as f:
	reader = csv.reader(f)
	cols = []
	for row in reader:
		cols.append(row)

with open(outfile, 'wb') as f:
	writer = csv.writer(f)
	for i in range(len(max(cols, key=len))):
		writer.writerow([(c[i] if i<len(c) else '') for c in cols])'''

			
print k
print j


#print z
		
#print tweets

