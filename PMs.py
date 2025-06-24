# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 15:21:54 2024

@author: lenovo
"""

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')
data_input = pd.read_csv(r"../2019_PMs_dataset.csv",encoding="GBK")
print(data_input) 
action = pd.DataFrame(index=range(10000), columns=['牙膏消费', '沐浴露消费', '磨砂膏消费', '洗面奶消费', '十档人群占比',
                                                   '牙膏单位重量价格', '沐浴露单位重量价格', '磨砂膏单位重量价格', '洗面奶单位重量价格',
                                                   '含有塑料微粒的牙膏百分比', '含有塑料微粒的沐浴露百分比',
                                                   '含有塑料微粒的磨砂膏百分比', '含有塑料微粒的洗面奶百分比', '牙膏排放因子', '沐浴露排放因子', '磨砂膏排放因子',
                                                   '洗面奶排放因子',
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
    
    action['牙膏消费'] = np.random.normal(loc=data_input['牙膏消费'][i], scale=0.15*data_input['牙膏消费'][i], size=10000)
    action['沐浴露消费'] = np.random.normal(loc=data_input['沐浴露消费'][i], scale=0.15*data_input['沐浴露消费'][i], size=10000)
    action['磨砂膏消费'] = np.random.normal(loc=data_input['磨砂膏消费'][i], scale=0.15*data_input['磨砂膏消费'][i], size=10000)
    action['洗面奶消费'] = np.random.normal(loc=data_input['洗面奶消费'][i], scale=0.15*data_input['洗面奶消费'][i], size=10000)
    action['十档人群占比'] = np.random.normal(loc=data_input['十档人群占比'][i], scale=0.15*data_input['十档人群占比'][i], size=10000)
    action['牙膏单位重量价格'] = np.random.normal(loc=data_input['牙膏单位重量价格'][i], scale=0.15*data_input['牙膏单位重量价格'][i], size=10000)
    action['沐浴露单位重量价格'] = np.random.normal(loc=data_input['沐浴露单位重量价格'][i], scale=0.15*data_input['沐浴露单位重量价格'][i], size=10000)
    action['磨砂膏单位重量价格'] = np.random.normal(loc=data_input['磨砂膏单位重量价格'][i], scale=0.15*data_input['磨砂膏单位重量价格'][i], size=10000)
    action['洗面奶单位重量价格'] = np.random.normal(loc=data_input['洗面奶单位重量价格'][i], scale=0.15*data_input['洗面奶单位重量价格'][i], size=10000)
    action['含有塑料微粒的牙膏百分比'] = np.random.normal(loc=data_input['含有塑料微粒的牙膏百分比'][i], scale=0.13*data_input['含有塑料微粒的牙膏百分比'][i], size=10000)
    action['含有塑料微粒的沐浴露百分比'] = np.random.normal(loc=data_input['含有塑料微粒的沐浴露百分比'][i], scale=0.13*data_input['含有塑料微粒的沐浴露百分比'][i], size=10000)
    action['含有塑料微粒的磨砂膏百分比'] = np.random.normal(loc=data_input['含有塑料微粒的磨砂膏百分比'][i], scale=0.13*data_input['含有塑料微粒的磨砂膏百分比'][i], size=10000)
    action['含有塑料微粒的洗面奶百分比'] = np.random.normal(loc=data_input['含有塑料微粒的洗面奶百分比'][i], scale=0.13*data_input['含有塑料微粒的洗面奶百分比'][i], size=10000)
    action['牙膏排放因子'] = np.random.normal(loc=data_input['牙膏排放因子'][i], scale=0.13*data_input['牙膏排放因子'][i], size=10000)
    action['沐浴露排放因子'] = np.random.normal(loc=data_input['沐浴露排放因子'][i], scale=0.13*data_input['沐浴露排放因子'][i], size=10000)
    action['磨砂膏排放因子'] = np.random.normal(loc=data_input['磨砂膏排放因子'][i], scale=0.13*data_input['磨砂膏排放因子'][i], size=10000)
    action['洗面奶排放因子'] = np.random.normal(loc=data_input['洗面奶排放因子'][i], scale=0.13*data_input['洗面奶排放因子'][i], size=10000)

    action['牙膏消费'] = np.where(action['牙膏消费'] < 0, 0.0001, action['牙膏消费'])
    action['沐浴露消费'] = np.where(action['沐浴露消费'] < 0, 0.0001, action['沐浴露消费'])
    action['磨砂膏消费'] = np.where(action['磨砂膏消费'] < 0, 0.0001, action['磨砂膏消费'])
    action['洗面奶消费'] = np.where(action['洗面奶消费'] < 0, 0.0001, action['洗面奶消费'])
    action['十档人群占比'] = np.where(action['十档人群占比'] < 0, 0.0001, action['十档人群占比'])
    action['牙膏单位重量价格'] = np.where(action['牙膏单位重量价格'] < 0, 0.0001, action['牙膏单位重量价格'])
    action['沐浴露单位重量价格'] = np.where(action['沐浴露单位重量价格'] < 0, 0.0001, action['沐浴露单位重量价格'])
    action['磨砂膏单位重量价格'] = np.where(action['磨砂膏单位重量价格'] < 0, 0.0001, action['磨砂膏单位重量价格'])
    action['洗面奶单位重量价格'] = np.where(action['洗面奶单位重量价格'] < 0, 0.0001, action['洗面奶单位重量价格'])
    action['含有塑料微粒的牙膏百分比'] = np.where(action['含有塑料微粒的牙膏百分比'] < 0, 0.0001, action['含有塑料微粒的牙膏百分比'])
    action['含有塑料微粒的沐浴露百分比'] = np.where(action['含有塑料微粒的沐浴露百分比'] < 0, 0.0001, action['含有塑料微粒的沐浴露百分比'])
    action['含有塑料微粒的磨砂膏百分比'] = np.where(action['含有塑料微粒的磨砂膏百分比'] < 0, 0.0001, action['含有塑料微粒的磨砂膏百分比'])
    action['含有塑料微粒的洗面奶百分比'] = np.where(action['含有塑料微粒的洗面奶百分比'] < 0, 0.0001, action['含有塑料微粒的洗面奶百分比'])
    action['牙膏排放因子'] = np.where(action['牙膏排放因子'] < 0, 0.0001, action['牙膏排放因子'])
    action['沐浴露排放因子'] = np.where(action['沐浴露排放因子'] < 0, 0.0001, action['沐浴露排放因子'])
    action['磨砂膏排放因子'] = np.where(action['磨砂膏排放因子'] < 0, 0.0001, action['磨砂膏排放因子'])
    action['洗面奶排放因子'] = np.where(action['洗面奶排放因子'] < 0, 0.0001, action['洗面奶排放因子'])
    #################################
    action['TC13'] = np.random.normal(loc=data_input['TC13'][i], scale=0.43*data_input['TC13'][i], size=10000)
    action['TC13'][action['TC13'] < 0] = 0.0001
    action['TC14'] = np.random.normal(loc=data_input['TC14'][i], scale=0.43*data_input['TC14'][i], size=10000)
    action['TC14'][action['TC14'] < 0] = 0.0001
    action['TC134'] = 1 / (action['TC13'] + action['TC14'])
    action['RTC13'] = action['TC13'] * action['TC134']
    action['RTC14'] = action['TC14'] * action['TC134']
    
    action['TC23'] = np.random.normal(loc=data_input['TC23'][i], scale=0.43*data_input['TC23'][i], size=10000)
    action['TC23'][action['TC23'] < 0] = 0.0001
    action['TC24'] = np.random.normal(loc=data_input['TC24'][i], scale=0.43*data_input['TC24'][i], size=10000)
    action['TC24'][action['TC24'] < 0] = 0.0001
    action['TC25'] = np.random.normal(loc=data_input['TC25'][i], scale=0.43*data_input['TC25'][i], size=10000)
    action['TC25'][action['TC25'] < 0] = 0.0001
    action['TC2345'] = 1 / (action['TC23'] + action['TC24'] + action['TC25'])
    action['RTC23'] = action['TC23'] * action['TC2345']
    action['RTC24'] = action['TC24'] * action['TC2345']
    action['RTC25'] = action['TC25'] * action['TC2345']
    
    action['TC313'] = np.random.normal(loc=data_input['TC313'][i], scale=0.05 * data_input['TC313'][i], size=10000)
    action['TC313'][action['TC313'] < 0] = 0.0001
    action['RTC313'] = action['TC313']
    
    action['TC46'] = np.random.normal(loc=data_input['TC46'][i], scale=0.16*data_input['TC46'][i], size=10000)
    action['TC46'][action['TC46'] < 0] = 0.0001
    action['TC47'] = np.random.normal(loc=data_input['TC47'][i], scale=0.16*data_input['TC47'][i], size=10000)
    action['TC47'][action['TC47'] < 0] = 0.0001
    action['TC48'] = np.random.normal(loc=data_input['TC48'][i], scale=0.16*data_input['TC48'][i], size=10000)
    action['TC48'][action['TC48'] < 0] = 0.0001
    action['TC49'] = np.random.normal(loc=data_input['TC49'][i], scale=0.16*data_input['TC49'][i], size=10000)
    action['TC49'][action['TC49'] < 0] = 0.0001
    action['TC46789'] = 1 / (action['TC46'] + action['TC47'] + action['TC48'] + action['TC49'])
    action['RTC46'] = action['TC46'] * action['TC46789']
    action['RTC47'] = action['TC47'] * action['TC46789']
    action['RTC48'] = action['TC48'] * action['TC46789']
    action['RTC49'] = action['TC49'] * action['TC46789']
    

    action['TC514'] = np.random.normal(loc=data_input['TC514'][i], scale=0.1*data_input['TC514'][i], size=10000)
    action['TC514'][action['TC514'] < 0] = 0.0001
    action['TC515'] = np.random.normal(loc=data_input['TC515'][i], scale=0.1*data_input['TC515'][i], size=10000)
    action['TC515'][action['TC515'] < 0] = 0.0001
    action['TC516'] = np.random.normal(loc=data_input['TC516'][i], scale=0.1*data_input['TC516'][i], size=10000)
    action['TC516'][action['TC516'] < 0] = 0.0001
    action['TC5141516'] = 1 / (action['TC514'] + action['TC515'] + action['TC516'])
    action['RTC514'] = action['TC514'] * action['TC5141516']
    action['RTC515'] = action['TC515'] * action['TC5141516']
    action['RTC516'] = action['TC516'] * action['TC5141516']
    
    action['TC613'] = np.random.normal(loc=data_input['TC613'][i], scale=0.05 * data_input['TC613'][i], size=10000)
    action['TC613'][action['TC613'] < 0] = 0.0001
    action['RTC613'] = action['TC613']
    
    action['TC710'] = np.random.normal(loc=data_input['TC710'][i], scale=0.16*data_input['TC710'][i], size=10000)
    action['TC710'][action['TC710'] < 0] = 0.0001
    action['TC713'] = np.random.normal(loc=data_input['TC713'][i], scale=0.16*data_input['TC713'][i], size=10000)
    action['TC713'][action['TC713'] < 0] = 0.0001
    action['TC71013'] = 1 / (action['TC710'] + action['TC713'])
    action['RTC710'] = action['TC710'] * action['TC71013']
    action['RTC713'] = action['TC713'] * action['TC71013']
    
    action['TC810'] = np.random.normal(loc=data_input['TC810'][i], scale=0.16*data_input['TC810'][i], size=10000)
    action['TC810'][action['TC810'] < 0] = 0.0001
    action['TC813'] = np.random.normal(loc=data_input['TC813'][i], scale=0.16*data_input['TC813'][i], size=10000)
    action['TC813'][action['TC813'] < 0] = 0.0001
    action['TC81013'] = 1 / (action['TC810'] + action['TC813'])
    action['RTC810'] = action['TC810'] * action['TC81013']
    action['RTC813'] = action['TC813'] * action['TC81013']
    action['TC910'] = np.random.normal(loc=data_input['TC910'][i], scale=0.16*data_input['TC910'][i], size=10000)
    action['TC910'][action['TC910'] < 0] = 0.0001
    action['TC913'] = np.random.normal(loc=data_input['TC913'][i], scale=0.16*data_input['TC913'][i], size=10000)
    action['TC913'][action['TC913'] < 0] = 0.0001
    action['TC91013'] = 1 / (action['TC910'] + action['TC913'])
    action['RTC910'] = action['TC910'] * action['TC91013']
    action['RTC913'] = action['TC913'] * action['TC91013']
    
    action['TC1011'] = np.random.normal(loc=data_input['TC1011'][i], scale=0.16*data_input['TC1011'][i], size=10000)
    action['TC1011'][action['TC1011'] < 0] = 0.0001
    action['TC1012'] = np.random.normal(loc=data_input['TC1012'][i], scale=0.16*data_input['TC1012'][i], size=10000)
    action['TC1012'][action['TC1012'] < 0] = 0.0001
    action['TC101112'] = 1 / (action['TC1011'] + action['TC1012'])
    action['RTC1011'] = action['TC1011'] * action['TC101112']
    action['RTC1012'] = action['TC1012'] * action['TC101112']
    
    action['TC1116'] = np.random.normal(loc=data_input['TC1116'][i], scale=0.05*data_input['TC1116'][i], size=10000)
    action['TC1116'][action['TC1116'] < 0] = 0.0001
    action['RTC1116'] = action['TC1116']
    
    action['TC1318'] = np.random.normal(loc=data_input['TC1318'][i], scale=0.42*data_input['TC1318'][i], size=10000)
    action['TC1318'][action['TC1318'] < 0] = 0.0001
    action['TC1319'] = np.random.normal(loc=data_input['TC1319'][i], scale=0.42*data_input['TC1319'][i], size=10000)
    action['TC1319'][action['TC1319'] < 0] = 0.0001
    action['TC131819'] = 1 / (action['TC1318'] + action['TC1319'])
    action['RTC1318'] = action['TC1318'] * action['TC131819']
    action['RTC1319'] = action['TC1319'] * action['TC131819']
    
    action['TC1617'] = np.random.normal(loc=data_input['TC1617'][i], scale=0.46*data_input['TC1617'][i], size=10000)
    action['TC1617'][action['TC1617'] < 0] = 0.0001
    action['TC1618'] = np.random.normal(loc=data_input['TC1618'][i], scale=0.46*data_input['TC1618'][i], size=10000)
    action['TC1618'][action['TC1618'] < 0] = 0.0001
    action['TC161718'] = 1 / (action['TC1617'] + action['TC1618'])
    action['RTC1617'] = action['TC1617'] * action['TC161718']
    action['RTC1618'] = action['TC1618'] * action['TC161718']
    
    action['TC1819'] = np.random.normal(loc=data_input['TC1819'][i], scale=0.16*data_input['TC1819'][i], size=10000)
    action['TC1819'][action['TC1819'] < 0] = 0.0001
    action['TC1820'] = np.random.normal(loc=data_input['TC1820'][i], scale=0.16*data_input['TC1820'][i], size=10000)
    action['TC1820'][action['TC1820'] < 0] = 0.0001
    action['TC181920'] = 1 / (action['TC1819'] + action['TC1820'])
    action['RTC1819'] = action['TC1819'] * action['TC181920']
    action['RTC1820'] = action['TC1820'] * action['TC181920']
    
    #单位吨
    micro['microyagao'] = action['牙膏消费']  * action['十档人群占比'] / action['牙膏单位重量价格'] * action['含有塑料微粒的牙膏百分比'] * action['牙膏排放因子'] * 0.1
    micro['micromyl'] = action['沐浴露消费']  * action['十档人群占比'] / action['沐浴露单位重量价格'] * action['含有塑料微粒的沐浴露百分比'] * action['沐浴露排放因子'] * 0.1
    micro['micromsg'] = action['磨砂膏消费']  * action['十档人群占比'] / action['磨砂膏单位重量价格'] * action['含有塑料微粒的磨砂膏百分比'] * action['磨砂膏排放因子'] * 0.1
    micro['microxmn'] = action['洗面奶消费']  * action['十档人群占比'] / action['洗面奶单位重量价格'] * action['含有塑料微粒的洗面奶百分比'] * action['洗面奶排放因子'] * 0.1
    
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
    a1.extend(np.quantile(micro['Input'], [0.05, 0.25, 0.75, 0.95])) #PMs总产生量
    
    a2 = [np.mean(micro['BOX1']), np.std(micro['BOX1'])]
    a2.extend(np.quantile(micro['BOX1'], [0.05, 0.25, 0.75, 0.95])) #冲洗掉的PPCP
    
    a3 = [np.mean(micro['BOX2']), np.std(micro['BOX2'])]
    a3.extend(np.quantile(micro['BOX2'], [0.05, 0.25, 0.75, 0.95])) #残留的PPCP
    
    a4 = [np.mean(micro['microyagao']), np.std(micro['microyagao'])]
    a4.extend(np.quantile(micro['microyagao'], [0.05, 0.25, 0.75, 0.95])) #牙膏产生微塑料
    
    a5 = [np.mean(micro['micromyl']), np.std(micro['micromyl'])]
    a5.extend(np.quantile(micro['micromyl'], [0.05, 0.25, 0.75, 0.95])) #沐浴露产生微塑料
    
    a6 = [np.mean(micro['micromsg']), np.std(micro['micromsg'])]
    a6.extend(np.quantile(micro['micromsg'], [0.05, 0.25, 0.75, 0.95])) #磨砂膏产生微塑料
    
    a7 = [np.mean(micro['microxmn']), np.std(micro['microxmn'])]
    a7.extend(np.quantile(micro['microxmn'], [0.05, 0.25, 0.75, 0.95])) #洗面奶产生微塑料
    
    a8 = [np.mean(micro['BOX17']), np.std(micro['BOX17'])]
    a8.extend(np.quantile(micro['BOX17'], [0.05, 0.25, 0.75, 0.95])) #残余土壤污染
    
    a9 = [np.mean(micro['BOX19']), np.std(micro['BOX19'])]
    a9.extend(np.quantile(micro['BOX19'], [0.05, 0.25, 0.75, 0.95])) #海洋污染
    
    a10 = [np.mean(micro['BOX20']), np.std(micro['BOX20'])]
    a10.extend(np.quantile(micro['BOX20'], [0.05, 0.25, 0.75, 0.95])) #残余河流污染

    
    t = np.concatenate([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10])
    city[i] = t 


city.columns = data_input['city']
city.to_csv("PMs_result.csv", index=True)  