import unittest

from word_ladder import *


class MyTestCase(unittest.TestCase):
    def test_get_word_buckets(self):
        test_buckets = get_word_buckets("test_vocabulary.txt")
        labels = list(test_buckets.keys())
        for label in labels:
            self.assertTrue(label in ['_an', '_ar', 'c_n', 'c_r', 'ca_', 'v_n', 'va_'])

    def test_add_vertices_edges(self):
        test_buckets = get_word_buckets("test_vocabulary.txt")
        graph = add_vertices_edges(test_buckets)
        for word in list(graph.get_vertices()):
            self.assertTrue(word in ['can', 'van', 'car'])


if __name__ == '__main__':
    unittest.main()
