# in terminal run: `pip install pandas` to install the pandas library
import pandas as pd # we rename pandas to pd just to make it easier to type, this is the industry standards
from scipy import stats

# load a file with pandas
agro_df = pd.read_csv('Data/Agrofood_co2_emission.csv')

print(agro_df.head())
print(agro_df.shape)
print(type(agro_df))

# there are 31 columns, but it only shows 10 at a time, lets print all the columns
print(agro_df.columns)
print(list(agro_df.columns).index('Food Processing'))

# okay that is cool, but how do I interact with my data now?

print(agro_df['Area'])
# but we don't care about duplicate countries, how can I get only the unique countries?
countries = set(agro_df['Area'])
print(countries)
print(len(countries))
countries = agro_df['Area'].unique()
print(countries)
print(len(countries))

# lets use this to get only the information about 'Romania'
result = agro_df['Area'] == 'Romania'
print(result)
print(type(result))
print(len(result))

romanian_df = agro_df[agro_df['Area'] == 'Romania']

print(romanian_df.head())

# what about if we only want specific columns?

romanian_fires = romanian_df[['Savanna fires','Forest fires']]

print(romanian_fires.head())

# we can also access information in a DF with indecies, row - col
print(romanian_df.iloc[0:10,0:5])

# doing math on columns
# I study fires but I don't care about the distrinction between forest and savanna fires, lets combine them into a single total fires column
romanian_df['total_fires'] = romanian_df['Savanna fires'] + romanian_df['Forest fires']

# lets check that works and print the top 5 rows of those three columns
print(romanian_df.iloc[0:5,:][['Savanna fires','Forest fires','total_fires']])


# Challenge 1 time!
'Canada', 'Manure applied to Soils', 'Manure left on Pasture', 'Manure Management'

canadian_poop = agro_df[agro_df['Area'] == 'Canada'][['Manure applied to Soils', 'Manure left on Pasture', 'Manure Management']]
print(canadian_poop)
print(canadian_poop.shape)
print(canadian_poop['Manure left on Pasture'].mean())
print(canadian_poop['Manure applied to Soils'].mean())
print(canadian_poop['Manure Management'].mean())


# part 2 cleaning data

gdp_df = pd.read_csv('Data/IMF_GDP.csv')
print(gdp_df.head())
print(gdp_df.shape)

# ... is not a good way to denote missing data.
# lets replace it with -1 or NaN
gdp_df = gdp_df.replace('...',None)
gdp_df = gdp_df.replace('-',None)

# lets get the median GPD of Cananda - will causes errors
can_gdps = gdp_df[gdp_df['Country'] == 'Canada'].iloc[0,1:]
# print(can_gdps.median())

# replace ',' with '' - shit that did not work
gdp_df = gdp_df.replace(',','')

# remove ',' from numbers
def destroy_commas(x):
    if x is None:
        return None
    return float(x.replace(',',''))

for col in gdp_df.columns:
    if col == 'Country':
        continue
    gdp_df[col] = gdp_df[col].apply(destroy_commas)

print(gdp_df.head())

# what is the median GDP for canada
can_gdp = gdp_df[gdp_df['Country'] == 'Canada']

print('Canadian median GPD:',can_gdp.iloc[0,1:].median())

# merging data
# add GDP info to the AG Data and save it to a file

print(agro_df)

print(can_gdp)
# transpose the data so we can merge
can_gdp = can_gdp.T.reset_index()
print(can_gdp)
can_gdp.columns = ['year','GDP']

print(can_gdp)

# remove the top row, or we can just merge on year
can_gdp = can_gdp.iloc[1:,:]

can_agro = agro_df[agro_df['Area'] == 'Canada']

# because the types are mismatched
print(can_agro.dtypes)
print(can_gdp.dtypes)

can_gdp['year'] = can_gdp['year'].astype('int64')

can_agro_gdp = pd.merge(can_agro,can_gdp,how='inner',left_on='Year',right_on='year')

print(can_agro_gdp)

# remove the extra year column
# instead of specifying everything we want, we can specify what we do not want

can_agro_gdp = can_agro_gdp.drop('year',axis=1)

print(can_agro_gdp)
# save the file
can_agro_gdp.to_csv('canada_agro_gpd.tsv', sep='\t', index=False)


print(can_agro_gdp.corr())
highest = 0
highest_pair = None
lowest = 1
lowest_pair = None
corr_df = can_agro_gdp.corr()
for i in range(corr_df.shape[0]):
    for j in range(corr_df.shape[1]):
        if i == j:
            continue
        val = corr_df.iloc[i,j]
        if type(val) == str:
            continue
        if val > highest:
            highest = val
            highest_pair = (corr_df.columns[i], corr_df.columns[j])
        if val < lowest:
            lowest = val
            lowest_pair = (corr_df.columns[i], corr_df.columns[j])

print(lowest, lowest_pair)
print(highest, highest_pair)

# what if I want to do a t-test for if the 'Average Temperature °C' 1990 - 2000 vs 2001 2010
set1 = can_agro_gdp[can_agro_gdp['Year'] <= 2000]['Average Temperature °C']
set2 = can_agro_gdp[(can_agro_gdp['Year'] > 2000) & (can_agro_gdp['Year'] <= 2010)]['Average Temperature °C']

print(set1)
print(set2)

print('T-test',stats.ttest_ind(set1, set2))

# is our data normally distributed? p > 0.05 we regent the null hypothesis and it is not normal
# normaltest
print('Is set 1 normal?', stats.normaltest(set1))
print('Is set 2 normal?', stats.normaltest(set2))

print('Mann-Whitneyu',stats.mannwhitneyu(set1, set2))

# Challange 2
# Is there a statisticall difference between the Rice Cultivation between the US and China mainland for 2000-2020? Who produdes more on average?