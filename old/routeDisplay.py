'''
Jingxian You

2018.5.15

python 3.5.2

Preprocess the truncated file, find the route
'''

import csv
import datetime
from datetime import timedelta
with open('ProMED Posts 2016.csv',encoding="utf-8") as csvfile:
	reader = csv.DictReader(csvfile)
	diseaseDic = {}
	dateDic = {}
	longitudeDic = {}
	latitudeDic = {}
	locationDic = {}
	countryDic = {}
	alertList = []
	link = {}
	group = {}
	for line in reader:
		alertID = line["Alert ID"]
		alertList.append(alertID)
		diseaseDic[alertID] = line["Disease"]
		dateDic[alertID] = line["Date Posted"]
		try: 
			dateDic[alertID] = datetime.datetime.strptime(dateDic[alertID],"%m/%d/%y %H:%M")
		except:
			dateDic[alertID] = datetime.datetime.strptime(dateDic[alertID],"%m/%d/%Y %H:%M")
		longitudeDic[alertID] = line["Longitude"]
		latitudeDic[alertID] = line["Latitude"]
		locationDic[alertID] = line["Location"]
		countryDic[alertID] = line["Country"]
	num = len(alertList)
	i = 0
	d1 = timedelta(days = 1)
	d2 = timedelta(days = 15)
	
	while i < num:
		temp = diseaseDic[alertList[i]]
		date = dateDic[alertList[i]]
		j = i + 1
		while (j < num) and (date - (dateDic[alertList[j]]) < d2):
			if temp == diseaseDic[alertList[j]]:
				#print(temp,diseaseDic[alertList[j]],alertList[i],alertList[j])
				if alertList[i] != alertList[j]:
					if  date - (dateDic[alertList[j]]) > d1:
						#print(temp,diseaseDic[alertList[j]],alertList[i],alertList[j])
						link[alertList[i]] = alertList[j]
					else:
						#print(temp,diseaseDic[alertList[j]],alertList[i],alertList[j])
						group[alertList[i]] = alertList[j]
				break
			else:
				j = j + 1
		i = i + 1
	#print(group)
def links(keys):
	target = keys
	if target in link.keys():
		print('find it',link[target])
		links(link[target])
	else:
		return target
print(links('4053654'))