import csv
import re 
import sys

with open(sys.argv[1], 'r') as file :
  filedata = file.read()
  
# Replace the target string
filedata = filedata.replace('.', '')
filedata = filedata.replace('^', '')
filedata = filedata.replace('http:', '')
filedata = filedata.replace('www', '')
filedata = filedata.replace('html', '')
filedata = filedata.replace('//', '')
filedata = filedata.replace('/', '')
filedata = filedata.replace(',', '')
# Write the file out again
with open(sys.argv[2], 'w') as file:
  file.write(filedata)
