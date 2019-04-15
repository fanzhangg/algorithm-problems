from unittest import TestCase
from get_closest_location_pair import get_location_pair_names, get_chigago_location_pair_names


class TestGetLocationPairNames(TestCase):
    def test_minnesotaLocations(self):
        names = get_location_pair_names("minnesotaLocations.csv")
        self.assertEqual(('Clara City Police Department', 'Clara City Fire Department'), names)

    def test_chicagoLocations(self):
        names = get_chigago_location_pair_names("chicagoLocations.csv")
        self.assertEqual(('Rolling Meadows Police Department', 'Palatine Townhall'), names)

    def test_wordOfAvatar(self):
        names = get_location_pair_names("worldOfAvatar.csv")
        self.assertEqual(('Shu', 'Hokage'), names)

