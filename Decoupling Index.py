# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 10:51:10 2025

@author: DELL
"""
import pandas as pd

df = pd.read_excel("../DI_dataset.xlsx")


#  ΔGDP%
df["ΔGDP%"]= (df["GDP_2035"] - df["GDP_2019"]) / df["GDP_2019"]

# ---- 1. BAU scenario----

# DI microplastics total generation
df["DI_GDP_gen_BAU"] = (
     df["ΔGDP%"]-
     ((df["MP_gen_2035_BAU"] - df["MP_gen_2019"]) / df["MP_gen_2019"])
    
) /  df["ΔGDP%"]

# DI microplastics total emission
df["DI_GDP_rel_BAU"] = (
     df["ΔGDP%"]-
    ((df["MP_rel_2035_BAU"] - df["MP_rel_2019"]) / df["MP_rel_2019"])

) /  df["ΔGDP%"]

# ---- 2. Reduce ----

# DI microplastics total generation
df["DI_GDP_gen_Reduce"] = (
     df["ΔGDP%"]-
    ((df["MP_gen_2035_Reduce"] - df["MP_gen_2019"]) / df["MP_gen_2019"])
) /  df["ΔGDP%"]

# DI microplastics total emission
df["DI_GDP_rel_Reduce"] = (
    df["ΔGDP%"]-
    ((df["MP_rel_2035_Reduce"] - df["MP_rel_2019"]) / df["MP_rel_2019"])
    
) /  df["ΔGDP%"]

### Population decoupling index calculation
# Δpopulation%
df["ΔPOP%"] = (df["Pop_2035"] - df["Pop_2019"]) / df["Pop_2019"]

# DI_POP for BAU
df["DI_POP_gen_BAU"] = (
    df["ΔPOP%"]-
    ((df["MP_gen_2035_BAU"] - df["MP_gen_2019"]) / df["MP_gen_2019"]) 
) / df["ΔPOP%"]

df["DI_POP_rel_BAU"] = (
     df["ΔPOP%"]-
    ((df["MP_rel_2035_BAU"] - df["MP_rel_2019"]) / df["MP_rel_2019"]) 
) / df["ΔPOP%"]

# DI_POP for Reduce
df["DI_POP_gen_Reduce"] = (
     df["ΔPOP%"]-
    ((df["MP_gen_2035_Reduce"] - df["MP_gen_2019"]) / df["MP_gen_2019"]) 
) / df["ΔPOP%"]

df["DI_POP_rel_Reduce"] = (
     df["ΔPOP%"]-
    ((df["MP_rel_2035_Reduce"] - df["MP_rel_2019"]) / df["MP_rel_2019"]) 
) / df["ΔPOP%"]


columns_to_keep = [
    "city",
    "DI_GDP_gen_BAU", "DI_GDP_rel_BAU", "DI_GDP_gen_Reduce", "DI_GDP_rel_Reduce",
    "DI_POP_gen_BAU", "DI_POP_rel_BAU", "DI_POP_gen_Reduce", "DI_POP_rel_Reduce"
]

df_result = df[columns_to_keep]

df_result.to_excel("../DI_result.xlsx", index=False)