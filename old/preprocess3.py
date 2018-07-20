'''
Jingxian You

2018.5.4

python 3.5.2

Preprocess the text, extract entities with packages
'''
import nltk
from ExtractText import ExtractText
from py_aho_corasick import py_aho_corasick

def splitSentence(text):
	paragraph = ExtractText(text)
	#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	#sentences = tokenizer.tokenize(paragraph)
	sentences = nltk.sent_tokenize(paragraph)
	return sentences


#--------------------------------------------------import report-----------------------------------------------------#

#input report name
a = '20160101.3905373.json.parsed.json'

#input report direction
a1 = 'report\\' + a

#extract report ID
a2 = a.split('.')
#print(a2[0],a2[1])
#print(type(a[0]))

#splitsentences
sentences = splitSentence(a1)


#--------------------------------------------------import disease list as kv-----------------------------------------------------#
#import disease list
kv = []
direDisease = 'diseasesList\\epidemicDiseaseWHO.txt'
f = open(direDisease,'r')
lines = f.readlines()
for line in lines:
	temp = line.split(',')
	kv.append((temp[0],int(temp[1])))
#print(kv)

#--------------------------------------------------Aho Corasick algorithm-----------------------------------------------------#
i = 0
A = py_aho_corasick.Automaton(kv)

diseaseList = []
for sentence in sentences:
	text = lower(sentence)
	for idx,k,v in A.get_keywords_found(text):
	    assert text[idx:idx+len(k)] == k
	    assert v == dict(kv)[k]
	    diseaseList.append(v)
print(diseaseList)

'''
#output direction
dire = 'temp\\diseaseExtraction' + a2[0] + a2[1] + '.tmp'
f = open(dire,'w')

for sentence in sentences:
	
	print (, file = f)

f.close()
'''