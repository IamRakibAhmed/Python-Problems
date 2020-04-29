import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
if api_key is False:
    api_key = 42
    serviceURL = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceURL = 'http://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter Location: ")
    if len(address) < 1:
        break

    parmission = dict()
    parmission['address'] = address
    if api_key is not False:
        parmission['key'] = api_key
    url = serviceURL + urllib.parse.urlencode(parmission)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failed to Retrieved !')
        print(data)
        continue

    location = js['results'][0]['formatted_address']
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    print('Address:', location)
    print('Lat:', lat)
    print('Lng', lng)
