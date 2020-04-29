import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter the URL: ")
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_469096.xml'

print('Retrieving', url)
xml = urllib.request.urlopen(url).read()
print('Recieved', len(xml), 'characters')

tree = ET.fromstring(xml)
count = tree.findall('.//count')
print('Count:', len(count))
s = 0

for i in count:
    s = s + int(i.text)

print('Sum:', s)
