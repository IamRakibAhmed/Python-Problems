import re
x = input("Enter file name: ")
inp = open("file.txt")

lst = list()
for line in inp:
    num = re.findall('[0-9]+', line)
    lst = lst + num

s = 0
for it in lst:
    s = s + int(it)

print(s)
