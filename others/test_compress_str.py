from unittest import TestCase
from compress_string import compress_str


class TestCompressStr(TestCase):
    def test_compress_str(self):
        self.assertEqual(compress_str("AAAAaaBCCCDDe"), "A4a2B1C3D2e1")
