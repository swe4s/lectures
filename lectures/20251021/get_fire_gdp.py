import file_lib
import sys

co2_country = sys.argv[1]
gdp_country = sys.argv[2]

file_path = 'Agrofood_co2_emission.csv'

data_co2 = file_lib.get_data(file_path,
                                query_value=co2_country,
                                query_col=0,
                                header=True)
years = [row[1] for row in data_co2.data]
fire_co2 = [row[2] for row in data_co2.data]



file_path = 'IMF_GDP.csv'

data_gdp = file_lib.get_data(file_path,
                                query_value=gdp_country,
                                query_col=0,
                                header=True)

for i in range(len(years)):
    year = years[i]
    co2_emission = fire_co2[i]
    gdp_string = file_lib.search_parallel_lists(data_gdp.data[0], # data_gdp is a list of lists
                                                data_gdp.header,
                                                year) # holds the year
    if gdp_string is None:
        continue
    gdp_float = float(gdp_string.replace(",", ""))
    print(f'{float(co2_emission)}\t{gdp_float}')
