import urllib2
from re import findall

#ref=more value goes from p1 to p52, but I'm only getting p1 regardless
# of what value is there
url = 'http://www.kickstarter.com/discover/categories/film%20&%20video/popular?ref=more#p1'

#scrape the html
response = urllib2.urlopen(url)
html = response.read()
text = str(html)

#pull out the links
dataCrop = findall("\"https://www\.kickstarter\.com/projects/[\w\-/?=]*\"", text)
links = set(dataCrop)	#remove duplicates

#save links in file
file = open('kickstarterProjectLinks.txt', 'w')
for link in links:
	file.write(link + "\n")
file.close()