'''
Jingxian You

2018.5.1

python 3.5.2

Build disease list
'''

import re
import sys

f1 = open("diseasesList.txt","r",encoding='utf-8')
lines = f1.readlines()
f2 = open("diseasesList\\diseasesList_O.txt","w")
for line in lines:
	a3 = re.compile('\—.*?\n')
	line = a3.sub('',line)

	a1 = re.compile('\[.*?\]')
	line = a1.sub('',line)
	a2 = re.compile('\(.*?\)')
	line = a2.sub('',line)

	a4 = re.compile(('\,.*?\n'))
	line = a4.sub('',line)

	if line != '\n':
		print(line, file = f2)
f1.close()
f2.close()