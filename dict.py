name = input("Enter file:")
if len(name) < 1:
    name = "file.txt"

handle = open(name)

words = list()
for line in handle:
    if line.startswith('From '):
        line = line.split()
        words.append(line[1])

counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

maxVal = None
maxKey = None

for key, val in counts.items():
    if maxVal is None or val > maxVal:
        maxVal = val
        maxKey = key

print(maxKey, maxVal)
