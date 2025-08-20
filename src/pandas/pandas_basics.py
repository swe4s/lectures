import numpy as np
import pandas as pd
from functools import reduce


#Let's import some data from csv files to pandas dataframes! 
cgm = pd.read_csv('./data/cgm_aligned.csv')
hr = pd.read_csv('./data/hr_aligned.csv')
meal = pd.read_csv('./data/meal_aligned.csv')

# If pandas imported some "junk" that we had in the spreadsheet and
# resulted in extra "Unnamed" columns, we can filter for and drop them by using
# text parsing (str.contains())
cgm = cgm.loc[:, ~cgm.columns.str.contains('^Unnamed')]
hr = hr.loc[:, ~hr.columns.str.contains('^Unnamed')]
meal = meal.loc[:, ~meal.columns.str.contains('^Unnamed')]

#lets rename columns
cgm.rename(columns={"value":"cgm"},inplace=True)
hr.rename(columns={"value":"hr"},inplace=True)
meal.rename(columns={"value":"meal"},inplace=True)

#we have problems in the cgm file.... lets replace words with values

#first, let's find all the unique elements that cannot be cast to int
uniq = cgm.cgm[~cgm.cgm.str.isnumeric()].unique()
print(uniq) #print them out

#to make it easier, lets lowercase everything
cgm.cgm=cgm.cgm.str.lower()
uniq = cgm.cgm[~cgm.cgm.str.isnumeric()].unique()
print(uniq) #now we just have lower case words, there are fewer unique items

#replace the words with integer values
cgm.cgm.replace('dog',40,inplace=True)
cgm.cgm.replace('cat',400,inplace=True)
cgm.cgm.replace('platypus',138,inplace=True)

#now we can cast the column as int type
cgm.cgm=cgm.cgm.astype(int)

#we can combine our dataframes to a list. Note this list has pointers to our dataframes (not copied versions)
listOfFrames = [cgm, hr, meal]

#lets set the indexes to be time
for frame in listOfFrames:
    frame.set_index('time',inplace=True)

#Lets join the frames together with an inner join (left join default)
joinFrame = cgm.join([hr,meal], how='inner')

#lets fill in any nan values with 0. We will do this inplace to not create a copy
joinFrame.fillna(0,inplace=True)


#Here is an example of how to use a lambda (anonymous) function with merge & reduce to do a similar task
# see the pandas notes for explanations
mergedFrame = reduce(lambda x, y: pd.merge(x, y, left_index=True, right_index=True, how='inner'), listOfFrames)

#or we can concat on the index and perform an outer join
concatFrame = reduce(lambda x,y: pd.concat([x, y], axis=0, join='outer',sort=True),listOfFrames)


# if we want, we can view the results
print(mergedFrame.head())
print(joinFrame.head())
print(concatFrame.head())

print('Descriptions for frames')
print(mergedFrame.describe())
print(joinFrame.describe())
print(concatFrame.describe())

#check how it compares to descriptions of our original dataframes.
#this is useful to see if you have dropped rows, duplicated rows, etc.
print(cgm.describe())
print(hr.describe())
print(meal.describe())




#now lets work with time stamps
cgm.index = pd.to_datetime(cgm.index)
#add a new column
cgm.insert(len(cgm.columns),'DT',cgm.index)
#lets get the difference between values, and add it as a new column
cgm.insert(len(cgm.columns),'DT_diff',cgm.DT.diff())

#lets make a column that rounds to nearest 15minute interval
cgm.insert(len(cgm.columns),'15min',cgm['DT'].dt.round('15min'))

#lets group by our new times, and get the means
roundedCGM = cgm.groupby('15min')['cgm'].mean()




# Let's try pivoting with the gtex data
gtex = pd.read_table('gtex.txt')
print(gtex.columns)
print(gtex.SMTS.unique())

#lets pull the just two columns
gtexSmall = gtex[['SMTS','SAMPID']]

#pivot to group by tissue type
byTissue = gtexSmall.pivot(columns='SMTS', values='SAMPID')

#get the stats and pull sums of unique sample IDs per tissue type
stats = byTissue.describe()
genesPerType = stats.loc['count']
