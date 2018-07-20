import os
from summa.keywords import keywords

#allFileNum = 0
def printPath(path):
	#global allFileNum
	filesList = os.listdir(path)
	for fileName in filesList:
		filePath = path + '\\' + fileName
		#print(filePath)
		f = open(filePath,'r',encoding = "utf-8")
		text = f.read()
		generated_keywords = keywords(text)
		outputPath = path + '_keywords' + '\\' + fileName + '_keywords.txt'
		outputFile = open(outputPath,'w',encoding = "utf-8")
		print(generated_keywords, file = outputFile)
	#print(files)

path = 'report\\reports\\temp\\2017'
printPath(path)