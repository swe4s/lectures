import unittest
import math_lib

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

        self.assertRaises(ZeroDivisionError, math_lib.div, 10, 0)

        with self.assertRaises(ZeroDivisionError):
            math_lib.div(10, 0)

    def test_file_add_no_setup(self):

        import random

        test_file_name = 'test_file.txt'
        f = open(test_file_name, 'w')

        direct_sum = 0

        for i in range(100):
            rand_int = random.randint(1,100)
            direct_sum += rand_int
            f.write(str(rand_int) + '\n')
        f.close()

        file_sum = math_lib.file_add(test_file_name)
        
        self.assertEqual(file_sum, direct_sum)

        import os

        os.remove(test_file_name)


    def test_file_prod_no_setup(self):
        import random

        test_file_name = 'test_file.txt'
        f = open(test_file_name, 'w')

        direct_prod = 1

        for i in range(100):
            rand_int = random.randint(1,100)
            direct_prod *= rand_int
            f.write(str(rand_int) + '\n')
        f.close()

        file_prod = math_lib.file_prod(test_file_name)
        
        self.assertEqual(file_prod, direct_prod)


    def setUp(self):
        import random

        self.test_file_name = 'setup_test_file.txt'
        f = open(self.test_file_name, 'w')

        self.direct_sum = 0
        self.direct_prod = 1

        for i in range(100):
            rand_int = random.randint(1,100)
            self.direct_prod *= rand_int
            self.direct_sum += rand_int
            f.write(str(rand_int) + '\n')
        f.close()

    def tearDown(self):
        import os
        os.remove(self.test_file_name)

    def test_file_add_setup(self):
        file_sum = math_lib.file_add(self.test_file_name)
        
        self.assertEqual(file_sum, self.direct_sum)

    def test_file_prod_setup(self):
        file_prod = math_lib.file_prod(self.test_file_name)
        self.assertEqual(file_prod, self.direct_prod)


if __name__ == '__main__':
    unittest.main()
