"""
Created on Sun Nov  6 16:12:32 2022
@author: TharindaArachchi
Assignment1 - Question1
Plot type : Line plot
"""
# importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def convertKilostoPounds(kgs): 
    """ This will convert unit of measure kilograms(kg) to pounds(lbs) """
    lbs = kgs * 2.20462
    return lbs

# making a dataframe from csv file
df_meat = pd.read_csv('dataset_meat_consumption_worldwide.csv')
# replacing empty characters in csv with NAN 
df_meat = df_meat.replace('?', np.NaN)
# removing null values
df_meat = df_meat.dropna()
# removing unwanted columns
df_meat = df_meat.drop('MEASURE', axis=1)
# convert unit of measurement
df_meat['Value_in_lbs'] = convertKilostoPounds(df_meat['Value'])
# summing up total meat consumption
df_meat_total = df_meat.groupby(['LOCATION','TIME'], as_index = False)['Value_in_lbs'].sum()
# rename columns
df_meat_total = df_meat_total.rename({'LOCATION': 'Country', 'TIME': 'Year', 'Value': 'Value_in_kgs'}, axis=1)
# filter data records after year 2010
df_meat_total_2021 = df_meat_total[df_meat_total['Year'] >= 2010]
# reshaping the dataset
df_meat_cons_pivot = df_meat_total_2021.pivot(index='Year', columns='Country',values='Value_in_lbs').reset_index()

print(df_meat_cons_pivot.head())

# create a new figure
plt.figure(figsize=(8,5))
# add a stylesheet
plt.style.use('ggplot')
# adding a title to the plot
plt.title('Meat Consumption Over Time')
# plot the grapgh
plt.plot(df_meat_cons_pivot.Year, df_meat_cons_pivot.AUS, 'b.-', label = 'Australia')
plt.plot(df_meat_cons_pivot.Year, df_meat_cons_pivot.CAN, 'r.-', label = 'Canada')
plt.plot(df_meat_cons_pivot.Year, df_meat_cons_pivot.COL, 'y.-', label = 'Colombia')
plt.plot(df_meat_cons_pivot.Year, df_meat_cons_pivot.TUR, 'g.-', label = 'Turkey')
plt.plot(df_meat_cons_pivot.Year, df_meat_cons_pivot.UKR, 'm.-', label = 'Ukraine')
plt.xticks(df_meat_cons_pivot.Year[::2])
# labeling the graph
plt.xlabel('Year')
plt.ylabel('Pounds (lbs)')
plt.legend(loc = 'lower right', title ="Countries", bbox_to_anchor =(0.8, 0, 0.3, 0))
# save plot as .png
plt.savefig('Meat Consumption over time - Line Plot.png', dpi=300)
plt.show()

