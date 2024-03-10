import unittest
from app import dodaj

class TestDodaj(unittest.TestCase):

    def test_dodaj(self):
        self.assertEqual(dodaj(3, 5), 8)
        self.assertEqual(dodaj(-1, 1), 0)
        self.assertEqual(dodaj(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
