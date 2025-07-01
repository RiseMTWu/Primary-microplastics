# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:06:05 2024

@author: lenovo
"""
##############################  TWP gini
import numpy as np
import pandas as pd


data = pd.read_csv('../TWP_Gini_dataset.csv', encoding="GBK")


def gini_coefficient_index(data):
    n = len(data)
    coef = 2 / n
    constant = (n + 1) / n
    weighted_sum = sum([(i + 1) * yi for i, yi in enumerate(data)])
    total = sum(data)
    gini = coef * weighted_sum / total - constant
    return gini

def gini_coefficient_standard(data):
    n = len(data)
    indexed_data = (2 * np.arange(1, n + 1) - n - 1) * data
    gini = np.sum(indexed_data) / (n * np.sum(data))
    return gini


columns_to_compute = ['Total', 'car', 'airplane', 'Emission','ocean', 'oil', 'river']


for column in columns_to_compute:
   
    grouped_data = data.groupby('level')[column].sum().reset_index(name=f'{column}_amount')
    
    
    is_sorted = grouped_data[f'{column}_amount'].is_monotonic_increasing
    if is_sorted:
        print(f"{column} Column in ascending order")
    else:
        print(f"{column} Column is not in ascending order")

  
    sorted_data = grouped_data[f'{column}_amount'].sort_values().values
    
  
    gini_index = gini_coefficient_index(sorted_data)
    gini_standard = gini_coefficient_standard(sorted_data)
    
    
    print(f"{column} column Gini coefficient (Index method): {gini_index}")
    print(f"{column} Column Gini coefficient (standardized method): {gini_standard}")
    print()
#%%
########################### PMs gini
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../PMs_Gini_dataset.csv',encoding="GBK",low_memory=False)

def gini_coefficient_index(data):
    n = len(data)
    coef = 2 / n
    constant = (n + 1) / n
    weighted_sum = sum([(i + 1) * yi for i, yi in enumerate(data)])
    total = sum(data)
    gini = coef * weighted_sum / total - constant
    return gini

def gini_coefficient_standard(data):
    n = len(data)
    indexed_data = (2 * np.arange(1, n + 1) - n - 1) * data
    gini = np.sum(indexed_data) / (n * np.sum(data))
    return gini


columns_to_compute = ['PMs', 'PMs1', 'PMs2', 'yagao', 'myl', 'msg','xmn','soil','ocean','river','emission']


for column in columns_to_compute:
    
    grouped_data = data.groupby('level')[column].sum().reset_index(name=f'{column}_amount')

    
    sorted_data = grouped_data[f'{column}_amount'].sort_values().values
    
  
    gini_index = gini_coefficient_index(sorted_data)
    gini_standard = gini_coefficient_standard(sorted_data)
    
   
    print(f"{column} column Gini coefficient (Index method): {gini_index}")
    print(f"{column} Column Gini coefficient (standardized method): {gini_standard}")
    print()
#%%
################             MFs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('../MFs_Gini_dataset.csv',encoding="GBK")



def gini_coefficient_index(data):
    n = len(data)
    coef = 2 / n
    constant = (n + 1) / n
    weighted_sum = sum([(i + 1) * yi for i, yi in enumerate(data)])
    total = sum(data)
    gini = coef * weighted_sum / total - constant
    return gini

def gini_coefficient_standard(data):
    n = len(data)
    indexed_data = (2 * np.arange(1, n + 1) - n - 1) * data
    gini = np.sum(indexed_data) / (n * np.sum(data))
    return gini


columns_to_compute = ['MFs_generation', 'MW', 'HW','MFs_emission', 'ocean', 'soil','river']


for column in columns_to_compute:
   
    grouped_data = data.groupby('level')[column].sum().reset_index(name=f'{column}_amount')

  
    sorted_data = grouped_data[f'{column}_amount'].sort_values().values
    

    gini_index = gini_coefficient_index(sorted_data)
    gini_standard = gini_coefficient_standard(sorted_data)
    
    print(f"{column} column Gini coefficient (Index method): {gini_index}")
    print(f"{column} Column Gini coefficient (standardized method): {gini_standard}")
    print()
#%%
################################ MPs Gini
import numpy as np
import pandas as pd
data = pd.read_csv('../MPs_Gini.csv',encoding="GBK")


def gini_coefficient_index(data):
    n = len(data)
    coef = 2 / n
    constant = (n + 1) / n
    weighted_sum = sum([(i + 1) * yi for i, yi in enumerate(data)])
    total = sum(data)
    gini = coef * weighted_sum / total - constant
    return gini

def gini_coefficient_standard(data):
    n = len(data)
    indexed_data = (2 * np.arange(1, n + 1) - n - 1) * data
    gini = np.sum(indexed_data) / (n * np.sum(data))
    return gini


columns_to_compute = ['MPs_ge', 'TWP_ge', 'MFs_ge','PMs_ge', 'MPs_em', 'TWP_em','MFs_em','PMs_em']


for column in columns_to_compute:

    grouped_data = data.groupby('level')[column].sum().reset_index(name=f'{column}_amount')


    sorted_data = grouped_data[f'{column}_amount'].sort_values().values
    

    gini_index = gini_coefficient_index(sorted_data)
    gini_standard = gini_coefficient_standard(sorted_data)
    
    print(f"{column} column Gini coefficient (Index method): {gini_index}")
    print(f"{column} Column Gini coefficient (standardized method): {gini_standard}")
    print()

#%%
################################ MPs Gini by City Category
import numpy as np
import pandas as pd


data = pd.read_csv('../MPs_Gini.csv', encoding="GBK")


def gini_coefficient_index(data):
    n = len(data)
    coef = 2 / n
    constant = (n + 1) / n
    weighted_sum = sum([(i + 1) * yi for i, yi in enumerate(data)])
    total = sum(data)
    gini = coef * weighted_sum / total - constant
    return gini

def gini_coefficient_standard(data):
    n = len(data)
    indexed_data = (2 * np.arange(1, n + 1) - n - 1) * data
    gini = np.sum(indexed_data) / (n * np.sum(data))
    return gini


columns_to_compute = ['MPs_ge', 'TWP_ge', 'MFs_ge','PMs_ge', 'MPs_em', 'TWP_em','MFs_em','PMs_em']


categories = data['Category'].unique()


for cat in categories:
    print(f"===== Category: {cat} =====")
    cat_data = data[data['Category'] == cat]

    for column in columns_to_compute:
       
        grouped_data = cat_data.groupby('level')[column].sum().reset_index(name=f'{column}_amount')
     
        sorted_data = grouped_data[f'{column}_amount'].sort_values().values
        
    
        gini_index = gini_coefficient_index(sorted_data)
       
        gini_standard = gini_coefficient_standard(sorted_data)
        
        print(f"{column} Gini coefficient (Index method): {gini_index:.4f}")
        print(f"{column} Gini coefficient (Standard method): {gini_standard:.4f}")
        print()