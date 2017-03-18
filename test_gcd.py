from unittest import TestCase
from euler import gcd


class TestGcd(TestCase):
    def test_gcd(self):
        r = gcd(9,4)
        self.assertEqual(1,r)

    def test_gcd2(self):
        r = gcd(461952, 116298)
        self.assertEqual(18, r)
