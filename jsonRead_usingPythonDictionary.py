#module to read json data
import json

#a curly bracket indicates that it is a dictionary
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

#load data into a dictionary named "info"
info = json.loads(data)

#print data of the dictionary (key-value pairs)
print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]