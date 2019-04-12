import unittest
from goodfellas import *


class PersonTest(unittest.TestCase):
    def test_other_is_good(self):
        good = Person(True)
        bad = Person(False)
        self.assertTrue(good.other_is_good(good))
        self.assertFalse(good.other_is_good(bad))
        for _ in range(10):
            print("Bad says a good:", bad.other_is_good(good))

        for _ in range(10):
            print("Bad says a bad:", bad.other_is_good(bad))


class FindSingleGoodTest(unittest.TestCase):
    def test_all_good(self):
        good_gang = []
        for i in range(10):
            good_gang.append(Person(True))
        p = find_single_good(good_gang)
        self.assertTrue(bool(p))

    def test_random_cases(self):
        # create a random list such as more good than bad
        for _ in range(1000):
            gang = list()
            for i in range(200):
                gang.append(Person(True))
            for i in range(100):
                gang.append(Person(False))
            random.shuffle(gang)

            self.assertTrue(bool(find_single_good(gang)))


if __name__ == '__main__':
    unittest.main()
