import unittest
import fire_gdp


class TestRyan(unittest.TestCase):

    
    # goal: for some country plot the fire v gdp over time
    # fire data is in agro... gdp datq is in img...

    # get fire data
    # TEST make sure files are there
    # open it up and get for a country get fire data for each year
    # get gdp data
    # open up a file
    # for some country and year get gdp data
    # TEST make sure files are there
    # TEST for empty rows

    def test_get_data_open_file(self):
            fire_file_name = 'Agrofood_co2_emission.csv'
            gdp_file_name = 'IMF_GDP.csv'
            dne_file_name = 'fire_gdp.txt'
            empty_file_name = 'empty.txt'

    
            self.assertEqual(fire_gdp.get_data(empty_file_name), [])
            self.assertRaises(FileNotFoundError, fire_gdp.get_data, dne_file_name)
            
    def test_get_data_read_lines(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'
        empty_file_name = 'empty.txt'

        self.assertEqual(len(fire_gdp.get_data(fire_file_name)), 6966)
        self.assertEqual(len(fire_gdp.get_data(gdp_file_name)), 199)
        self.assertEqual(len(fire_gdp.get_data(empty_file_name)), 0)
        
    def test_get_data_query_lines(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'
        empty_file_name = 'empty.txt'
        
        target_country = 'Zimbabwe'
        
        self.assertEqual(len(fire_gdp.get_data(fire_file_name, 
                                           query_value=target_country, 
                                           query_col=0)), 
                        31)
        
        self.assertEqual(len(fire_gdp.get_data(gdp_file_name,
                                           query_value=target_country,
                                           query_col=0)), 
                         1)
        
        self.assertEqual(len(fire_gdp.get_data(empty_file_name,
                                           query_value=target_country,
                                           query_col=0)),
                         0)
        
        self.assertEqual(len(fire_gdp.get_data(gdp_file_name,
                                           query_value=target_country,
                                           query_col=1)), 
                         0)
        
        self.assertRaises(IndexError,
                          fire_gdp.get_data,
                          gdp_file_name,
                          query_value=target_country,
                          query_col=10000)
        
    def test_get_get_header(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'
        empty_file_name = 'empty.txt'
        
        target_country = 'Zimbabwe'
        
        data, header = fire_gdp.get_data(fire_file_name, 
                                     query_value=target_country, 
                                     query_col=0,
                                     header=True)
        self.assertEqual(len(data), 31)
        self.assertEqual(len(header), 31)
        
        data,header = fire_gdp.get_data(gdp_file_name,
                                    query_value=target_country,
                                    query_col=0,
                                    header=True)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(len(header), 74)
        
        data, header = fire_gdp.get_data(empty_file_name,
                                     query_value=target_country,
                                     query_col=0,
                                     header=True)
         
        self.assertEqual(len(data), 0)
        self.assertEqual(len(header), 0)       
        
        data, header = fire_gdp.get_data(gdp_file_name,
                                     query_value=target_country,
                                     query_col=1,
                                     header=True) 
        
        self.assertEqual(len(data), 0)
        self.assertEqual(len(header), 74)
        
        self.assertRaises(IndexError,
                          fire_gdp.get_data,
                          gdp_file_name,
                          query_value=target_country,
                          query_col=10000,
                          header=True)
        
        
