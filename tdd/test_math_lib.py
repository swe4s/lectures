import unittest
import math_lib
import statistics
import random
import math
import os

class TestMathLib(unittest.TestCase):
    def test_list_mean_for_empty_list(self):
        r = math_lib.list_mean([])
        self.assertEqual(r, None)

    def test_list_mean_for_None_list(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)

    def test_list_mean_constants(self):
        r = math_lib.list_mean( [1,1,1,1,1,1,1] )
        self.assertEqual(r, 1)

    def test_list_mean_rand_ints(self):
        L = []

        for i in range(10):
            L.append(random.randint(0,100))

        r = math_lib.list_mean( L )
        self.assertEqual(r, statistics.mean(L))

    def test_list_mean_non_int_in_list(self):
        L = []

        for i in range(10):
            L.append(random.randint(0,100))

        L.append('X')

        self.assertRaises(ValueError, math_lib.list_mean, L)

    def test_list_mean_non_int_in_list_good_msg(self):
        L = []

        for i in range(10):
            L.append(random.randint(0,100))

        L.append('X')

        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean(L)

        self.assertEqual(str(ex.exception), 
                         'Cannot find mean. Unsupported value in list.')

    def test_list_mean_rand_floats(self):
        L = []

        for i in range(10):
            L.append(random.uniform(0,100))

        r = math_lib.list_mean( L )
        self.assertTrue(math.isclose(r, statistics.mean(L)))


    def test_list_mean_zero(self):
        r = math_lib.list_mean( [0] )
        self.assertEqual(r, 0)


    def test_list_mean_rand_ints_and_floats(self):
        L = []

        for i in range(10):
            L.append(random.uniform(0,100))
            L.append(random.randint(0,100))

        r = math_lib.list_mean( L )
        self.assertTrue(math.isclose(r, statistics.mean(L)))


    def test_list_mean_many_rand_ints_and_floats(self):
        for i in range(1000):
            L = []

            for i in range(10):
                L.append(random.uniform(0,100))
                L.append(random.randint(0,100))

            r = math_lib.list_mean( L )
            self.assertTrue(math.isclose(r, statistics.mean(L)))


    def test_read_file_col_no_file(self):
        file_name = 'no_file.csv'
        
        with self.assertRaises(FileNotFoundError) as ex:
            L = math_lib.read_file_col(file_name, 0)

    def test_read_file_col_no_file_good_msg(self):
        file_name = 'no_file.csv'
        
        with self.assertRaises(FileNotFoundError) as ex:
            L = math_lib.read_file_col(file_name, 0)

        self.assertEqual(str(ex.exception), 
                         file_name + ' not found.')

    def test_read_file_col_empty_file(self):
        file_name = 'empty.csv'
        f = open(file_name, 'w')
        f.close()

        L = math_lib.read_file_col(file_name, 0)

        self.assertEqual(L, None)

    def test_read_file_col_constant(self):
        file_name = 'constant.csv'
        f = open(file_name, 'w')
        f.write('1\n1\n1\n1')
        f.close()

        L = math_lib.read_file_col(file_name, 0)

        self.assertEqual(L, [1,1,1,1])

    def test_read_file_col_2nd_col_constant(self):
        file_name = 'constant.csv'
        f = open(file_name, 'w')
        f.write('1,2\n1,2\n1,2\n1,2')
        f.close()

        L = math_lib.read_file_col(file_name, 1)

        self.assertEqual(L, [2,2,2,2])

    def test_read_file_col_no_col_in_file(self):
        file_name = 'constant.csv'
        f = open(file_name, 'w')
        f.write('1,2\n1,2\n1,2\n1,2')
        f.close()

        L = math_lib.read_file_col(file_name, 3)
        self.assertEqual(L, None)



if __name__ == '__main__':
    unittest.main()
