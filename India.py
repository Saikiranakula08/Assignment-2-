#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:05:17 2024

@author: saikiranakula
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data for India from an Excel file
file_path_india = '/Users/saikiranakula/Downloads/API_4_DS2_en_csv_v2_6227700 2.xlsx'  # Replace with your actual file path
my_india = pd.read_excel(file_path_india)

# The index set as 'Series Name'
my_india.set_index('Series Name', inplace=True)

# Filtering out non-numeric columns
numeric_my_india = my_india.select_dtypes(include=['number'])
print(numeric_my_india.describe())


# Create a heatmap using seaborn with 'viridis' cmap
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_my_india, annot=True, cmap='viridis', linewidths=0.5, fmt=".2f", cbar_kws={'label': 'Value'})
plt.title('India', fontsize=15, color='black')

# Adding labels to the axes
plt.xlabel('Year', fontsize=12, color='orange')
plt.ylabel('Series Name', fontsize=12, color='orange')

# Show the plot
plt.show()
