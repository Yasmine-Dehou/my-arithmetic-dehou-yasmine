import unittest
from src.my_arithmetic_dehou_yasmine.pgcd import pgcd

class TestPGCD(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        self.assertEqual(pgcd(48, 18), 6)

    def test_gcd_with_zero(self):
        self.assertEqual(pgcd(0, 18), 18)
        self.assertEqual(pgcd(48, 0), 48)

    def test_gcd_same_numbers(self):
        self.assertEqual(pgcd(25, 25), 25)

    def test_gcd_one_and_number(self):
        self.assertEqual(pgcd(1, 18), 1)

    def test_gcd_negative_numbers(self):
        self.assertEqual(pgcd(-48, -18), -6)

    def test_gcd_negative_and_positive_numbers(self):
        self.assertEqual(pgcd(-48, 18), 6)
        self.assertEqual(pgcd(48, -18), 6)