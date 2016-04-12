import unittest

from zip_functions import local_city_list_maker, weather_station_code_finder


class ZipFunTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_weather_station_code_finder(self):
        self.assertEqual((weather_station_code_finder(['OK MUSKOGEE'])[0][1]).strip(), 'KMKO')

    def test_local_city_list_maker(self):
        self.assertNotIn('NY MEDUSA', local_city_list_maker())
        self.assertIn('NY HUDSON', local_city_list_maker('12120'))

