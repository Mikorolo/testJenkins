import unittest
from app import *

class TestArytmetyki(unittest.TestCase):
    def test_dodawanie(self):
        self.assertEqual(dodaj(3, 5), 8)

    def test_odejmowanie(self):
        self.assertEqual(odejmij(10, 4), 6)

    def test_mnozenie(self):
        self.assertEqual(pomnoz(2, 3), 6)

    def test_dzielenie(self):
        self.assertEqual(podziel(10, 2), 5)
        self.assertEqual(podziel(10, 5), 2)
        with self.assertRaises(ValueError):
            podziel(10, 0)

if __name__ == '__main__':
    unittest.main()
