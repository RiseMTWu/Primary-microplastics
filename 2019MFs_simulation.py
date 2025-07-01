# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:48:37 2025

@author: DELL
"""

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')
data_input = pd.read_csv(r"../2019_MFs_dataset.csv",encoding="GBK")
print(data_input.shape) 

para_df = pd.read_csv(r"../MFs_para_score.csv",encoding="GBK")
score_mapping = dict(zip(para_df['Parameters'], para_df['Score']))

action = pd.DataFrame(index=range(10000), columns=['population', 'synthetic fibers', 'FrequencyMW', 'FrequencyHW', 'EF-MW',
                                                   'EF-HW', 'Load-MW', 'Load-HW', 
                                                   'TC14', 'TC15', 'TC145',
                                                   'TC23', 'TC24', 'TC25', 'TC2345',
                                                   'TC314', 'TC413',
                                                   'TC56', 'TC57','TC58', 'TC59', 'TC56789',                        
                                                   'TC613',
                                                   'TC710', 'TC713', 'TC71013', 
                                                   'TC810','TC813', 'TC81013', 'TC910', 'TC913','TC91013', 
                                                   'TC1011', 'TC1012', 'TC101112',
                                                   'TC1114', 
                                                   'TC1315', 'TC1316','TC131516', 
                                                   'TC1415', 'TC1417', 'TC141517', 'TC1516', 'TC1518','TC151618',
                                                   'RTC14', 'RTC15', 'RTC23', 'RTC24', 'RTC25', 'RTC314','RTC413',
                                                   'RTC56', 'RTC57', 'RTC58', 'RTC59', 'RTC613', 'RTC710', 'RTC713', 'RTC810', 'RTC813', 'RTC910', 'RTC913',
                                                   'RTC1011', 'RTC1012', 'RTC1114', 'RTC1315', 'RTC1316', 'RTC1415', 'RTC1417', 'RTC1516', 'RTC1518'])

micro = pd.DataFrame(np.nan,index=range(10000), columns=range(19))


micro_columns = ['total','BOX1', 'BOX2', 'BOX3', 'BOX4', 'BOX5', 'BOX6', 'BOX7', 'BOX8', 'BOX9', 'BOX10',
                 'BOX11', 'BOX12', 'BOX13', 'BOX14', 'BOX15', 'BOX16', 'BOX17', 'BOX18']

city = pd.DataFrame(np.nan, index=range(36), columns=[])


for i in range(3060):
    
    action['population'] = np.random.normal(loc=data_input['population'][i], scale=score_mapping['population'] * data_input['population'][i], size=10000)
    action['synthetic fibers'] = np.random.normal(loc=data_input['synthetic fibers'][i], scale=score_mapping['synthetic fibers']*data_input['synthetic fibers'][i], size=10000)
    action['FrequencyMW'] = np.random.normal(loc=data_input['FrequencyMW'][i], scale=score_mapping['FrequencyMW'] * data_input['FrequencyMW'][i], size=10000)
    action['FrequencyHW'] = np.random.normal(loc=data_input['FrequencyHW'][i], scale=score_mapping['FrequencyHW'] * data_input['FrequencyHW'][i], size=10000)
    action['EF-MW'] = np.random.normal(loc=data_input['EF-MW'][i], scale=score_mapping['EF-MW'] * data_input['EF-MW'][i], size=10000)
    action['EF-HW'] = np.random.normal(loc=data_input['EF-HW'][i], scale=score_mapping['EF-HW'] * data_input['EF-HW'][i], size=10000)
    action['Load-MW'] = np.random.normal(loc=data_input['Load-MW'][i], scale=score_mapping['Load-MW'] * data_input['Load-MW'][i], size=10000)
    action['Load-HW'] = np.random.normal(loc=data_input['Load-HW'][i], scale=score_mapping['Load-HW'] * data_input['Load-HW'][i], size=10000)
    
    action['population'][action['population'] < 0] = 0.0001
    action['synthetic fibers'][action['synthetic fibers'] < 0] = 0.0001
    action['FrequencyMW'][action['FrequencyMW'] < 0] = 0.0001
    action['FrequencyHW'][action['FrequencyHW'] < 0] = 0.0001
    action['EF-MW'][action['EF-MW'] < 0] = 0.0001
    action['EF-HW'][action['EF-HW'] < 0] = 0.0001
    action['Load-MW'][action['Load-MW'] < 0] = 0.0001
    action['Load-HW'][action['Load-HW'] < 0] = 0.0001
    
    action['TC14'] = np.random.normal(loc=data_input['TC14'][i], scale=score_mapping['TC14'] * data_input['TC14'][i], size=10000)
    action['TC14'][action['TC14'] < 0] = 0.0001
    action['TC15'] = np.random.normal(loc=data_input['TC15'][i], scale=score_mapping['TC15'] * data_input['TC15'][i], size=10000)
    action['TC15'][action['TC15'] < 0] = 0.0001
    action['TC145'] = 1 / (action['TC14'] + action['TC15'])
    action['RTC14'] = action['TC14'] * action['TC145']
    action['RTC15'] = action['TC15'] * action['TC145']

    
    action['TC23'] = np.random.normal(loc=data_input['TC23'][i], scale=score_mapping['TC23'] * data_input['TC23'][i], size=10000)
    action['TC23'][action['TC23'] < 0] = 0.0001
    action['TC24'] = np.random.normal(loc=data_input['TC24'][i], scale=score_mapping['TC24']  * data_input['TC24'][i], size=10000)
    action['TC24'][action['TC24'] < 0] = 0.0001
    action['TC25'] = np.random.normal(loc=data_input['TC25'][i], scale=score_mapping['TC25']  * data_input['TC25'][i], size=10000)
    action['TC25'][action['TC15'] < 0] = 0.0001
    action['TC2345'] = 1 / (action['TC23'] + action['TC24'] + action['TC25'])
    action['RTC23'] = action['TC23'] * action['TC2345']
    action['RTC24'] = action['TC24'] * action['TC2345']
    action['RTC25'] = action['TC25'] * action['TC2345']
    
    action['TC314'] = np.random.normal(loc=data_input['TC314'][i], scale=score_mapping['TC314'] * data_input['TC314'][i], size=10000)
    action['TC314'][action['TC314'] < 0] = 0.0001
    action['RTC314'] = action['TC314']
    action['TC413'] = np.random.normal(loc=data_input['TC413'][i], scale=score_mapping['TC413']  * data_input['TC413'][i], size=10000)
    action['TC413'][action['TC413'] < 0] = 0.0001
    action['RTC413'] = action['TC413']
    
    action['TC56'] = np.random.normal(loc=data_input['TC56'][i], scale=score_mapping['TC56'] * data_input['TC56'][i], size=10000)
    action['TC56'][action['TC56'] < 0] = 0.0001
    action['TC57'] = np.random.normal(loc=data_input['TC57'][i], scale=score_mapping['TC57']  * data_input['TC57'][i], size=10000)
    action['TC57'][action['TC57'] < 0] = 0.0001
    action['TC58'] = np.random.normal(loc=data_input['TC58'][i], scale=score_mapping['TC58'] * data_input['TC58'][i], size=10000)
    action['TC58'][action['TC58'] < 0] = 0.0001
    action['TC59'] = np.random.normal(loc=data_input['TC59'][i], scale=score_mapping['TC59']  * data_input['TC59'][i], size=10000)
    action['TC59'][action['TC59'] < 0] = 0.0001
    action['TC56789'] = 1 / (action['TC56'] + action['TC57'] + action['TC58'] + action['TC59'])
    action['RTC56'] = action['TC56'] * action['TC56789']
    action['RTC57'] = action['TC57'] * action['TC56789']
    action['RTC58'] = action['TC58'] * action['TC56789']
    action['RTC59'] = action['TC59'] * action['TC56789']
    
    action['TC613'] = np.random.normal(loc=data_input['TC613'][i], scale=score_mapping['TC613']  * data_input['TC613'][i], size=10000)
    action['TC613'][action['TC613'] < 0] = 0.0001
    action['RTC613'] = action['TC613']
    
    action['TC710'] = np.random.normal(loc=data_input['TC710'][i], scale=score_mapping['TC710'] * data_input['TC710'][i], size=10000)
    action['TC710'][action['TC710'] < 0] = 0.0001
    action['TC713'] = np.random.normal(loc=data_input['TC713'][i], scale=score_mapping['TC713'] * data_input['TC713'][i], size=10000)
    action['TC713'][action['TC713'] < 0] = 0.0001
    action['TC71013'] = 1 / (action['TC710'] + action['TC713'])
    action['RTC710'] = action['TC710'] * action['TC71013']
    action['RTC713'] = action['TC713'] * action['TC71013']
    
    action['TC810'] = np.random.normal(loc=data_input['TC810'][i], scale=score_mapping['TC810'] * data_input['TC810'][i], size=10000)
    action['TC810'][action['TC810'] < 0] = 0.0001
    action['TC813'] = np.random.normal(loc=data_input['TC813'][i], scale=score_mapping['TC813'] * data_input['TC813'][i], size=10000)
    action['TC813'][action['TC813'] < 0] = 0.0001
    action['TC81013'] = 1 / (action['TC810'] + action['TC813'])
    action['RTC810'] = action['TC810'] * action['TC81013']
    action['RTC813'] = action['TC813'] * action['TC81013']
    
    action['TC910'] = np.random.normal(loc=data_input['TC910'][i], scale=score_mapping['TC910'] * data_input['TC910'][i], size=10000)
    action['TC910'][action['TC910'] < 0] = 0.0001
    action['TC913'] = np.random.normal(loc=data_input['TC913'][i], scale=score_mapping['TC913'] * data_input['TC913'][i], size=10000)
    action['TC913'][action['TC913'] < 0] = 0.0001
    action['TC91013'] = 1 / (action['TC910'] + action['TC913'])
    action['RTC910'] = action['TC910'] * action['TC91013']
    action['RTC913'] = action['TC913'] * action['TC91013']
    
    action['TC1011'] = np.random.normal(loc=data_input['TC1011'][i], scale=score_mapping['TC1011'] * data_input['TC1011'][i], size=10000)
    action['TC1011'][action['TC1011'] < 0] = 0.0001
    action['TC1012'] = np.random.normal(loc=data_input['TC1012'][i], scale=score_mapping['TC1012'] * data_input['TC1012'][i], size=10000)
    action['TC1012'][action['TC1012'] < 0] = 0.0001
    action['TC101112'] = 1 / (action['TC1011'] + action['TC1012'] )
    action['RTC1011'] = action['TC1011'] * action['TC101112']
    action['RTC1012'] = action['TC1012'] * action['TC101112']
    
    action['TC1114'] = np.random.normal(loc=data_input['TC1114'][i], scale=score_mapping['TC1114'] * data_input['TC1114'][i], size=10000)
    action['TC1114'][action['TC1114'] < 0] = 0.0001
    action['RTC1114'] = action['TC1114']
    
    action['TC1315'] = np.random.normal(loc=data_input['TC1315'][i], scale=score_mapping['TC1315']  * data_input['TC1315'][i], size=10000)
    action['TC1315'][action['TC1315'] < 0] = 0.0001
    action['TC1316'] = np.random.normal(loc=data_input['TC1316'][i], scale=score_mapping['TC1316'] * data_input['TC1316'][i], size=10000)
    action['TC1316'][action['TC1316'] < 0] = 0.0001
    action['TC131516'] = 1 / (action['TC1315'] + action['TC1316'])
    action['RTC1315'] = action['TC1315'] * action['TC131516']
    action['RTC1316'] = action['TC1316'] * action['TC131516']
    
    action['TC1415'] = np.random.normal(loc=data_input['TC1415'][i], scale=score_mapping['TC1415'] * data_input['TC1415'][i], size=10000)
    action['TC1415'][action['TC1415'] < 0] = 0.0001
    action['TC1417'] = np.random.normal(loc=data_input['TC1417'][i], scale=score_mapping['TC1417'] * data_input['TC1417'][i], size=10000)
    action['TC1417'][action['TC1417'] < 0] = 0.0001
    action['TC141517'] = 1 / (action['TC1415'] + action['TC1417'])
    action['RTC1415'] = action['TC1415'] * action['TC141517']
    action['RTC1417'] = action['TC1417'] * action['TC141517']
    
    action['TC1516'] = np.random.normal(loc=data_input['TC1516'][i], scale=score_mapping['TC1516'] * data_input['TC1516'][i], size=10000)
    action['TC1516'][action['TC1516'] < 0] = 0.0001
    action['TC1518'] = np.random.normal(loc=data_input['TC1518'][i], scale=score_mapping['TC1518'] * data_input['TC1518'][i], size=10000)
    action['TC1518'][action['TC1518'] < 0] = 0.0001
    action['TC151618'] = 1 / (action['TC1516'] + action['TC1518'])
    action['RTC1516'] = action['TC1516'] * action['TC151618']
    action['RTC1518'] = action['TC1518'] * action['TC151618']
    

    micro['BOX1'] = action['population'] * action['synthetic fibers'] * action['FrequencyMW']* action['Load-MW']* action['EF-MW']*0.00001
    micro['BOX2'] = action['population'] * action['synthetic fibers'] * action['FrequencyHW']* action['Load-HW']* action['EF-HW']*0.00001
   
    micro['total'] =micro['BOX1']+ micro['BOX2'] 
    
    micro['BOX3'] = action['RTC23'] * micro['BOX2']
    micro['BOX4'] = action['RTC14'] * micro['BOX1'] + action['RTC24'] * micro['BOX2']
    micro['BOX5'] = action['RTC15'] * micro['BOX1'] + action['RTC25'] * micro['BOX2']
    micro['BOX6'] = micro['BOX5'] * action['RTC56']
    micro['BOX7'] = micro['BOX5'] * action['RTC57']
    micro['BOX8'] = micro['BOX5'] * action['RTC58']
    micro['BOX9'] = micro['BOX5'] * action['RTC59']
    micro['BOX10'] = micro['BOX7'] * action['RTC710'] + micro['BOX8'] * action['RTC810'] + micro['BOX9'] * action['RTC910']
    micro['BOX11'] = micro['BOX10'] * action['RTC1011']
    micro['BOX12'] = micro['BOX10'] * action['RTC1012']
    micro['BOX13'] = micro['BOX4'] * action['RTC413']+ micro['BOX6'] * action['RTC613']+ micro['BOX7'] * action['RTC713'] + micro['BOX8'] * action['RTC813'] + micro['BOX9'] * action['RTC913'] 
    micro['BOX14'] = micro['BOX3'] * action['RTC314']+micro['BOX11'] * action['RTC1114']
    micro['BOX15'] = micro['BOX13'] * action['RTC1315']+micro['BOX14'] * action['RTC1415']
    micro['BOX16'] = micro['BOX13'] * action['RTC1316'] + micro['BOX15'] * action['RTC1516']
    micro['BOX17'] = micro['BOX14'] * action['RTC1417']
    micro['BOX18'] = micro['BOX15'] * action['RTC1518'] 

    
    a1 = [np.mean(micro['total']), np.std(micro['total'])]
    a1.extend(np.quantile(micro['total'], [0.05, 0.25, 0.75, 0.95])) 
    
    a2 = [np.mean(micro['BOX1']), np.std(micro['BOX1'])]
    a2.extend(np.quantile(micro['BOX1'], [0.05, 0.25, 0.75, 0.95]))  #machine washing
    
    a3 = [np.mean(micro['BOX2']), np.std(micro['BOX2'])]
    a3.extend(np.quantile(micro['BOX2'], [0.05, 0.25, 0.75, 0.95])) #hand washing
    
    a4 = [np.mean(micro['BOX16']), np.std(micro['BOX16'])]
    a4.extend(np.quantile(micro['BOX16'], [0.05, 0.25, 0.75, 0.95])) #Ocean
    
    a5 = [np.mean(micro['BOX17']), np.std(micro['BOX17'])]
    a5.extend(np.quantile(micro['BOX17'], [0.05, 0.25, 0.75, 0.95]))   #Soil
    
    a6 = [np.mean(micro['BOX18']), np.std(micro['BOX18'])]
    a6.extend(np.quantile(micro['BOX18'], [0.05, 0.25, 0.75, 0.95]))   #River

    
    t = np.concatenate([a1, a2, a3, a4, a5, a6])
    city[i] = t 


city.columns = data_input['City']
city.to_csv("../2019_MFs_result.csv", index=True)    
