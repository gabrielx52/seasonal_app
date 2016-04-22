import zipcode
import requests
import pprint
import re


def local_city_grabber(starting_zip='98119', mile_radius=100):
    """returns dict of zipcodes within radius of starting zip"""
    cities = {}
    zip_obj = zipcode.isequal(starting_zip)
    local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), mile_radius)
    for i in local_zips:
        state_city = i.state + ' ' + i.city
        if state_city not in cities:
            cities[state_city] = {'zip': i.zip}
    return cities


def weather_station_code_grabber(cities=local_city_grabber()):
    """returns list of weather station ICAO codes
    city_list: list of states and cities * needs to be in 'ST CITY' format
               use return from local_city_list_maker()
    """
    compiled_cities = {}
    with open('weather_codes.txt', 'r') as text:
        code_db = text.read()
    for city in cities:
        city_info = re.search(city + '.*[PKXQ]\w{3}\s\s', code_db)
        try:
            cities[city]['code'] = re.search('\s[PKXQ]\w{3}\s\s', city_info.group()).group().strip()
            compiled_cities[city] = cities[city]
        except:
            pass
    return compiled_cities


def plant_hardiness_zone(cities=weather_station_code_grabber()):
    """Adds plant hardiness zone to cities in dict"""
    root_site = 'https://shop.arborday.org/LookUp.aspx?zipcode='
    for city in cities:
        l = root_site + '{}'.format(cities[city]['zip'])
        r = requests.get(root_site + '{}'.format(cities[city]['zip']))
        zone = re.search('\s\d\-*\d*',re.search('Zones?\s\d+\-*\d*', r.text).group())
        if zone:
            cities[city]['zone'] = zone.group().strip()
    return cities

pprint.pprint(plant_hardiness_zone())
