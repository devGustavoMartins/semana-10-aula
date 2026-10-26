import unittest

from numeroromano import converte


class TestConverteNumeroRomano(unittest.TestCase):
    def test_I(self):
        self.assertEqual(converte('I'), 1)

    def test_V(self):
        self.assertEqual(converte('V'), 5)

    def test_II(self):
        self.assertEqual(converte('II'), 2)

    def test_XXII(self):
        self.assertEqual(converte('XXII'), 22)

    def test_IX(self):
        self.assertEqual(converte('IX'), 9)

    def test_XXIV(self):
        self.assertEqual(converte('XXIV'), 24)

    def test_M(self):
        self.assertEqual(converte('M'), 1000)

    def test_XIII(self):
        self.assertEqual(converte('XIII'), 13)

    def test_MMXXVI(self):
        self.assertEqual(converte('MMXXVI'), 2026)


if __name__ == '__main__':
    unittest.main()
