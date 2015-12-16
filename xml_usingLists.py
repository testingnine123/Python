#import the module to process XML in python
import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

#read the XML data
stuff = ET.fromstring(input)
#create a list of all users, which will include user, id, etc.
lst = stuff.findall('users/user')

#print total users found in the XML data.
print 'User count:', len(lst)

#parse the list and find out the data needed.
for item in lst:
    #serach and print the name of the users (name tag)
    print 'Name', item.find('name').text
    #search and print the id of the users (id tag)
    print 'Id', item.find('id').text
    #serach and print the attribute of the users (x's value)
    print 'Attribute', item.get("x")