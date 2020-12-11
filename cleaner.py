import pandas as pd 
import numpy as np

df = pd.read_csv('Employment Data.csv')

# Full time employment
# Undergraduate, taught post grad, research post graduate
# How has COVID and Hong Kong Political Instability affected employment of UGC funded graduates and post graduates (across diferent sectors and university)
#Are there trends in sector wise hiring across the years 

#Change pips back to commas
#remove nans
#remove sub degree
#make year a date
df.dropna(inplace=True)
for index,row in df.iterrows():
    s = row['Occupation'].replace(' |',',')
    df.at[index,'Occupation'] = s
df['Academic Year'] = pd.to_datetime(df['Academic Year'].str[:-3],format='%Y')
df = df[df['Level of study']!='Sub-degree']

#GRAPH1 - Academic year against occupation
occ_year = df[['Academic Year', 'Occupation', 'Number of Graduates']]
occ_year = occ_year.groupby(['Academic Year','Occupation'],as_index = False).agg({'Number of Graduates':'sum'})
axes = occ_year.plot.line(subplots=True)

occupations = list(set(df['Occupation']))
years = list(set(df['Academic Year']))

num_people_per_occ = {occ:0 for occ in occupations}
for ind,row in df.iterrows():
    num_people_per_occ[row['Occupation']]+=row['Number of Graduates']


#How many are underemployed
employment_stats = df.groupby('Employment Situation').count()