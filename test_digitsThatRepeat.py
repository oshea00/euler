from unittest import TestCase
from reciprocal import digitsThatRepeat, allTheSame, \
    repeatsAfterN, digitsInQuotient

class TestDigitsThatRepeat(TestCase):
    def test_allTheSame(self):
        self.assertEqual(allTheSame('11'), '1')

    def test_repeatsAfterN(self):
        self.assertEqual(repeatsAfterN(2, '99321321'), ('99', '321'))

    def test_repeatsAfterN1(self):
        self.assertEqual(repeatsAfterN(1, '500'), ('500', False))

    def test_digitsInQuotient(self):
        self.assertEqual((digitsInQuotient(1,19,4)), '0526')

    def test_digitsInQuotient1(self):
        self.assertEqual((digitsInQuotient(1, 4, 4)), '25')

    def test_tenthousand(self):
        self.assertEqual(len((digitsInQuotient(1, 499, 10000))), 10001)





