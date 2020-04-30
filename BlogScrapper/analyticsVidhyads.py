from bs4 import BeautifulSoup
import requests


def analyticsdsData():
	link = "https://www.analyticsvidhya.com/blog/category/data-science/"
	# link = "https://www.analyticsvidhya.com/blog/category/machine-learning/"
	source = requests.get(link).text 
	soup = BeautifulSoup(source,'html.parser')
	data = soup.find('div',class_='row block-streams el-module-2')
	link = []
	author = []
	author_link = []
	title = []
	article = []
	# print(data.prettify())
	for d in data.find_all('div',class_='up-up-child col-sm-6'):
		post = d.find('article',class_='item-medium post-box-big')
		l = post.find('div',class_='thumb-wrap zoom-zoom').find('a').get('href')
		link.append(l)
		
		a_name = post.find('div',class_='meta-info').find('span',class_='entry-author').text
		author.append(a_name)
		a_link = post.find('div',class_='meta-info').find('span',class_='entry-author').find('a').get('href')
		author_link.append(a_link)
		
		t = post.find('h3',class_='entry-title').text.strip() 
		title.append(t)
		
		a = post.find('div',class_='i-summary').text.strip()
		article.append(a)
		# print("*"*50)

	return zip(link, author, author_link, title, article)


# d = analyticsData()
# # print(d)

# for l, a_name, a_link, t, a in d:
# 	print(l)
# 	print(a_name)
# 	print(a_link )
# 	print(t)
# 	print(a)
# 	print("*"*50)
# 	print()
