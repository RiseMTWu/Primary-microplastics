# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 16:20:50 2025

@author: DELL
"""

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')
data_input = pd.read_csv(r"../2019_PMs_dataset.csv",encoding="GBK")
print(data_input.shape) 

para_df = pd.read_csv(r"../PMs_para_score.csv",encoding="GBK")
score_mapping = dict(zip(para_df['Parameters'], para_df['Score']))

action = pd.DataFrame(index=range(10000), columns=['Consumption-yagao', 'Consumption-myl', 'Consumption-msg', 'Consumption-xmn', 'PCPpercent',
                                                   'PPUW-yagao', 'PPUW-myl', 'PPUW-msg', 'PPUW-xmn',
                                                   'PMs-yagao', 'PMs-myl',
                                                   'PMs-msg', 'PMs-xmn', 'EF-yagao', 'EF-myl', 'EF-msg',
                                                   'EF-xmn',
                                                   'TC13', 'TC14', 'TC134',
                                                   'TC23', 'TC24', 'TC25', 'TC2345',
                                                   'TC313', 
                                                   'TC46', 'TC47','TC48', 'TC49', 'TC46789', 
                                                   'TC514', 'TC515','TC516','TC5141516',
                                                   'TC613',
                                                   'TC710', 'TC713', 'TC71013', 
                                                   'TC810','TC813', 'TC81013', 'TC910', 'TC913','TC91013', 
                                                   'TC1011', 'TC1012', 'TC101112',
                                                   'TC1116', 
                                                   'TC1318', 'TC1319','TC131819', 
                                                   'TC1617', 'TC1618', 'TC161718', 'TC1819', 'TC1820','TC181920',
                                                   'RTC13', 'RTC14', 'RTC23', 'RTC24', 'RTC25', 'RTC313',
                                                   'RTC46', 'RTC47', 'RTC48', 'RTC49', 'RTC514', 'RTC515', 'RTC516', 'RTC613', 'RTC710', 'RTC713', 'RTC810', 'RTC813', 
                                                   'RTC910','RTC913', 'RTC1011', 'RTC1012', 'RTC1116', 'RTC1318', 'RTC1319', 'RTC1617', 'RTC1618', 'RTC1819', 'RTC1820']) #86列


micro = pd.DataFrame(np.nan,index=range(10000), columns=range(25))


micro.columns = ['microyagao', 'micromsg', 'microxmn', 'micromyl', 'Input', 'BOX1', 'BOX2', 'BOX3', 
                 'BOX4', 'BOX5', 'BOX6', 'BOX7', 'BOX8', 'BOX9', 'BOX10', 'BOX11', 'BOX12', 'BOX13', 
                 'BOX14', 'BOX15', 'BOX16', 'BOX17', 'BOX18', 'BOX19', 'BOX20']


city = pd.DataFrame(np.nan, index=range(60), columns=[])


for i in range(3060):
    
    action['Consumption-yagao'] = np.random.normal(loc=data_input['Consumption-yagao'][i], scale=score_mapping['Consumption-yagao'] *data_input['Consumption-yagao'][i], size=10000)
    action['Consumption-myl'] = np.random.normal(loc=data_input['Consumption-myl'][i], scale=score_mapping['Consumption-myl']*data_input['Consumption-myl'][i], size=10000)
    action['Consumption-msg'] = np.random.normal(loc=data_input['Consumption-msg'][i], scale=score_mapping['Consumption-msg']*data_input['Consumption-msg'][i], size=10000)
    action['Consumption-xmn'] = np.random.normal(loc=data_input['Consumption-xmn'][i], scale=score_mapping['Consumption-xmn']*data_input['Consumption-xmn'][i], size=10000)
    action['PCPpercent'] = np.random.normal(loc=data_input['PCPpercent'][i], scale=score_mapping['PCPpercent']*data_input['PCPpercent'][i], size=10000)
    action['PPUW-yagao'] = np.random.normal(loc=data_input['PPUW-yagao'][i], scale=score_mapping['PPUW-yagao']*data_input['PPUW-yagao'][i], size=10000)
    action['PPUW-myl'] = np.random.normal(loc=data_input['PPUW-myl'][i], scale=score_mapping['PPUW-myl']*data_input['PPUW-myl'][i], size=10000)
    action['PPUW-msg'] = np.random.normal(loc=data_input['PPUW-msg'][i], scale=score_mapping['PPUW-msg']*data_input['PPUW-msg'][i], size=10000)
    action['PPUW-xmn'] = np.random.normal(loc=data_input['PPUW-xmn'][i], scale=score_mapping['PPUW-xmn']*data_input['PPUW-xmn'][i], size=10000)
    action['PMs-yagao'] = np.random.normal(loc=data_input['PMs-yagao'][i], scale=score_mapping['PMs-yagao']*data_input['PMs-yagao'][i], size=10000)
    action['PMs-myl'] = np.random.normal(loc=data_input['PMs-myl'][i], scale=score_mapping['PMs-myl']*data_input['PMs-myl'][i], size=10000)
    action['PMs-msg'] = np.random.normal(loc=data_input['PMs-msg'][i], scale=score_mapping['PMs-msg']*data_input['PMs-msg'][i], size=10000)
    action['PMs-xmn'] = np.random.normal(loc=data_input['PMs-xmn'][i], scale=score_mapping['PMs-xmn']*data_input['PMs-xmn'][i], size=10000)
    action['EF-yagao'] = np.random.normal(loc=data_input['EF-yagao'][i], scale=score_mapping['EF-yagao']*data_input['EF-yagao'][i], size=10000)
    action['EF-myl'] = np.random.normal(loc=data_input['EF-myl'][i], scale=score_mapping['EF-myl']*data_input['EF-myl'][i], size=10000)
    action['EF-msg'] = np.random.normal(loc=data_input['EF-msg'][i], scale=score_mapping['EF-msg']*data_input['EF-msg'][i], size=10000)
    action['EF-xmn'] = np.random.normal(loc=data_input['EF-xmn'][i], scale=score_mapping['EF-xmn']*data_input['EF-xmn'][i], size=10000)

    action['Consumption-yagao'] = np.where(action['Consumption-yagao'] < 0, 0.0001, action['Consumption-yagao'])
    action['Consumption-myl'] = np.where(action['Consumption-myl'] < 0, 0.0001, action['Consumption-myl'])
    action['Consumption-msg'] = np.where(action['Consumption-msg'] < 0, 0.0001, action['Consumption-msg'])
    action['Consumption-xmn'] = np.where(action['Consumption-xmn'] < 0, 0.0001, action['Consumption-xmn'])
    action['PCPpercent'] = np.where(action['PCPpercent'] < 0, 0.0001, action['PCPpercent'])
    action['PPUW-yagao'] = np.where(action['PPUW-yagao'] < 0, 0.0001, action['PPUW-yagao'])
    action['PPUW-myl'] = np.where(action['PPUW-myl'] < 0, 0.0001, action['PPUW-myl'])
    action['PPUW-msg'] = np.where(action['PPUW-msg'] < 0, 0.0001, action['PPUW-msg'])
    action['PPUW-xmn'] = np.where(action['PPUW-xmn'] < 0, 0.0001, action['PPUW-xmn'])
    action['PMs-yagao'] = np.where(action['PMs-yagao'] < 0, 0.0001, action['PMs-yagao'])
    action['PMs-myl'] = np.where(action['PMs-myl'] < 0, 0.0001, action['PMs-myl'])
    action['PMs-msg'] = np.where(action['PMs-msg'] < 0, 0.0001, action['PMs-msg'])
    action['PMs-xmn'] = np.where(action['PMs-xmn'] < 0, 0.0001, action['PMs-xmn'])
    action['EF-yagao'] = np.where(action['EF-yagao'] < 0, 0.0001, action['EF-yagao'])
    action['EF-myl'] = np.where(action['EF-myl'] < 0, 0.0001, action['EF-myl'])
    action['EF-msg'] = np.where(action['EF-msg'] < 0, 0.0001, action['EF-msg'])
    action['EF-xmn'] = np.where(action['EF-xmn'] < 0, 0.0001, action['EF-xmn'])
    #################################
    action['TC13'] = np.random.normal(loc=data_input['TC13'][i], scale=score_mapping['TC13']*data_input['TC13'][i], size=10000)
    action['TC13'][action['TC13'] < 0] = 0.0001
    action['TC14'] = np.random.normal(loc=data_input['TC14'][i], scale=score_mapping['TC14']*data_input['TC14'][i], size=10000)
    action['TC14'][action['TC14'] < 0] = 0.0001
    action['TC134'] = 1 / (action['TC13'] + action['TC14'])
    action['RTC13'] = action['TC13'] * action['TC134']
    action['RTC14'] = action['TC14'] * action['TC134']
    
    action['TC23'] = np.random.normal(loc=data_input['TC23'][i], scale=score_mapping['TC23']*data_input['TC23'][i], size=10000)
    action['TC23'][action['TC23'] < 0] = 0.0001
    action['TC24'] = np.random.normal(loc=data_input['TC24'][i], scale=score_mapping['TC24']*data_input['TC24'][i], size=10000)
    action['TC24'][action['TC24'] < 0] = 0.0001
    action['TC25'] = np.random.normal(loc=data_input['TC25'][i], scale=score_mapping['TC25']*data_input['TC25'][i], size=10000)
    action['TC25'][action['TC25'] < 0] = 0.0001
    action['TC2345'] = 1 / (action['TC23'] + action['TC24'] + action['TC25'])
    action['RTC23'] = action['TC23'] * action['TC2345']
    action['RTC24'] = action['TC24'] * action['TC2345']
    action['RTC25'] = action['TC25'] * action['TC2345']
    
    action['TC313'] = np.random.normal(loc=data_input['TC313'][i], scale=score_mapping['TC313'] * data_input['TC313'][i], size=10000)
    action['TC313'][action['TC313'] < 0] = 0.0001
    action['RTC313'] = action['TC313']
    
    action['TC46'] = np.random.normal(loc=data_input['TC46'][i], scale=score_mapping['TC46'] *data_input['TC46'][i], size=10000)
    action['TC46'][action['TC46'] < 0] = 0.0001
    action['TC47'] = np.random.normal(loc=data_input['TC47'][i], scale=score_mapping['TC47'] *data_input['TC47'][i], size=10000)
    action['TC47'][action['TC47'] < 0] = 0.0001
    action['TC48'] = np.random.normal(loc=data_input['TC48'][i], scale=score_mapping['TC48']*data_input['TC48'][i], size=10000)
    action['TC48'][action['TC48'] < 0] = 0.0001
    action['TC49'] = np.random.normal(loc=data_input['TC49'][i], scale=score_mapping['TC49']*data_input['TC49'][i], size=10000)
    action['TC49'][action['TC49'] < 0] = 0.0001
    action['TC46789'] = 1 / (action['TC46'] + action['TC47'] + action['TC48'] + action['TC49'])
    action['RTC46'] = action['TC46'] * action['TC46789']
    action['RTC47'] = action['TC47'] * action['TC46789']
    action['RTC48'] = action['TC48'] * action['TC46789']
    action['RTC49'] = action['TC49'] * action['TC46789']
    

    action['TC514'] = np.random.normal(loc=data_input['TC514'][i], scale=score_mapping['TC514']*data_input['TC514'][i], size=10000)
    action['TC514'][action['TC514'] < 0] = 0.0001
    action['TC515'] = np.random.normal(loc=data_input['TC515'][i], scale=score_mapping['TC515']*data_input['TC515'][i], size=10000)
    action['TC515'][action['TC515'] < 0] = 0.0001
    action['TC516'] = np.random.normal(loc=data_input['TC516'][i], scale=score_mapping['TC516']*data_input['TC516'][i], size=10000)
    action['TC516'][action['TC516'] < 0] = 0.0001
    action['TC5141516'] = 1 / (action['TC514'] + action['TC515'] + action['TC516'])
    action['RTC514'] = action['TC514'] * action['TC5141516']
    action['RTC515'] = action['TC515'] * action['TC5141516']
    action['RTC516'] = action['TC516'] * action['TC5141516']
    
    action['TC613'] = np.random.normal(loc=data_input['TC613'][i], scale=score_mapping['TC613'] * data_input['TC613'][i], size=10000)
    action['TC613'][action['TC613'] < 0] = 0.0001
    action['RTC613'] = action['TC613']
    
    action['TC710'] = np.random.normal(loc=data_input['TC710'][i], scale=score_mapping['TC710'] *data_input['TC710'][i], size=10000)
    action['TC710'][action['TC710'] < 0] = 0.0001
    action['TC713'] = np.random.normal(loc=data_input['TC713'][i], scale=score_mapping['TC713'] *data_input['TC713'][i], size=10000)
    action['TC713'][action['TC713'] < 0] = 0.0001
    action['TC71013'] = 1 / (action['TC710'] + action['TC713'])
    action['RTC710'] = action['TC710'] * action['TC71013']
    action['RTC713'] = action['TC713'] * action['TC71013']
    
    action['TC810'] = np.random.normal(loc=data_input['TC810'][i], scale=score_mapping['TC810']*data_input['TC810'][i], size=10000)
    action['TC810'][action['TC810'] < 0] = 0.0001
    action['TC813'] = np.random.normal(loc=data_input['TC813'][i], scale=score_mapping['TC813']*data_input['TC813'][i], size=10000)
    action['TC813'][action['TC813'] < 0] = 0.0001
    action['TC81013'] = 1 / (action['TC810'] + action['TC813'])
    action['RTC810'] = action['TC810'] * action['TC81013']
    action['RTC813'] = action['TC813'] * action['TC81013']
    action['TC910'] = np.random.normal(loc=data_input['TC910'][i], scale=score_mapping['TC910']*data_input['TC910'][i], size=10000)
    action['TC910'][action['TC910'] < 0] = 0.0001
    action['TC913'] = np.random.normal(loc=data_input['TC913'][i], scale=score_mapping['TC913']*data_input['TC913'][i], size=10000)
    action['TC913'][action['TC913'] < 0] = 0.0001
    action['TC91013'] = 1 / (action['TC910'] + action['TC913'])
    action['RTC910'] = action['TC910'] * action['TC91013']
    action['RTC913'] = action['TC913'] * action['TC91013']
    
    action['TC1011'] = np.random.normal(loc=data_input['TC1011'][i], scale=score_mapping['TC1011']*data_input['TC1011'][i], size=10000)
    action['TC1011'][action['TC1011'] < 0] = 0.0001
    action['TC1012'] = np.random.normal(loc=data_input['TC1012'][i], scale=score_mapping['TC1012']*data_input['TC1012'][i], size=10000)
    action['TC1012'][action['TC1012'] < 0] = 0.0001
    action['TC101112'] = 1 / (action['TC1011'] + action['TC1012'])
    action['RTC1011'] = action['TC1011'] * action['TC101112']
    action['RTC1012'] = action['TC1012'] * action['TC101112']
    
    action['TC1116'] = np.random.normal(loc=data_input['TC1116'][i], scale=score_mapping['TC1116']*data_input['TC1116'][i], size=10000)
    action['TC1116'][action['TC1116'] < 0] = 0.0001
    action['RTC1116'] = action['TC1116']
    
    action['TC1318'] = np.random.normal(loc=data_input['TC1318'][i], scale=score_mapping['TC1318']*data_input['TC1318'][i], size=10000)
    action['TC1318'][action['TC1318'] < 0] = 0.0001
    action['TC1319'] = np.random.normal(loc=data_input['TC1319'][i], scale=score_mapping['TC1319']*data_input['TC1319'][i], size=10000)
    action['TC1319'][action['TC1319'] < 0] = 0.0001
    action['TC131819'] = 1 / (action['TC1318'] + action['TC1319'])
    action['RTC1318'] = action['TC1318'] * action['TC131819']
    action['RTC1319'] = action['TC1319'] * action['TC131819']
    
    action['TC1617'] = np.random.normal(loc=data_input['TC1617'][i], scale=score_mapping['TC1617']*data_input['TC1617'][i], size=10000)
    action['TC1617'][action['TC1617'] < 0] = 0.0001
    action['TC1618'] = np.random.normal(loc=data_input['TC1618'][i], scale=score_mapping['TC1618']*data_input['TC1618'][i], size=10000)
    action['TC1618'][action['TC1618'] < 0] = 0.0001
    action['TC161718'] = 1 / (action['TC1617'] + action['TC1618'])
    action['RTC1617'] = action['TC1617'] * action['TC161718']
    action['RTC1618'] = action['TC1618'] * action['TC161718']
    
    action['TC1819'] = np.random.normal(loc=data_input['TC1819'][i], scale=score_mapping['TC1819']*data_input['TC1819'][i], size=10000)
    action['TC1819'][action['TC1819'] < 0] = 0.0001
    action['TC1820'] = np.random.normal(loc=data_input['TC1820'][i], scale=score_mapping['TC1820']*data_input['TC1820'][i], size=10000)
    action['TC1820'][action['TC1820'] < 0] = 0.0001
    action['TC181920'] = 1 / (action['TC1819'] + action['TC1820'])
    action['RTC1819'] = action['TC1819'] * action['TC181920']
    action['RTC1820'] = action['TC1820'] * action['TC181920']
    
    #单位吨
    micro['microyagao'] = action['Consumption-yagao']  * action['PCPpercent'] / action['PPUW-yagao'] * action['PMs-yagao'] * action['EF-yagao'] * 0.1
    micro['micromyl'] = action['Consumption-myl']  * action['PCPpercent'] / action['PPUW-myl'] * action['PMs-myl'] * action['EF-myl'] * 0.1
    micro['micromsg'] = action['Consumption-msg']  * action['PCPpercent'] / action['PPUW-msg'] * action['PMs-msg'] * action['EF-msg'] * 0.1
    micro['microxmn'] = action['Consumption-xmn']  * action['PCPpercent'] / action['PPUW-xmn'] * action['PMs-xmn'] * action['EF-xmn'] * 0.1
    
    micro['Input'] = micro['microyagao'] + micro['micromsg'] + micro['microxmn'] + micro['micromyl']
    #单位吨
    micro['BOX1'] = micro['Input'] * 0.95
    micro['BOX2'] = micro['Input'] * 0.05
    
    micro['BOX3'] = action['RTC13'] * micro['BOX1'] + action['RTC23'] * micro['BOX2']
    micro['BOX4'] = action['RTC14'] * micro['BOX1'] + action['RTC24'] * micro['BOX2']
    micro['BOX5'] = action['RTC25'] * micro['BOX2']
    micro['BOX6'] = micro['BOX4'] * action['RTC46']
    micro['BOX7'] = micro['BOX4'] * action['RTC47']
    micro['BOX8'] = micro['BOX4'] * action['RTC48']
    micro['BOX9'] = micro['BOX4'] * action['RTC49']
    micro['BOX10'] = micro['BOX7'] * action['RTC710'] + micro['BOX8'] * action['RTC810'] + micro['BOX9'] * action['RTC910']
    micro['BOX11'] = micro['BOX10'] * action['RTC1011']
    micro['BOX12'] = micro['BOX10'] * action['RTC1012']
    micro['BOX13'] = micro['BOX7'] * action['RTC713'] + micro['BOX8'] * action['RTC813'] + micro['BOX9'] * action['RTC913'] + micro['BOX6'] * action['RTC613'] + micro['BOX3'] * action['RTC313']
    micro['BOX14'] = micro['BOX5'] * action['RTC514']
    micro['BOX15'] = micro['BOX5'] * action['RTC515']
    micro['BOX16'] = micro['BOX5'] * action['RTC516'] + micro['BOX11'] * action['RTC1116']
    micro['BOX17'] = micro['BOX16'] * action['RTC1617']
    micro['BOX18'] = micro['BOX13'] * action['RTC1318'] + micro['BOX16'] * action['RTC1618']
    micro['BOX19'] = micro['BOX13'] * action['RTC1319'] + micro['BOX18'] * action['RTC1819']
    micro['BOX20'] = micro['BOX18'] * action['RTC1820']
    
    a1 = [np.mean(micro['Input']), np.std(micro['Input'])]
    a1.extend(np.quantile(micro['Input'], [0.05, 0.25, 0.75, 0.95])) 
    
    a2 = [np.mean(micro['BOX1']), np.std(micro['BOX1'])]
    a2.extend(np.quantile(micro['BOX1'], [0.05, 0.25, 0.75, 0.95])) 
    
    a3 = [np.mean(micro['BOX2']), np.std(micro['BOX2'])]
    a3.extend(np.quantile(micro['BOX2'], [0.05, 0.25, 0.75, 0.95])) 
    
    a4 = [np.mean(micro['microyagao']), np.std(micro['microyagao'])]
    a4.extend(np.quantile(micro['microyagao'], [0.05, 0.25, 0.75, 0.95])) 
    
    a5 = [np.mean(micro['micromyl']), np.std(micro['micromyl'])]
    a5.extend(np.quantile(micro['micromyl'], [0.05, 0.25, 0.75, 0.95])) 
    
    a6 = [np.mean(micro['micromsg']), np.std(micro['micromsg'])]
    a6.extend(np.quantile(micro['micromsg'], [0.05, 0.25, 0.75, 0.95])) 
    
    a7 = [np.mean(micro['microxmn']), np.std(micro['microxmn'])]
    a7.extend(np.quantile(micro['microxmn'], [0.05, 0.25, 0.75, 0.95])) 
    
    a8 = [np.mean(micro['BOX17']), np.std(micro['BOX17'])]
    a8.extend(np.quantile(micro['BOX17'], [0.05, 0.25, 0.75, 0.95])) 
    
    a9 = [np.mean(micro['BOX19']), np.std(micro['BOX19'])]
    a9.extend(np.quantile(micro['BOX19'], [0.05, 0.25, 0.75, 0.95])) 
    
    a10 = [np.mean(micro['BOX20']), np.std(micro['BOX20'])]
    a10.extend(np.quantile(micro['BOX20'], [0.05, 0.25, 0.75, 0.95])) 

    
    t = np.concatenate([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10])
    city[i] = t 


city.columns = data_input['City']
city.to_csv("../2019_PMs_result.csv", index=True)  
