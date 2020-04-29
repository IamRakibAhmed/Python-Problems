import json

data = '''[
{"id" : "001", "x" : "2", "name" : "Rakib"},
{"id" : "009", "x" : "7", "name" : "Janina"}
]'''

tree = json.loads(data)
print('Total item(s):', len(tree))

for items in tree:
    print('Name:', items["name"])
    print('ID:', items["id"])
    print('Attribute:', items["x"])
