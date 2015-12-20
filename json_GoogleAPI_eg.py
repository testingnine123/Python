#use "South Federal Boulevard" for testing. Place_id should be...
#...ChIJJ8oO7_B_bIcR2AlhC8nKlok

import urllib
import json

#base url of the API is serviceurl

#use this for Dr. Chuck's API
#serviceurl = 'http://python-data.dr-chuck.net/geojson?'

#use this for Google's API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

place = raw_input('Enter location:')

if len(place) < 1 : exit()

url = serviceurl + urllib.urlencode({'sensor':'false', 'address':place})

print 'Retrieving',url

data = urllib.urlopen(url).read()

print "Retrieved",len(data),'characters'

#type of "jsonData" is dictionary
try : jsonData = json.loads(data)
except:
	print "Not found!"
	exit()
	
#serach place_id in the json, and print it
print jsonData["results"][0]["place_id"]