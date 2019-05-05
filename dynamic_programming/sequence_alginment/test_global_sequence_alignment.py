from unittest import TestCase
import string
from global_sequence_alignment import alignment


class TestAlignment(TestCase):
    @staticmethod
    def get_mismatch_costs():
        costs = {}
        vowels = "aeiou"
        consonants = [l for l in string.ascii_lowercase if l not in vowels]

        for a in string.ascii_lowercase:
            for b in string.ascii_lowercase:
                if a == b:
                    costs[a, b] = 0
                elif (a in vowels and b in consonants) or (a in consonants and b in vowels):
                    costs[a, b] = 2
                else:
                    costs[a, b] = 1
        return costs

    def test_alignment(self):
        mismatch_costs = self.get_mismatch_costs()
        print(mismatch_costs)
        result = alignment("name", "nail", 2, self.get_mismatch_costs())
        self.assertEqual((4, 'name', 'nail'), result)
        result2 = alignment("elephant", "telephone", 2, self.get_mismatch_costs())
        self.assertEqual((5, '-elephant', 'telephone'), result2)
