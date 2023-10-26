import unittest
import fire_gdp
import random

class TestRyan(unittest.TestCase):

    
    # goal: for some country plot the fire v gdp over time
    # fire data is in agro... gdp datq is in img...

    # some of the gdp data is not avaiable, so must handle that
    # get the year and fire data, search for year in header, grab the gdp col 
    # to get year from fire just call get data twice
    
    def test_clean_str(self):
        self.assertEqual(fire_gdp.clean_str('1,000'), '1000')
        self.assertEqual(fire_gdp.clean_str('1,000,000'), '1000000')
  
    def test_search(self):
        self.assertEqual(fire_gdp.search([1,2,3,4,5], 3), 2)
        self.assertEqual(fire_gdp.search([1,2,3,4,5], 100), None)
        self.assertEqual(fire_gdp.search([1,2,3,3,4,5], 3), 2)
        self.assertEqual(fire_gdp.search([3,1,2,3,4,5], 3), 0)
        self.assertEqual(fire_gdp.search([], 3), None)

        for i in range(100):
            random_list = [random.randint(1,100000) for x in range(1000)]
            random_value = random.choice(random_list)
            first_value = random_list[0]
            no_hit_value = 1000000
            self.assertIsNotNone(fire_gdp.search(random_list, random_value))
            self.assertIsNone(fire_gdp.search(random_list, no_hit_value))
            self.assertEqual(fire_gdp.search(random_list,first_value), 0)

        
    def test_ryan(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'

        fire_year_col = 1
        fire_savanna_col = 2
        fire_forest_col = 3
        
        # 1: [ [fire], [gdp], [year] ]
        
        country = 'Albania'
        
        data = fire_gdp.ryan(fire_file_name,
                             gdp_file_name,
                             country,
                             fire_year_col,
                             fire_savanna_col,
                             fire_forest_col)

        fire = data[0]
        gdp = data[1]
        year = data[2]
        
        self.assertEqual(1.3469 + 13.3278, fire[0])
        self.assertEqual(334359.13, gdp[0])
        self.assertEqual(1996, year[0])
        
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
        
        
    def test_get_data_fire_and_year(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        target_country = 'Albania'
        
        data = fire_gdp.get_data(fire_file_name, 
                                 query_value=target_country, 
                                 query_col=0)
        
        self.assertEqual(data[0][0], 'Albania')
        self.assertEqual(data[0][1], '1990')
        self.assertEqual(data[1][2], '5.5561')
        
    def test_get_gdpr(self):
        gdp_file_name = 'IMF_GDP.csv'
        target_country = 'Albania'
        
        data = fire_gdp.get_data(gdp_file_name, 
                                 query_value=target_country, 
                                 query_col=0)
        
        self.assertEqual(data[0][2], '...')
        self.assertEqual(data[0][47],'334,359.13')

    
        
    def test_get_get_header(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'
        empty_file_name = 'empty.txt'
        
        target_country = 'Zimbabwe'
        
        data, header = fire_gdp.get_data(fire_file_name, 
                                     query_value=target_country, 
                                     query_col=0,
                                     get_header=True)
        self.assertEqual(len(data), 31)
        self.assertEqual(len(header), 31)
        
        data,header = fire_gdp.get_data(gdp_file_name,
                                    query_value=target_country,
                                    query_col=0,
                                    get_header=True)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(len(header), 74)
        
        data, header = fire_gdp.get_data(empty_file_name,
                                     query_value=target_country,
                                     query_col=0,
                                     get_header=True)
         
        self.assertEqual(len(data), 0)
        self.assertEqual(len(header), 0)       
        
        data, header = fire_gdp.get_data(gdp_file_name,
                                     query_value=target_country,
                                     query_col=1,
                                     get_header=True) 
        
        self.assertEqual(len(data), 0)
        self.assertEqual(len(header), 74)
        
        self.assertRaises(IndexError,
                          fire_gdp.get_data,
                          gdp_file_name,
                          query_value=target_country,
                          query_col=10000,
                          get_header=True)
        
if __name__ == '__main__':
    unittest.main()
        
