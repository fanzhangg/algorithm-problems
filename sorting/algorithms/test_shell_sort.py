from unittest import TestCase
from shell_sort import *


class TestShellSort(TestCase):
    def test_shell_sort(self):
        l = [1, 5, 2, 3, 4]
        shell_sort(l)
        self.assertEqual([1, 2, 3, 4, 5], l)
