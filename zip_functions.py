import zipcode
import re
import requests

def local_city_list_maker(starting_zip='98119', mile_radius=100):
    """returns list of cities within radius of starting zip"""
    city_list = []
    zip_obj = zipcode.isequal(starting_zip)
    local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), mile_radius)
    for i in local_zips:
        state_city = i.state + ' ' + i.city
        if state_city not in city_list:
            city_list.append(state_city)
    return city_list


def weather_station_code_finder(city_list=local_city_list_maker()):
    """returns list of weather station ICAO codes
    city_list: list of states and cities * needs to be in 'ST CITY' format
               use return from local_city_list_maker()
    """
    city_code_list = []
    code_db = open('weather_codes.txt', 'r').read()
    for city in city_list:
        city_info = re.search(city + '.*[PKXQ]\w{3}\s\s', code_db)
        try:
            code = re.search('\s[PKXQ]\w{3}\s\s', city_info.group())
            #city_code_list.append((city, code.group()))
            city_code_list.append((code.group()).strip())
        except:
            pass
    return city_code_list


print(weather_station_code_finder(['OK MUSKOGEE'])[0])

# #starting to get weather data. need to make mock produce data for cross reference
# codes = weather_station_code_finder()
# for i in codes:
#     #print(i)
#     r = requests.get('https://www.wunderground.com/history/airport/{}/2016/4/0/MonthlyHistory.html?format=1'.format(i))
#     print(r.text)
# #
# # r = requests.get('https://www.wunderground.com/history/airport/{}/2016/4/0/MonthlyHistory.html?format=1'.format('KSEA'))
# # print(r.text)