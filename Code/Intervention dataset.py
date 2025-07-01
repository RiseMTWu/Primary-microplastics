# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 09:03:18 2025

@author: DELL
"""
###########               Considering only conversion factors — Dataset construction -TWP
import pandas as pd
import os


folder_path1 = r'../2020-2035Dataset'
folder_path2 = r'../Contribution of interventions/'


columns_to_replace =[
    "Vehicles",
    "small1", "cityroadA", "M1", "ruralroadA", "M2", "highwayA", "M3",
    "medium1", "cityroadB", "M4", "ruralroadB", "M5", "highwayB", "M6",
    "big1", "cityroadC", "M7", "ruralroadC", "M8", "highwayC", "M9",
    "small2", "cityroadD", "M10", "ruralroadD", "M11", "highwayD", "M12",
    "medium2", "cityroadE", "M13", "ruralroadE", "M14", "highwayE", "M15",
    "big2", "cityroadF", "M16", "ruralroadF", "M17", "highwayF", "M18","Airplaneinput"
]


for year in range(2020, 2036):
  
    reduce_path = os.path.join(folder_path1 , f'TWP_{year}reduce.csv')
    bau_path = os.path.join(folder_path1 , f'TWP_{year}BAU.csv')
    output_path = os.path.join(folder_path2 , f'TWP_{year}reduce1.csv')

    try:
       
        df_reduce = pd.read_csv(reduce_path, encoding="GBK")
        df_bau = pd.read_csv(bau_path, encoding="GBK")

        
        for col in columns_to_replace:
            if col in df_reduce.columns and col in df_bau.columns:
                df_reduce[col] = df_bau[col]
            else:
                print(f'⚠️ {year}: Column "{col}" not found in file, skipping.')
        
       
        df_reduce.to_csv(output_path, index=False, encoding='GBK',float_format='%.8f')
        print(f'✅ Saved：{output_path}')

    except Exception as e:
        print(f'❌ Error processing data for {year} ：{e}')
#%%
###########               Considering only conversion factors — Dataset construction -MFs
import pandas as pd
import os


folder_path1 = r'../2020-2035Dataset'
folder_path2 = r'../Contribution of interventions/'


columns_to_replace =[
    "synthetic fibers","EF-MW","EF-HW"
]


for year in range(2020, 2036):
  
    reduce_path = os.path.join(folder_path1 , f'MFs_{year}reduce.csv')
    bau_path = os.path.join(folder_path1 , f'MFs_{year}BAU.csv')
    output_path = os.path.join(folder_path2 , f'MFs_{year}reduce1.csv')

    try:
        
        df_reduce = pd.read_csv(reduce_path, encoding="GBK")
        df_bau = pd.read_csv(bau_path, encoding="GBK")

        
        for col in columns_to_replace:
            if col in df_reduce.columns and col in df_bau.columns:
                df_reduce[col] = df_bau[col]
            else:
                print(f'⚠️ {year}: Column "{col}" not found in file, skipping.')
        
       
        df_reduce.to_csv(output_path, index=False, encoding='GBK',float_format='%.8f')
        print(f'✅ Saved：{output_path}')

    except Exception as e:
        print(f'❌ Error processing data for {year} ：{e}')
#%%
###########               Considering conversion factors+ Vehicle — Dataset construction
import pandas as pd
import os


folder_path1 = r'../2020-2035Dataset'
folder_path2 = r'../Contribution of interventions/'


columns_to_replace =[
    "cityroadA", "M1", "ruralroadA", "M2", "highwayA", "M3",
     "cityroadB", "M4", "ruralroadB", "M5", "highwayB", "M6",
    "cityroadC", "M7", "ruralroadC", "M8", "highwayC", "M9",
     "cityroadD", "M10", "ruralroadD", "M11", "highwayD", "M12",
     "cityroadE", "M13", "ruralroadE", "M14", "highwayE", "M15",
    "cityroadF", "M16", "ruralroadF", "M17", "highwayF", "M18","Airplaneinput"
]


for year in range(2020, 2036):
  
    reduce_path = os.path.join(folder_path1 , f'TWP_{year}reduce.csv')
    bau_path = os.path.join(folder_path1 , f'TWP_{year}BAU.csv')
    output_path = os.path.join(folder_path2 , f'TWP_{year}reduce2.csv')

    try:
    
        df_reduce = pd.read_csv(reduce_path, encoding="GBK")
        df_bau = pd.read_csv(bau_path, encoding="GBK")

      
        for col in columns_to_replace:
            if col in df_reduce.columns and col in df_bau.columns:
                df_reduce[col] = df_bau[col]
            else:
                print(f'⚠️ {year}: Column "{col}" not found in file, skipping.')
        
       
        df_reduce.to_csv(output_path, index=False, encoding='GBK',float_format='%.8f')
        print(f'✅ Saved：{output_path}')

    except Exception as e:
        print(f'❌ Error processing data for {year} ：{e}')
#%%
###########               Considering conversion factors+ Vehicle+ EF — Dataset construction
import pandas as pd
import os


folder_path1 = r'..2020-2035Dataset'
folder_path2 = r'../Contribution of interventions/'


columns_to_replace =[
    "cityroadA", "ruralroadA",  "highwayA", 
     "cityroadB", "ruralroadB", "highwayB", 
    "cityroadC", "ruralroadC",  "highwayC",
     "cityroadD",  "ruralroadD",  "highwayD", 
     "cityroadE",  "ruralroadE","highwayE", 
    "cityroadF", "ruralroadF","highwayF", "Airplaneinput"
]


for year in range(2020, 2036):
  
    reduce_path = os.path.join(folder_path1 , f'TWP_{year}reduce.csv')
    bau_path = os.path.join(folder_path1 , f'TWP_{year}BAU.csv')
    output_path = os.path.join(folder_path2 , f'TWP_{year}reduce3.csv')

    try:
      
        df_reduce = pd.read_csv(reduce_path, encoding="GBK")
        df_bau = pd.read_csv(bau_path, encoding="GBK")

       
        for col in columns_to_replace:
            if col in df_reduce.columns and col in df_bau.columns:
                df_reduce[col] = df_bau[col]
            else:
                print(f'⚠️ {year}: Column "{col}" not found in file, skipping.')
        
       
        df_reduce.to_csv(output_path, index=False, encoding='GBK',float_format='%.8f')
        print(f'✅ Saved：{output_path}')

    except Exception as e:
        print(f'❌ Error processing data for {year} ：{e}')