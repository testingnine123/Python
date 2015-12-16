#module to read XML data. "ET" is being used as the shortform for the name of...
#...the module.
import xml.etree.ElementTree as ET

#sample data as below. Use tripple single quotes to define the data.
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

#use the ET module and the functions insid it
tree = ET.fromstring(data)

#find the "name" tag and print its text using tree.find()
print 'Name:',tree.find('name').text
#find the email tag and print the text of the "hide" attribute
print 'Attr:',tree.find('email').get('hide')