from unittest import TestCase
from quadraticprimes import primeList, quadratic
from euler import isprime

class TestPrimeList(TestCase):
    def test_primeList(self):
        list = []
        for n in self.yieldList():
            if not primeList(list,n):
                break
        self.assertEqual(2,len(list))

    def yieldList(self):
        list = [3,5,6]
        for n in list:
            yield n

    def test_quadratic(self):
        self.assertTrue(isprime(quadratic(1,0,1)))