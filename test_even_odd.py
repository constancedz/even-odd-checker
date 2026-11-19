import unittest
from even_odd import check_even_odd


class CheckEvenOddTests(unittest.TestCase):
    def test_even(self):
        self.assertEqual(check_even_odd(4), "4 is Even")

    def test_odd(self):
        self.assertEqual(check_even_odd(7), "7 is Odd")

    def test_zero_and_negative(self):
        self.assertEqual(check_even_odd(0), "0 is Even")
        self.assertEqual(check_even_odd(-3), "-3 is Odd")

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            check_even_odd("4")


if __name__ == "__main__":
    unittest.main()
