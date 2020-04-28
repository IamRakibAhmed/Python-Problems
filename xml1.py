import xml.etree.ElementTree as ET

data = '''
<students>
    <users>
        <user x = '2'>
            <id> 001 </id>
            <name> Rakib Ahmed </name>
        </user>
        <user x = '7'>
            <id> 002 </id>
            <name> Imaginary Person </name>
        </user>
    </users>
</students>'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print('Total Users:', len(lst))

for items in lst:
    print('Name:', items.find('name').text)
    print('ID:', items.find('id').text)
    print('Attribute:', items.get('x'))
    print('\n')
