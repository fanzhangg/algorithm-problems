import unittest
from goodfellas import *


class PersonTest(unittest.TestCase):
    def test_other_is_good(self):
        good = Person(True, 1)
        bad = Person(False, 2)
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
            good_gang.append(Person(True, i))
        p = find_single_good(good_gang)
        print(p)
        self.assertTrue(bool(p))

    def test_random_cases(self):
        # create a random list such as more good than bad
        for _ in range(1000):
            gang = list()
            for i in range(200):
                gang.append(Person(True, i))
            for i in range(100):
                gang.append(Person(False, i))
            random.shuffle(gang)
            p = find_single_good(gang)
            self.assertTrue(bool(p))


class IdentifyAllPeopleTest(unittest.TestCase):
    def test_all_good(self):
        people = []
        for i in range(10):
            people.append(Person(True, i))

        people_copy = people.copy()
        good = find_single_good(people)
        result = identify_all_people(good, people_copy)
        self.assertEqual([True] * 10, result)

    def test_random_cases(self):
        for _ in range(1000):
            gang = list()
            for i in range(20):
                gang.append(Person(True, i))
            for i in range(10):
                gang.append(Person(False, i))
            random.shuffle(gang)
            initial_gang = gang.copy()
            good = find_single_good(gang)
            result = identify_all_people(good, initial_gang)
            for i in range(len(gang)):
                self.assertEqual(initial_gang[i].is_good, result[i])


if __name__ == '__main__':
    unittest.main()
