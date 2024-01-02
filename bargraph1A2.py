#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:54:39 2023

@author: saikiranakula
"""

import pandas as pd
import matplotlib.pyplot as plt

countries=['India','Brazil','Jordan','Spain','Canada','Morocco','Portugal','United Kingdom']
# Imagine 'df' is your DataFrame
my = pd.read_csv('/Users/saikiranakula/Downloads/API_EN-2/API_EN.ATM.METH.KT.CE_DS2_en_csv_v2_6232520.csv',skiprows=3)
print(my)

# Set to years in df
years_my = my.iloc[:, -10:]
print(years_my)

#Insert the data by Country wise
req_data = my[my['Country Name'].isin(countries)][['Country Name','2015','2016','2017','2018','2019','2020','2021','2022']]
print(req_data)

print(req_data.describe())

# Plotting the bar graph
req_data.plot.bar(x = 'Country Name',figsize = (12,8))

# Creating the bar graph
plt.title('Methane emissions (kt of CO2 equivalent))',color = 'darkgreen',fontsize = (25))
plt.xlabel('Country Name',fontsize = (15),color = 'blue')
plt.ylabel('(kt of CO2 equivalent)',fontsize = (15))
plt.show 