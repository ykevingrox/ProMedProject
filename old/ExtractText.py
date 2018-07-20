'''
Jingxian You

2018.4.22

python 3.5.2

Extract Text information from report
'''
import json

def ExtractText(path):
	f = open(path,'r')
	in_json = json.loads(f.read())
	post = (in_json['post_text'])
	location_1 = post.find('Subject')
	location_2 = post.find('-',location_1)
	location_3 = post.find('\n\n\n')
	location_3 = post.find('\n\n\n',location_3+1)
	location_4 = post.find('Communicated by:',location_3)
	#print(location_1, location_2, location_3)
	subject = post[location_1 + 9 : location_2 - 1]
	text = post[location_3 + 3 : location_4 - 5]
	return (text)
	#print(type(post))
	#-------------------NEED SPELL CORRECTION FIRST

	pass

#a = '20160101.3905373.json.parsed.json'
#text = ExtractText(a)