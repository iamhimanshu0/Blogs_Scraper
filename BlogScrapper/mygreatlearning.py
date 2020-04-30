from bs4 import BeautifulSoup
import requests

def myGreatLearning():
	link = "https://www.mygreatlearning.com/blog/category/data-science/"
	source = requests.get(link).text 
	soup = BeautifulSoup(source,'html.parser')
	# print(soup)
	link  = []
	title = []
	article = []
	data = soup.find('div',class_='td-pb-span8 td-main-content').find('div',class_='td-ss-main-content')
	for d in data.find_all('div',class_='td_module_11 td_module_wrap td-animation-stack'):
		l = d.find('div',class_='td-module-thumb').find('a').get('href')
		link.append(l)
		t = d.find('div',class_='item-details').find('h2',class_='entry-title td-module-title').text
		title.append(t)
		a= d.find('div',class_='td-excerpt').text.strip()
		article.append(a)
	
	return zip(link,title,article)


# data = myGreatLearning()

# for l,t,a in data:
# 	print(l)
# 	print(t)
# 	print(a)
# 	print("*"*50)
