'''
Jingxian You

2018.5.1

python 3.5.2

Preprocess the text, extract entities without packages
'''

import nltk
import nltk.data
from ExtractText import ExtractText

def splitSentence(text):
	paragraph = ExtractText(text)
	#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	#sentences = tokenizer.tokenize(paragraph)
	sentences = nltk.sent_tokenize(paragraph)
	return sentences

def wordToken(sentence):
	words = nltk.word_tokenize(sentence)
	return words

def lemmatization(wordsList):
	porter = nltk.PorterStemmer()
	temp = wordsList
	for t in temp:
		t = porter.stem(t)
	print(temp)
	return temp

def posTag(wordsList):
	temp = wordsList
	return(nltk.pos_tag(temp))

a = '20160101.3905373.json.parsed.json'
a1 = 'report\\' + a
a2 = a.split('.')
#print(a2[0],a2[1])
#print(type(a[0]))
sentences = splitSentence(a1)
entityCount = {}
entityPos ={}

for sentence in sentences:
	words = wordToken(sentence)
	posTaggedTokens = posTag(words)
	#wordStem = lemmatization(words)
	#print(posTaggedTokens)

	#posTaggedTokens = [token for sent in posTaggedTokens for token in sent]  
	#print(posTaggedTokens)
	allEntity = []
	allEntityPos = []
	previousPos = None
	currentEntity = []

	for tokens in posTaggedTokens:
		token = tokens[0]
		pos = tokens[1]
		#print(pos)
		if pos.startswith('NN'):
			if previousPos != pos:
				currentEntity = []
			currentEntity.append(token)
		elif currentEntity != [] and previousPos.startswith('NN'):
			entity = ''
			for t in currentEntity:
				entity = entity + ' ' + t
			allEntity.append(entity)
			allEntityPos.append(previousPos)
		previousPos = pos

	numberEntity = len(allEntity)
	i = 0
	for i in range(0,numberEntity):
		entityCount[allEntity[i]] = entityCount.get(allEntity[i],0) + 1
		entityPos[allEntity[i]] = allEntityPos[i]
'''
	numberEntity = len(allEntity)
	i = 0
	for i in range(0,numberEntity):
		print(i,allEntity[i],allEntityPos[i],entityCount[allEntity[i]])
'''

entityCountSorted = sorted(entityCount.items(), key=lambda item:item[1], reverse = True)

dire = 'temp\\entityCount' + a2[0] + a2[1] + '.tmp'
f = open(dire,'w')
for (k,v)  in entityCountSorted:
	print(k,v,entityPos[k], file = f)
f.close()