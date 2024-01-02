#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:46:41 2024

@author: saikiranakula
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data for Australia from an Excel file
file_path_australia = '/Users/saikiranakula/Downloads/API_2_DS2_en_csv_v2_6227700 2.xlsx'  # Replace with your actual file path
my_australia = pd.read_excel(file_path_australia)

# The index Set as 'Series Name'
my_australia.set_index('Series Name', inplace=True)

# Filtering out non-numeric columns
numeric_my_australia = my_australia.select_dtypes(include=['number'])
print(numeric_my_australia.describe())

# Create a heatmap using seaborn with 'coolwarm' cmap
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_my_australia, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f", cbar_kws={'label': 'Value'})
plt.title('Australia', fontsize=15, color='navy')

# Adding labels to the axes
plt.xlabel('Year', fontsize=12, color='blue')
plt.ylabel('Series Name', fontsize=12, color='blue')

# Show the plot
plt.show()
