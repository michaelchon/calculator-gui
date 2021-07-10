import unittest
from .number_formatter import formatter


class TestNumberFormatter(unittest.TestCase):
    def test_format(self):
        self.assertEqual(formatter.format('9999999.9'), '9 999 999,9')
        self.assertEqual(formatter.format('9999999.90'), '9 999 999,9')
        self.assertEqual(formatter.format('9999999.'), '9 999 999')
        self.assertEqual(formatter.format('9999999'), '9 999 999')


if __name__ == '__main__':
    unittest.main()
