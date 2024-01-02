#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:44:23 2023

@author: saikiranakula
"""

import pandas as pd
import matplotlib.pyplot as plt

countries=['India', 'China', 'France', 'Norway', 'Pakistan']

# Function to read data from an Excel file
def read_file(filename):
    # Read the Excel file into a DataFrame
    my = pd.read_excel(filename)
    
    # Convert the 'Year' column to integer type
    my['Year'] = my['Year'].astype(int)
    
    # Display summary statistics for DataFrame
    my.describe()
    
    # Select data for specific countries
    req_data = my[(my['Country Name'].isin(countries)) & (my['Year'].between(2015, 2022))]
    
    # Plotting the data
    for country in ['India', 'China', 'France', 'Norway', 'Pakistan']:
        country_data = req_data[req_data['Country Name'] == country]
        
        # Plotting the urban population
        plt.plot(country_data['Year'], country_data['Urban Population growth(annual %)'], label=country, linestyle='--')
        
        # Display summary statistics for the selected data
        print(country_data.describe())
        
        # Adding legend to the plot
        plt.legend()
        
        # Adding labels to the x and y axes
        plt.xlabel('Year', color='teal', size=12)
        plt.ylabel('Urban Population growth(annual %)', color='teal', size='12')

        # Adding a title to the plot
        plt.title('Urban Population growth(annual %)', color='darkkhaki', size=15)
        
        # Adding a grid to the plot for better readability
        plt.grid(True)
        plt.grid(which='major', color='#dddddd', linewidth=0.8)
        plt.grid(which='minor', color='#EEEEEE', linewidth=0.5)
        plt.minorticks_on()

# Specify the file path
filename = '/Users/saikiranakula/Downloads/Data1.xlsx'

# Call the read_file function with the specified file path
print(read_file(filename))