import unittest
from palindrome_checker import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_palindrome(self):
        s = "madam"
        self.assertTrue(is_palindrome(s))

        s = "helleh"
        self.assertTrue(is_palindrome(s))

    def test_non_palindrome(self):
        s = "yahoo"
        self.assertFalse(is_palindrome(s))

if __name__ == "__main__":
    unittest.main()
