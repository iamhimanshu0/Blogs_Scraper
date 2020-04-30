from bs4 import BeautifulSoup
import requests

def kdnuggetsData():
	link = "https://www.kdnuggets.com/news/index.html"
	source = requests.get(link).text 
	soup = BeautifulSoup(source,'html.parser')

	data = soup.find('ul',class_='three_ul')
	link = []
	article = []
	tags = []
	for d in data.find_all('li'):
		# get the link
		l = d.find('a').get('href')
		link.append(l)
		# print(link)
		#get data
		a = d.find('div').text
		article.append(a)
		# print(data)
		# get tags
		t = d.find('p',class_='tags').text 
		# print(tags)
		tags.append(t)
		# print('*'*50)

	return zip(link,article,tags)
		
# getdata = kdnuggetsData()
# for l,a,t in getdata:
# 	print(l)
# 	print(a)
# 	print(t)
# 	print("*"*50)