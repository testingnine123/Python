import urllib
#BeautifulSoup library is used to screen-scraping data from websites
#from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input('Enter web address:')
html = urllib.urlopen(url).read()
#make use of the BeautifulSoup library to parse the HTML data we get back
soup = BeautifulSoup(html,"html.parser")

#retieve anchor tags only and print the value after the 'href' string
#tags will be a list
tags = soup('a')

#print all in the list tags. Default is None in case there are no tags
for tag in tags:
	print tag.get('href', None)
