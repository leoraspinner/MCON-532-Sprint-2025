import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_basic_palindromes(self):
        palindromes = ["madam", "eve", "bob", "33"]
        for word in palindromes:
            with self.subTest(word=word):
                self.assertTrue(is_palindrome(word))

    def test_non_palindromes(self):
        non_palindromes = ["owl", "case", "teacher"]
        for word in non_palindromes:
            with self.subTest(word=word):
                self.assertFalse(is_palindrome(word))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("Race a car"))

    def test_special_characters(self):
        self.assertTrue(is_palindrome("Madam, I'm Adam"))
        self.assertTrue(is_palindrome("A Santa at NASA"))
        self.assertFalse(is_palindrome("not a palindrome!"))

if __name__ == "__main__":
    unittest.main()
