from unittest import TestCase
from is_hybrid import is_hybrid


class TestIsHybrid(TestCase):
    def test_is_hybrid(self):
        x = "hello"
        y = "goodbye"
        z = "hgoeoldlboye"

        self.assertTrue(is_hybrid(x, y, z))

        x = "python"
        y = "java"
        z = "pyjathvona"

        self.assertTrue(is_hybrid(x, y, z))

    def test_len_neq(self):
        self.assertFalse(is_hybrid("helllo", "goodby", "hello"))

    def test_false_case(self):
        self.assertFalse(is_hybrid("hello", "world", "hewrolllod"))
