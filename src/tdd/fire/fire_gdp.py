import csv

def clean_str(string):
    return string.replace(",", "")

def get_data(file_name, query_value=None, query_col=None, get_header=False):
    header = []
    data = []
    
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if query_value is None or query_col is None:
                data.append(row)
            else:
                if get_header and len(header) == 0:
                    header = row
                    continue
                if row[query_col] == query_value:
                    data.append(row)
    if get_header:
        return data, header
    else:
        return data

def search(L, k):
    for i, value in enumerate(L):
        if k == value:
            return i
    return None
    
def get_fire_gdp_year_data(fire_file_name,
                           gdp_file_name,
                           target_country,
                           fire_year_col,
                           fire_savanna_col,
                           fire_forest_col):
    
    fire_datas = get_data(fire_file_name, 
                         query_value=target_country, 
                         query_col=0)

    gdp_datas, header = get_data(gdp_file_name,
                                 query_value=target_country,
                                 query_col=0,
                                 get_header=True)
    
    fires = []
    gdps = []
    years = []
    
    for fire_data in fire_datas:
        year = fire_data[fire_year_col]
        year_idx = search(header, year)
        if gdp_datas[0][year_idx] != '...':
            fires.append(float(fire_data[fire_savanna_col]) + float(fire_data[fire_forest_col]))
            years.append(int(year))
            gdps.append(float(clean_str(gdp_datas[0][year_idx])))
            
    return [fires, gdps, years]

    