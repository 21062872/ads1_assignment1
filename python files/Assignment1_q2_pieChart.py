# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:09:21 2022
@author: TharindaArachchi
Assignment1 - Question2
Plot type : Pie chart
"""
# importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculatePercentage(meat):
    '''Return portion of meat as a percentage
        Used for printing purpose'''
    df_total = df_meat_total.sum()
    total_ro = df_total['Value'].astype(float)    
    if meat == 'PIG':
        df_pig = df_meat_total[df_meat_total['SUBJECT'] == 'PIG']
        pig_ro = df_pig['Value'].astype(float)
        perc = (pig_ro / total_ro) * 100
    elif meat == 'SHEEP':
        df_sheep = df_meat_total[df_meat_total['SUBJECT'] == 'SHEEP']
        sheep_ro = df_sheep['Value'].astype(float)
        perc = (sheep_ro / total_ro) * 100
    elif meat == 'BEEF':
        df_beef = df_meat_total[df_meat_total['SUBJECT'] == 'BEEF']
        df_beef_ro = df_beef['Value'].astype(float)
        perc = (df_beef_ro / total_ro) * 100
    else:
        df_poultry = df_meat_total[df_meat_total['SUBJECT'] == 'POULTRY']
        poultry_ro = df_poultry['Value'].astype(float)
        perc = (poultry_ro / total_ro) * 100
    perc = perc.round(2).to_string(index=False)
    return perc

def calculateAutoPct(values):
    '''Calculate percentage of portion
        Used for labeling the chart'''
    def autopct(pct):
        return '{p:.2f}%'.format(p=pct)
    return autopct
     
# reading csv file and loading to dataframe
df_meat = pd.read_csv('dataset_meat_consumption_worldwide.csv')
# replacing empty characters in csv with NAN 
df_meat = df_meat.replace('?', np.NaN)
# removing null values
df_meat = df_meat.dropna()
# filtering records for the current year
df_meat = df_meat[df_meat['TIME'] == 2022]
# removing unwanted columns
df_meat = df_meat.drop(['MEASURE','LOCATION','TIME'], axis=1)
# summing up total meat consumption
df_meat_total = df_meat.groupby(['SUBJECT'], as_index = False)['Value'].sum()

# printing calcualated percentage
print('Percentage of PIG consumption : ', calculatePercentage('PIG'), '%')
print('\nPercentage of SHEEP consumption : ', calculatePercentage('SHEEP'), '%')
print('\nPercentage of BEEF consumption : ', calculatePercentage('BEEF'), '%')
print('\nPercentage of POULTRY consumption : ', calculatePercentage('POULTRY'), '%')

# defining color list for pie chart
colors = ("red", "cyan","Yellow", "indigo")

# wedge properties
wp = { 'linewidth' : 1, 'edgecolor' : "green" }

# creating plot
plt.figure(figsize=(8,5))
plt.pie(df_meat_total.Value, labels=df_meat_total.SUBJECT, shadow = True, colors = colors, \
        startangle = 90, wedgeprops = wp, autopct=calculateAutoPct(df_meat_total.Value))
# adding legend
plt.legend(
              title ="Meat",
              loc ="lower left",
              bbox_to_anchor =(1, 0, 0.5, 1)
          )    
plt.title("Consumption of Meat in 2022")
plt.savefig('Total Meat Consumption in 2022 - Pie Chart.png', dpi=300)
plt.show()
