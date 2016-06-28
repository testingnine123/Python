#Can use http://python-data.dr-chuck.net/comments_42.xml...
#...for testing. Sum should be 2482

#module for reading urls
import urllib
#module for processing XML data
import xml.etree.ElementTree as ET

lst = list()

#run the code till the user doesn't enter a url
while True:
	sum = 0
	url = raw_input('Enter location: ')
	if len(url) < 1 : break

	print 'Retrieving',url
	
	#open the url and read the data
	data = urllib.urlopen(url).read()
	
	print 'Retrived',len(data),'characters'

	#process the XML file
	tree = ET.fromstring(data)

	#make a list of all the "count" tags stored under the "comment" tag
	counts = tree.findall('.//comment')

	print 'Count:',len(counts)

	#run a loop to sum all the values of the count tage
	for item in counts:
		sum = sum + int(item.find('count').text)
	
	print 'Sum:',sum
