# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 20:28:29 2022
@author: TharindaArachchi
Assignment1 - Question2
Plot type : histogram
"""
# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculateBins(val):
    """ Using Freedman-Diaconis rule to calculate number of bins """
    q1 = val.quantile(0.25)
    q3 = val.quantile(0.75)
    iqr = q3-q1
    bin_width = (2 * iqr)/(len(val) ** (1/3))
    bin_count = int(np.ceil((val.max() - val.min()) / bin_width))
    return bin_count
    
# reading from the excel file and loading to dataframe
df_bat = pd.read_excel('dataset_of_icc_test_batters.xlsx')
# filter out records of players with atleast 50 matches played
df_bat = df_bat[df_bat['Mat'] >= 50]

# calculate number of bins 
bins = calculateBins(df_bat['Avg'])
print('\tNumber of bins = ', bins)

# adding a style
plt.style.use('ggplot')
# ploting histogram
plt.hist(df_bat['Avg'], bins=bins, alpha=0.7, color='#ab34eb', edgecolor='black')
# labeling the plot
plt.ylabel('Number of players')
plt.xlabel('Batting Average')
plt.title('Distribution of player batting average in ICC')
plt.savefig('Distribution of player batting average - Histogram.png', dpi=300)
plt.show()

