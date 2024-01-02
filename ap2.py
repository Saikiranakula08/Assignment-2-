#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:40:44 2023

@author: saikiranakula
"""

import pandas as pd
import matplotlib.pyplot as plt

countries=['India', 'Brazil', 'Jordan', 'Spain', 'Canada', 'Morocco', 'Portugal', 'United Kingdom']
# Imagine 'df' is DataFrame
my = pd.read_csv('/Users/saikiranakula/Downloads/API_EN/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_6224818.csv', skiprows=3)

# Set as years in DataFrame
years_my = my.iloc[:, -10:]

# Inserting the selected data
req_data = my[my['Country Name'].isin(countries)][['Country Name', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']]

# Plotting the bar graph
req_data.plot.bar(x='Country Name', figsize=(12, 8))

# Creating the bar graph with data
plt.title('CO2 Emissions (kt)', color='darkgreen', fontsize=25)
plt.xlabel('Country Name', fontsize=15, color='grey')
plt.ylabel('CO2 Emissions (kt)', fontsize=15)

# Adding grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotating x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.show()
