from bs4 import BeautifulSoup
import requests
import csv

#Use FOR Loop to loop through pages; END FOR Loop @ line 30
#Using GET Request
page = requests.get("https://hackthenorth2017.devpost.com/submissions")
#print(page.text)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
li = []
substring = "https://devpost.com/software"
for a in soup.find_all('a', href=True):
	#print(a['href'])
	if substring in a['href']:
		li.append(a['href']) 
li = li[0:24]
print(li)

for item in li:
	page = requests.get(item)
	soup = BeautifulSoup(page.content, 'html.parser')
	test = soup.find_all('p')[2].get_text()
	print(test)

#Issue with p-tags: random p-tags pop up for diff projects, might be better to target the divs/container that contain all the info about the hack. If there is a class for this, then that's even better

