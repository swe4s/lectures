file_name = 'covid-19-data/us-counties.csv'

f = open(file_name, 'r')

for l in f:
    print(l, end='')

f.close()
