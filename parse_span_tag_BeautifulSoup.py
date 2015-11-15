import urllib
from BeautifulSoup import *

score = 0

url = raw_input('Enter web address:')
#can use "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html" or "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_171699.html". Answer for the first file is 2553 and for the second one is 2200

#read the file
html = urllib.urlopen(url).read()
#soup up the html text
soup = BeautifulSoup(html)

#create list of span tags
tags = soup('span')

for tag in tags:
	score = score + int(tag.contents[0])

print 'Sum:', score


