path = 'report\\reports\\ProdMED_2016.csv'

def extractContent(path):
	f = open(path,'r',encoding = "utf-8")
	lines = f.readlines()
	for line in lines:
		text = line
		location_1 = text.find('?id=')
		location_2 = text.find('Source',location_1)
		location_3 = text.find('[See',location_2)
		content = text[location_2 + 8 :location_3]
		id = text[:7]
		str = 'report\\reports\\temp\\2016\\' + id + '.txt' 
		dir = open(str,'w',encoding = 'utf-8')
		print(content, file = dir)
		dir.close()
	f.close()	
extractContent(path)