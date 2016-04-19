import zipcode
import pprint
import csv


def local_zipcodes(startingzip='98119', radius=100):
    """ Returns zipcodes within radius of startingzip"""
    zip_obj = zipcode.isequal(startingzip)
    local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), radius)
    return {i.zip for i in local_zips}


def local_info(zipcodes=local_zipcodes()):
    """ Returns city, tate, grow zone and airport code (if applicable) of zipcode(s) """
    with open('data_files/alldata.csv', 'r') as f:
        reader = csv.reader(f)
        return [row for row in reader if row[0] in zipcodes]



pprint.pprint(local_info())