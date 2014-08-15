import requests
from bs4 import BeautifulSoup
import re

def get_webpage_content(url):
	webpage = requests.get(url)

	return webpage.content

def get_usage():
	c = get_webpage_content("https://www.start.ca/support/usage")
	soup = BeautifulSoup(c)

	for item in soup.find_all('div', class_ = 'content'):
		inner_div = str(item.div.li.get_text()).split()

	return inner_div[0]

#soup = BeautifulSoup(c)
#
#for item in soup.find_all('div', class_ = 'content'):
#	inner_div = item.div
#
#get_webpage_content("https://www.start.ca/support/usage")
#print(inner_div)

print(get_usage())