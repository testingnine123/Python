#use http://python-data.dr-chuck.net/comments_42.json to test. Sum should be 2482.
#can also use http://python-data.dr-chuck.net/comments_171700.json to test. Sum...
#...should end with 81.

import json
import urllib

sum = 0

url = raw_input("Enter location (url):")

#"data" type would be a string
try : data = urllib.urlopen(url).read()
except : data
	print "Improper url. Exiting...."
	exit()

print "Retrieving", url
print "Retrieved", len(data), "character"

#"jsonData" type would be a dictionary
jsonData = json.loads(data)

#print the number of nodes of "comments" tag
print "Count:",len(jsonData["comments"])

#the "count" tag is under the comments tag
for items in jsonData["comments"]:
	sum = sum + int(items["count"])

print "Sum:",sum