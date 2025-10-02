import unittest
import file_lib

# A general get_data function that retrieves rows from a data file with the
# option of providing a query value and query column to only return rows where
# the string at that column matches the value. Also optionally retrieve the
# header.

# Test if get_data retrieves rows from a data file 
class TestFileLib(unittest.TestCase):
    def test_get_data_basic_rows(self):
        file_path = 'test_data.csv' 

        data = file_lib.get_data(file_path) # returns list of lists, each sublist is a row

        expect_data = [['Afghanistan', '1990', '14.7237', '0.0557' ,'205.6077'],
                       ['Afghanistan', '1991', '14.7237', '0.0557' ,'209.4971'],
                       ['Afghanistan', '1992', '14.7237', '0.0557' ,'196.5341'],
                       ['Afghanistan', '1993', '14.7237', '0.0557' ,'230.8175'],
                       ['Afghanistan', '1994', '14.7237', '0.0557' ,'242.0494'],
                       ['Afghanistan', '1995', '14.7237', '0.0557' ,'243.8152'],
                       ['Afghanistan', '1996', '38.9302', '0.2014' ,'249.0364'],
                       ['Algeria', '2020', '41.1136', '107.1825','361.0129']]

        self.assertEqual(data, expect_data)

        file_path = 'test_data_imf.csv' 

        data = file_lib.get_data(file_path) # returns list of lists, each sublist is a row

        expect_data = [ ["Afghanistan, Islamic Rep. of", None, None, None, None, None, None, None, None, None],
                        ["Albania", None, None, None, None, None, None, None, None, None],
                        ["Algeria", None, None, "11,745.49", "18,835.02", "20,301.93", "22,391.65", "21,871.29", "24,554.12", "28,321.51"],
                        ["Andorra, Principality of", None, None, None, None, None, None, None, None, None],
                        ["Angola", None, None, None, None, None, None, None, None, None],
                        ["Anguilla", None, None, None, None, None, None, None, None, None],
                        ["Antigua and Barbuda", None, None, None, "4.75", "7.25", "6.86", "8.86", "10.9", "13.3"],
                        ["Argentina", None, None, None, None, None, None, None, None, None],
                        ["Armenia, Rep. of", None, None, None, None, None, None, None, None, None],
                        ["Aruba, Kingdom of the Netherlands", None, None, None, None, None, None, None, None, None],
                        ["Australia", "17,317.00", "17,477.00", "18,555.00", "20,254.00", "22,242.00", "23,912.00", "25,585.00", "28,321.00", "30,898.00"],
                        ["Austria", None, None, None, None, None, None, None, None, None],
                        ["Azerbaijan, Rep. of", None, None, None, None, None, None, None, None, None],
                        ["Bahamas, The", None, None, None, None, None, None, None, None, None],
                        ["Bahrain, Kingdom of", None, None, "125.18", "134.69", "143.46", "151.08", "156.9", "167.5", "177.11"],
                        ["Bangladesh", None, None, None, None, None, None, None, None, None],
                        ["Barbados", None, None, None, None, None, None, None, None, None],
                        ["Belarus, Rep. of", None, None, None, None, None, None, None, None, None],
                        ["Belgium", None, None, None, None, None, None, None, None, None],
                        ["Belize", None, None, None, "41.61", "65.19", "62.38", "60.51", "51.95", "33.82"],
                        ["Benin", None, None, "148,214.99", "168,532.14", "187,659.49", "203,306.84", "218,253.22", "228,257.42", "244,301.30"]]
                    
        self.assertEqual(data, expect_data)

    # providing a query value and query column to only return rows where the
    # string at that column matches the value.
    def test_get_data_query_r(self):
        file_path = 'test_data.csv' 

        data = file_lib.get_data(file_path, query_value='Afghanistan', query_col=0)

        expect_data = [['Afghanistan', '1990', '14.7237', '0.0557' ,'205.6077'],
                       ['Afghanistan', '1991', '14.7237', '0.0557' ,'209.4971'],
                       ['Afghanistan', '1992', '14.7237', '0.0557' ,'196.5341'],
                       ['Afghanistan', '1993', '14.7237', '0.0557' ,'230.8175'],
                       ['Afghanistan', '1994', '14.7237', '0.0557' ,'242.0494'],
                       ['Afghanistan', '1995', '14.7237', '0.0557' ,'243.8152'],
                       ['Afghanistan', '1996', '38.9302', '0.2014' ,'249.0364']]

        self.assertEqual(data, expect_data)

        data = file_lib.get_data(file_path, query_value='Algeria', query_col=0)

        self.assertEqual(len(data), 1)

        data = file_lib.get_data(file_path, query_value='ALSKDFJ', query_col=0)

        self.assertEqual(data, None)




if __name__ == '__main__':
    unittest.main()


# A general search function that scans a list for a key and returns the index
# of that key

# A specific get_fire_gdp_year_data function that integrates the CO2 and GDP
# data for a particular country based on entries with shared years. 

