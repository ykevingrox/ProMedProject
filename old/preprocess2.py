'''
Jingxian You

2018.5.4

python 3.5.2

Preprocess the text, extract entities with packages
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

dire = 'temp\\entityExtractTree' + a2[0] + a2[1] + '.tmp'
f = open(dire,'w')

for sentence in sentences:
	words = wordToken(sentence)
	posTaggedTokens = posTag(words)
	tree = nltk.ne_chunk(posTaggedTokens)
	print (tree, file = f)

f.close()
