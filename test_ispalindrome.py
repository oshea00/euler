from unittest import TestCase
from euler import ispalindrome

class TestIspalindrome(TestCase):
    def test_ispalindromeSingleDigit(self):
        self.assertTrue(ispalindrome(0))
        self.assertTrue(ispalindrome(1))
        self.assertTrue(ispalindrome(2))
        self.assertTrue(ispalindrome(3))
        self.assertTrue(ispalindrome(4))
        self.assertTrue(ispalindrome(5))
        self.assertTrue(ispalindrome(6))
        self.assertTrue(ispalindrome(7))
        self.assertTrue(ispalindrome(8))
        self.assertTrue(ispalindrome(9))
        self.assertFalse(ispalindrome(10))
        self.assertFalse(ispalindrome('01101'))
        self.assertFalse(ispalindrome('1110'))
        self.assertTrue(ispalindrome('31313'))
        self.assertTrue(ispalindrome('0110'))
        self.assertTrue(ispalindrome('010'))
        self.assertTrue(ispalindrome('11'))
        self.assertTrue(ispalindrome('121'))

