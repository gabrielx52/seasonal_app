import zipcode
import re


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


def weather_station_code_finder(city_list):
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
            city_code_list.append((city, code.group()))
        except:
            pass
    print(city_code_list)

weather_station_code_finder(local_city_list_maker())