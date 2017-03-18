from unittest import TestCase
from euler import ispandigital10
from pandigitals import ispandigital

class TestIspandigital(TestCase):
    def test_ispandigital(self):
        ispan = ispandigital(923456781)
        self.assertTrue(ispan)

    def test_ispandigital10(self):
        ispan = ispandigital10('9203456781')
        self.assertTrue(ispan)
