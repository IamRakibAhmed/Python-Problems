import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter the URL: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_469097.json'

print('Retrieving', url)
data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

tree = json.loads(data)
print(tree)
s = 0
c = 0

for item in tree['comments']:
    c = c + 1
    countval = int(item['count'])
    s = s + countval

print('Count:', c)
print('Sum:', s)
