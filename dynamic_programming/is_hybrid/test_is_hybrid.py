from unittest import TestCase
from is_hybrid import is_hybrid


class TestIsHybrid(TestCase):
    def test_is_hybrid(self):
        x = "hello"
        y = "goodbye"
        z = "hgoeoldlboye"

        result = is_hybrid(x, y, z)
        print(result)

