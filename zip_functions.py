import zipcode
import re


# def zip_code_finder(starting_zip='98119', mile_radius=100):
#     """returns dict of zipcodes within radius of starting zip"""
#     zip_dict = {}
#     zip_obj = zipcode.isequal(starting_zip)
#     local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), mile_radius)
#     for i in local_zips:
#         state_city = i.state + ' ' + i.city
#         if state_city not in zip_dict:
#             zip_dict[state_city] = [i.zip]
#         zip_dict[state_city].append(i.zip)
#     return zip_dict
#
#
# print(zip_code_finder())



def local_city_list_maker(starting_zip='98119', mile_radius=100):
    """returns list of cities within radius of starting zip"""
    city_code_list = []
    zip_obj = zipcode.isequal(starting_zip)
    local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), mile_radius)
    for i in local_zips:
        state_city = i.state + ' ' + i.city
        if state_city not in city_code_list:
            city_code_list.append(state_city)
    return city_code_list

print(local_city_list_maker())


def 