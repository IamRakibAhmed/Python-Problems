import xml.etree.ElementTree as ET

data = '''
<person>
<name> Rakib </name>
<phone type = 'intl'> +8801300000000 </phone>
<email hide = 'yes'/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone type:', tree.find('phone').get('type'))
print('Phone number:', tree.find('phone').text)
print('Email:', tree.find('email').get('hide'))
