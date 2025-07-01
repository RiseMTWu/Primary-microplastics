# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 09:38:47 2025

@author: DELL
"""

##############################  Summary of results ——TWP
import pandas as pd

years = range(2020, 2036)
columns = [
    "city", "TWP mean", "TWP std", "TWP 0.05", "TWP 0.25", "TWP 0.75", "TWP 0.95",
    "Vehicle mean", "Vehicle std", "Vehicle 0.05", "Vehicle 0.25", "Vehicle 0.75", "Vehicle 0.95",
    "Airplane mean", "Airplane std", "Airplane 0.05", "Airplane 0.25", "Airplane 0.75", "Airplane 0.95",
    "Ocean mean", "Ocean std", "Ocean 0.05", "Ocean 0.25", "Ocean 0.75", "Ocean 0.95",
    "Soil mean", "Soil std", "Soil 0.05", "Soil 0.25", "Soil 0.75", "Soil 0.95",
    "River mean", "River std", "River 0.05", "River 0.25", "River 0.75", "River 0.95"
]

folder = '../results/' 
output_excel = folder + 'TWP_result_reduce1_arrange.xlsx'

with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
    for year in years:
        file_path = f'{folder}TWP_{year}result_reduce1.csv'
        df = pd.read_csv(file_path, header=None).T
        
        # Delete the first row after transposition (old column names)
        df = df.drop(index=0).reset_index(drop=True)
        # Set the new column name
        df.columns = columns
        
        
        for col in df.columns:
            if col != "city":
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        
        df["TWP emission"] = (
            df["Ocean mean"] +
            df["soil mean"] +
            df["River mean"]
        )
        df.to_excel(writer, sheet_name=str(year), index=False,float_format='%.8f')

print(f"All year data has been written into multiple sheets:{output_excel}")
#%%
##############################  Summary of results ————————MFs
import pandas as pd

years = range(2020, 2036)
columns = [
    "city","MFs mean", "MFs std", "MFs 0.05", "MFs 0.25", "MFs 0.75", "MFs 0.95",
    "MW mean", "MW std", "MW 0.05", "MW 0.25", "MW 0.75", "MW 0.95",
    "HW mean", "HW std", "HW 0.05", "HW 0.25", "HW 0.75", "HW 0.95",
    "Ocean mean", "Ocean std", "Ocean 0.05", "Ocean 0.25", "Ocean 0.75", "Ocean 0.95",
    "Soil mean", "Soil std", "Soil 0.05", "Soil 0.25", "Soil 0.75", "Soil 0.95",
    "River mean", "River  std", "River 0.05", "River 0.25", "River 0.75", "River 0.95"
]

folder = '../results/' 
output_excel = folder + 'MFs_result_reduce1_arrange.xlsx'

with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
    for year in years:
        file_path = f'{folder}MFs_{year}result_reduce1.csv'
        df = pd.read_csv(file_path, header=None).T
        
        df = df.drop(index=0).reset_index(drop=True)
        df.columns = columns
        

        for col in df.columns:
            if col != "city":
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        
        df["MFs emission"] = (
            df["ocean mean"] +
            df["soil mean"] +
            df["River mean"]
        )
        df.to_excel(writer, sheet_name=str(year), index=False,float_format='%.8f')

print(f"All year data has been written into multiple sheets:{output_excel}")
