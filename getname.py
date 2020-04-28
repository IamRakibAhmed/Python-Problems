import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL: ')
p = input('Enter the position: ')
c = input('Enter count: ')

position = int(p)
count = int(c)

for line in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    a = []
    b = []

    for tag in tags:
        x = tag.get('href', None)
        a.append(x)
        y = tag.text
        b.append(y)

    url = a[position - 1]
    print(a[position - 1])
    print(b[position - 1])
