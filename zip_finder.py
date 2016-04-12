import zipcode
import re

my_zip = zipcode.isequal('98119')
local_zips = zipcode.isinradius((my_zip.lat, my_zip.lon), 100)



zip_dict = {}

## good code!!!
for i in local_zips:
    state_city = i.state + ' ' + i.city
    if state_city not in zip_dict:
        zip_dict[state_city] = [i.zip]
    zip_dict[state_city].append(i.zip)
## good code!!!




print(zip_dict)

code_db = open('weather_codes.txt', 'r').read()

for i in zip_dict:
    #m = re.search('{}.+'.format(i), code_db)

    m = re.search(i + '.*[PKXQ]\w{3}\s\s', code_db)

    #cm = re.search('^[PKXQ]{4}', m.group)
    # m = re.findall(i +'\s^[PKXQ]{4}', code_db)
    try:
        print(m.group())
        cm = re.search('\s[PKXQ]\w{3}\s\s', m.group())
        print(cm.group())
    # print(m.groups())
    except:
        pass