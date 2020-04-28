import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()

for line in fhand:
    word = line.decode().split()
    for c in word:
        count[c] = count.get(c, 0) + 1

print(count)
