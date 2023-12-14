#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:40:44 2023

@author: saikiranakula
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame
df=pd.read_csv('/Users/saikiranakula/Downloads/API_EN/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_6224818.csv',skiprows=3)
print(df)
years_df = df.iloc[:, -10:]
print(years_df)
selected_data = df[df['Country Name'].isin(['India','Brazil','Jordan','Spain','Canada','Morocco','Portugal','United Kingdom'])][['Country Name','2015','2016','2017','2018','2019','2020','2021','2022']]
print(selected_data)
selected_data.plot.bar(x='Country Name',figsize=(12,8))

plt.title('CO2 emissions (kt))',color='darkgreen',fontsize=(25))
plt.xlabel('Country Name',fontsize=(15),color='grey')
plt.ylabel('CO2 emissions (kt)',fontsize=(15))

