'''
Jingxian You

2018.5.15

python 3.5.2

Preprocess the truncated file, prepare for Tableau
'''

import csv
with open('ProMED Posts 2016.csv',newline= '') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')