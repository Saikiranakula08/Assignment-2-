#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:56:23 2024

@author: saikiranakula
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data for Japan from an Excel file
file_path_japan = '/Users/saikiranakula/Downloads/API_3_DS2_en_csv_v2_6227700 2.xlsx'  # Replace with your actual file path
my_japan = pd.read_excel(file_path_japan)

# The index Set as 'Series Name'
my_japan.set_index('Series Name', inplace=True)

# Filtering out non-numeric columns
numeric_my_japan = my_japan.select_dtypes(include=['number'])
print(numeric_my_japan.describe())

# Create a heatmap using seaborn with 'cividis' cmap
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_my_japan, annot=True, cmap='cividis', linewidths=0.5, fmt=".2f", cbar_kws={'label': 'Value'})
plt.title('Japan', fontsize=15, color='purple')

# Adding labels to the axes
plt.xlabel('Year', fontsize=12, color='purple')
plt.ylabel('Series Name', fontsize=12, color='purple')

# Show the plot
plt.show()