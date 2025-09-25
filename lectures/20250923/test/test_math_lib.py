import sys
import unittest

sys.path.append('src/') # noqa

import math_lib
import random

print(sys.path)

class TestMathLib(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_lib.add(10, 5), 15)
        self.assertEqual(math_lib.add(-1, 1), 0)
        self.assertEqual(math_lib.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(math_lib.sub(10, 5), 5)
        self.assertEqual(math_lib.sub(-1, 1), -2)
        self.assertEqual(math_lib.sub(-1, -1), 0)

    def test_prod(self):
        self.assertEqual(math_lib.prod(10, 5), 50)
        self.assertEqual(math_lib.prod(-1, 1), -1)
        self.assertEqual(math_lib.prod(-1, -1), 1)

    def test_div(self):
        self.assertEqual(math_lib.div(10, 5), 2)
        self.assertEqual(math_lib.div(-1, 1), -1)
        self.assertEqual(math_lib.div(-1, -1), 1)
        self.assertEqual(math_lib.div(5, 2), 2.5)


        for i in range(1000):
            a = random.randint(1,10000)
            b = random.randint(10001, 20000)
            self.assertTrue(math_lib.div(b, a) > 1)
            self.assertTrue(math_lib.div(a, b) < 1)
            self.assertEqual(math_lib.div(a, b) , a/b)
        

        self.assertRaises(ZeroDivisionError, math_lib.div, 10, 0)
        #with self.assertRaises(ValueError):
            #math_lib.div(10, 0)

if __name__ == '__main__':
    unittest.main()

