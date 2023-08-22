import unittest
import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(even_or_odd.is_even(1), False)

    def test_bad_input(self):
        self.assertRaises(TypeError, even_or_odd.is_even, 'a', False)

if __name__ == '__main__':
    unittest.main()
