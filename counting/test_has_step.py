from unittest import TestCase
from counting.count_num_with_no_step import has_step


class TestHasStep(TestCase):
    def test_is_num_with_step(self):
        self.assertTrue(has_step((1, 2, 3, 4, 5)))
        self.assertFalse(has_step((5, 4, 3, 2, 1)))
        self.assertTrue(has_step((5, 2, 3, 4, 1)))
