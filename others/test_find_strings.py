from unittest import TestCase
from find_strings import find_strings


class TestFindStrings(TestCase):
    def test_find_strings(self):
        self.assertEqual(find_strings(["hello", "is", "anybody", "here"], "h"), ["hello", "here"])
