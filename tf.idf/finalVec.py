# to create an input matrix for SVM
import csv
import sys
#features{}

#myfile = open('texvector1.csv', 'wb')
#myfile.close()

datalist=[]
#gtfile = 'groundfile.csv'        #to give the label value
with open(sys.argv[1],'rb') as datafile: 
	reader1 = csv.reader(datafile)
	for rowa in reader1:
		datalist.append(rowa[0])  

with open(sys.argv[2],'rb') as vectorfile:
	reader2 = csv.reader(vectorfile)
	counter2=0
	for rowb in reader2:
		count=0
		trainingdatarow=[]
		myfile = open(sys.argv[3], 'a')
		wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, delimiter=' ')
		trainingdatarow.append(datalist[counter2])
		flag=0
		for col in rowb:
			count+=1
			print str(count)+':'+col
			print col
			if int(col)>0:
				flag=1
				trainingdatarow.append(str(str(count)+':'+col))
		counter2+=1
		if flag==1:
			wr.writerow(trainingdatarow)
		myfile.close()	


