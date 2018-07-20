import os
import nltk

sno = nltk.wordnet.WordNetLemmatizer()

#allFileNum = 0
def printPath(path):
	#global allFileNum
	filesList = os.listdir(path)
	
	outputPath = path + '\\keywords_2017.csv'
	outputFile = open(outputPath,'w',encoding = "utf-8")
	
	#dataBase = open(path2,'r',encoding = "utf-8")
	
	for fileName in filesList:
		keywordList = []
		filePath = path + '\\' + fileName
		#print(filePath)
		id = fileName[:6]
		
		#get keywords list
		f1 = open(filePath,'r',encoding = "utf-8")
		text = f1.readlines()
		for line in text:
			line = line[:-1]
			line2 = line.strip('_')
			keywordList.append(line2)
		f1.close()
		
		#add location and disease to keywords list
		pass
		
		#filter keywords
		keywordListStemmered = []
		count = 0;
		keywordListNew = []
		keywordListStemmeredNew = []
		for word in keywordList:
			keywordListStemmered.append(sno.lemmatize(word))
			count = count + 1
		for i in range(0,count):
			if keywordListStemmered[i] not in keywordListStemmeredNew:
				keywordListStemmeredNew.append(keywordListStemmered[i])
				keywordListNew.append(keywordList[i])
		print(id,keywordListNew, file = outputFile)
	#print(files)
	outputFile.close()
path = 'report\\reports\\temp\\2017_keywords'
path2 = 'report\\reports\\ProdMED_2017'
printPath(path)