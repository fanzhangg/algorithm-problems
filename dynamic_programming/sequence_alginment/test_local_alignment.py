from unittest import TestCase
from local_sequence_alignment import *


class TestLocalAlignment(TestCase):
    def test_local_alignment(self):
        s2 = "TGTTACGG"
        s1 = "GGTTGACTA"
        max_score = local_alignment(s1, s2, 2)
        print(max_score)
