# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 08:53:28 2025

@author: DELL
"""
import pandas as pd
import warnings
import numpy as np

warnings.filterwarnings('ignore')

data_input = pd.read_csv(r"../TWP_dataset.csv",encoding="GBK")
print(data_input.shape)  

action_columns = ['small1', '城市道路A', 'M1', '农村道路A', 'M2', '高速道路A', 'M3',
                  'medium1', '城市道路B', 'M4', '农村道路B', 'M5', '高速道路B', 'M6',
                  'big1', '城市道路C', 'M7', '农村道路C', 'M8', '高速道路C', 'M9',
                  'small2', '城市道路D', 'M10', '农村道路D', 'M11', '高速道路D', 'M12',
                  'medium2', '城市道路E', 'M13', '农村道路E', 'M14', '高速道路E', 'M15',
                  'big2', '城市道路F', 'M16', '农村道路F', 'M17', '高速道路F', 'M18',
                  '十档人群客车比例', '十档人群货车比例', '飞机input','轮胎合成比例',
                  'TC13', 'TC14','TC15', 'TC1345', 'TC23', 'TC24', 'TC25', 'TC2345', 'TC314', 'TC413', 
                  'TC56','TC57', 'TC58', 'TC59', 'TC56789', 'TC613', 'TC710', 'TC713', 'TC71013','TC810',
                  'TC813', 'TC81013', 'TC910', 'TC913', 'TC91013', 'TC1011', 'TC1012','TC101112', 'TC1114','TC1315', 
                  'TC1316', 'TC131516', 'TC1415','TC1417', 'TC141517', 'TC1516', 'TC1518', 'TC151618', 
                  'RTC13', 'RTC14','RTC15',
                  'RTC23', 'RTC24', 'RTC25',
                  'RTC314', 'RTC413', 
                  'RTC56', 'RTC57', 'RTC58', 'RTC59',
                  'RTC613', 'RTC710', 'RTC713', 'RTC810', 'RTC813', 'RTC910', 'RTC913', 'RTC1011','RTC1012','RTC1114' ,
                  'RTC1315', 'RTC1316', 'RTC1415', 'RTC1417','RTC1516', 'RTC1518']  

action = pd.DataFrame(np.nan, columns=action_columns, index=range(10000))

micro_columns = ['total','BOX1', 'BOX2', 'BOX3', 'BOX4', 'BOX5', 'BOX6', 'BOX7', 'BOX8', 'BOX9', 'BOX10',
                 'BOX11', 'BOX12', 'BOX13', 'BOX14', 'BOX15', 'BOX16', 'BOX17', 'BOX18']

micro = pd.DataFrame(np.nan, columns=micro_columns, index=range(10000))

city_columns = []  

city = pd.DataFrame(np.nan, columns=city_columns, index=range(36))

for i in range(3060):

    action['small1'] = np.random.normal(loc=data_input['small1'][i], scale=0.25 * data_input['small1'][i], size=10000)
    action['城市道路A'] = np.random.normal(loc=data_input['城市道路A'][i], scale=0.28 * data_input['城市道路A'][i], size=10000)
    action['M1'] = np.random.normal(loc=data_input['M1'][i], scale=0.26 * data_input['M1'][i], size=10000)
    action['农村道路A'] = np.random.normal(loc=data_input['农村道路A'][i], scale=0.28 * data_input['农村道路A'][i], size=10000)
    action['M2'] = np.random.normal(loc=data_input['M2'][i], scale=0.26 * data_input['M2'][i], size=10000)
    action['高速道路A'] = np.random.normal(loc=data_input['高速道路A'][i], scale=0.28 * data_input['高速道路A'][i], size=10000)
    action['M3'] = np.random.normal(loc=data_input['M3'][i], scale=0.26 * data_input['M3'][i], size=10000)
    
    action['medium1'] = np.random.normal(loc=data_input['medium1'][i], scale=0.25 * data_input['medium1'][i], size=10000)
    action['城市道路B'] = np.random.normal(loc=data_input['城市道路B'][i], scale=0.28 * data_input['城市道路B'][i], size=10000)
    action['M4'] = np.random.normal(loc=data_input['M4'][i], scale=0.26 * data_input['M4'][i], size=10000)
    action['农村道路B'] = np.random.normal(loc=data_input['农村道路B'][i], scale=0.28 * data_input['农村道路B'][i], size=10000)
    action['M5'] = np.random.normal(loc=data_input['M5'][i], scale=0.26 * data_input['M5'][i], size=10000)
    action['高速道路B'] = np.random.normal(loc=data_input['高速道路B'][i], scale=0.28 * data_input['高速道路B'][i], size=10000)
    action['M6'] = np.random.normal(loc=data_input['M6'][i], scale=0.26 * data_input['M6'][i], size=10000)
    
    action['big1'] = np.random.normal(loc=data_input['big1'][i], scale=0.25 * data_input['big1'][i], size=10000)
    action['城市道路C'] = np.random.normal(loc=data_input['城市道路C'][i], scale=0.28 * data_input['城市道路C'][i], size=10000)
    action['M7'] = np.random.normal(loc=data_input['M7'][i], scale=0.26 * data_input['M7'][i], size=10000)
    action['农村道路C'] = np.random.normal(loc=data_input['农村道路C'][i], scale=0.28 * data_input['农村道路C'][i], size=10000)
    action['M8'] = np.random.normal(loc=data_input['M8'][i], scale=0.26 * data_input['M8'][i], size=10000)
    action['高速道路C'] = np.random.normal(loc=data_input['高速道路C'][i], scale=0.28 * data_input['高速道路C'][i], size=10000)
    action['M9'] = np.random.normal(loc=data_input['M9'][i], scale=0.26 * data_input['M9'][i], size=10000)
    
    action['small2'] = np.random.normal(loc=data_input['small2'][i], scale=0.25 * data_input['small2'][i], size=10000)
    action['城市道路D'] = np.random.normal(loc=data_input['城市道路D'][i], scale=0.28 * data_input['城市道路D'][i], size=10000)
    action['M10'] = np.random.normal(loc=data_input['M10'][i], scale=0.26 * data_input['M10'][i], size=10000)
    action['农村道路D'] = np.random.normal(loc=data_input['农村道路D'][i], scale=0.28 * data_input['农村道路D'][i], size=10000)
    action['M11'] = np.random.normal(loc=data_input['M11'][i], scale=0.26 * data_input['M11'][i], size=10000)
    action['高速道路D'] = np.random.normal(loc=data_input['高速道路D'][i], scale=0.28 * data_input['高速道路D'][i], size=10000)
    action['M12'] = np.random.normal(loc=data_input['M12'][i], scale=0.26 * data_input['M12'][i], size=10000)
    
    action['medium2'] = np.random.normal(loc=data_input['medium2'][i], scale=0.25 * data_input['medium2'][i], size=10000)
    action['城市道路E'] = np.random.normal(loc=data_input['城市道路E'][i], scale=0.28 * data_input['城市道路E'][i], size=10000)
    action['M13'] = np.random.normal(loc=data_input['M13'][i], scale=0.26 * data_input['M13'][i], size=10000)
    action['农村道路E'] = np.random.normal(loc=data_input['农村道路E'][i], scale=0.28 * data_input['农村道路E'][i], size=10000)
    action['M14'] = np.random.normal(loc=data_input['M14'][i], scale=0.26 * data_input['M14'][i], size=10000)
    action['高速道路E'] = np.random.normal(loc=data_input['高速道路E'][i], scale=0.28 * data_input['高速道路E'][i], size=10000)
    action['M15'] = np.random.normal(loc=data_input['M15'][i], scale=0.26 * data_input['M15'][i], size=10000)

    action['big2'] = np.random.normal(loc=data_input['big2'][i], scale=0.25 * data_input['big2'][i], size=10000)
    action['城市道路F'] = np.random.normal(loc=data_input['城市道路F'][i], scale=0.28 * data_input['城市道路F'][i], size=10000)
    action['M16'] = np.random.normal(loc=data_input['M16'][i], scale=0.26 * data_input['M16'][i], size=10000)
    action['农村道路F'] = np.random.normal(loc=data_input['农村道路F'][i], scale=0.28 * data_input['农村道路F'][i], size=10000)
    action['M17'] = np.random.normal(loc=data_input['M17'][i], scale=0.26 * data_input['M17'][i], size=10000)
    action['高速道路F'] = np.random.normal(loc=data_input['高速道路F'][i], scale=0.28 * data_input['高速道路F'][i], size=10000)
    action['M18'] = np.random.normal(loc=data_input['M18'][i], scale=0.26 * data_input['M18'][i], size=10000)
    
    action['small1'][action['small1'] < 0] = 0.0001
    action['城市道路A'][action['城市道路A'] < 0] = 0.0001
    action['M1'][action['M1'] < 0] = 0.0001
    action['农村道路A'][action['农村道路A'] < 0] = 0.0001
    action['M2'][action['M2'] < 0] = 0.0001
    action['高速道路A'][action['高速道路A'] < 0] = 0.0001
    action['M3'][action['M3'] < 0] = 0.0001
    
    action['medium1'][action['medium1'] < 0] = 0.0001
    action['城市道路B'][action['城市道路B'] < 0] = 0.0001
    action['M4'][action['M4'] < 0] = 0.0001
    action['农村道路B'][action['农村道路B'] < 0] = 0.0001
    action['M5'][action['M5'] < 0] = 0.0001
    action['高速道路B'][action['高速道路B'] < 0] = 0.0001
    action['M6'][action['M6'] < 0] = 0.0001
    
    action['big1'][action['big1'] < 0] = 0.0001
    action['城市道路C'][action['城市道路C'] < 0] = 0.0001
    action['M7'][action['M7'] < 0] = 0.0001
    action['农村道路C'][action['农村道路C'] < 0] = 0.0001
    action['M8'][action['M8'] < 0] = 0.0001
    action['高速道路C'][action['高速道路B'] < 0] = 0.0001
    action['M9'][action['M6'] < 0] = 0.0001
    
    action['small2'][action['small2'] < 0] = 0.0001
    action['城市道路D'][action['城市道路D'] < 0] = 0.0001
    action['M10'][action['M10'] < 0] = 0.0001
    action['农村道路D'][action['农村道路D'] < 0] = 0.0001
    action['M11'][action['M11'] < 0] = 0.0001
    action['高速道路D'][action['高速道路D'] < 0] = 0.0001
    action['M12'][action['M12'] < 0] = 0.0001
    
    action['medium2'][action['medium2'] < 0] = 0.0001
    action['城市道路E'][action['城市道路E'] < 0] = 0.0001
    action['M13'][action['M13'] < 0] = 0.0001
    action['农村道路E'][action['农村道路E'] < 0] = 0.0001
    action['M14'][action['M14'] < 0] = 0.0001
    action['高速道路E'][action['高速道路E'] < 0] = 0.0001
    action['M15'][action['M15'] < 0] = 0.0001
    
    action['big2'][action['big2'] < 0] = 0.0001
    action['城市道路F'][action['城市道路F'] < 0] = 0.0001
    action['M16'][action['M16'] < 0] = 0.0001
    action['农村道路F'][action['农村道路F'] < 0] = 0.0001
    action['M17'][action['M17'] < 0] = 0.0001
    action['高速道路F'][action['高速道路F'] < 0] = 0.0001
    action['M18'][action['M18'] < 0] = 0.0001


    action['十档人群客车比例'] = np.random.normal(loc=data_input['十档人群客车比例'][i], scale=0.28 * data_input['十档人群客车比例'][i], size=10000)
    #对生成的随机样本进行检查，如果有任何小于0的值，将其替换为0.0001
    action['十档人群客车比例'][action['十档人群客车比例'] < 0] = 0.0001
    action['十档人群货车比例'] = np.random.normal(loc=data_input['十档人群货车比例'][i], scale=0.28 * data_input['十档人群货车比例'][i], size=10000)
    action['十档人群货车比例'][action['十档人群货车比例'] < 0] = 0.0001
    
    
    action['飞机input'] = np.random.normal(loc=data_input['飞机input'][i], scale=0.28 * data_input['飞机input'][i], size=10000)
    action['飞机input'][action['飞机input'] < 0] = 0.0001
    
    action['轮胎合成比例'] = np.random.normal(loc=data_input['轮胎合成比例'][i], scale=0.11 * data_input['轮胎合成比例'][i], size=10000)
    action['轮胎合成比例'][action['轮胎合成比例'] < 0] = 0.0001
    
    action['TC13'] = np.random.normal(loc=data_input['TC13'][i], scale=0.16* data_input['TC13'][i], size=10000)
    action['TC13'][action['TC13'] < 0] = 0.0001
    action['TC14'] = np.random.normal(loc=data_input['TC14'][i], scale=0.16 * data_input['TC14'][i], size=10000)
    action['TC14'][action['TC14'] < 0] = 0.0001
    action['TC15'] = np.random.normal(loc=data_input['TC15'][i], scale=0.16 * data_input['TC15'][i], size=10000)
    action['TC15'][action['TC15'] < 0] = 0.0001
    action['TC1345'] = 1 / (action['TC13'] + action['TC14'] + action['TC15'])
    action['RTC13'] = action['TC13'] * action['TC1345']
    action['RTC14'] = action['TC14'] * action['TC1345']
    action['RTC15'] = action['TC15'] * action['TC1345']
    
    action['TC23'] = np.random.normal(loc=data_input['TC23'][i], scale=0.16 * data_input['TC23'][i], size=10000)
    action['TC23'][action['TC23'] < 0] = 0.0001
    action['TC24'] = np.random.normal(loc=data_input['TC24'][i], scale=0.16 * data_input['TC24'][i], size=10000)
    action['TC24'][action['TC24'] < 0] = 0.0001
    action['TC25'] = np.random.normal(loc=data_input['TC25'][i], scale=0.16 * data_input['TC25'][i], size=10000)
    action['TC25'][action['TC15'] < 0] = 0.0001
    action['TC2345'] = 1 / (action['TC23'] + action['TC24'] + action['TC25'])
    action['RTC23'] = action['TC23'] * action['TC2345']
    action['RTC24'] = action['TC24'] * action['TC2345']
    action['RTC25'] = action['TC25'] * action['TC2345']
    
    action['TC314'] = np.random.normal(loc=data_input['TC314'][i], scale=0.05 * data_input['TC314'][i], size=10000)
    action['TC314'][action['TC314'] < 0] = 0.0001
    action['RTC314'] = action['TC314']
    action['TC413'] = np.random.normal(loc=data_input['TC413'][i], scale=0.05 * data_input['TC413'][i], size=10000)
    action['TC413'][action['TC413'] < 0] = 0.0001
    action['RTC413'] = action['TC413']
    
    action['TC56'] = np.random.normal(loc=data_input['TC56'][i], scale=0.16 * data_input['TC56'][i], size=10000)
    action['TC56'][action['TC56'] < 0] = 0.0001
    action['TC57'] = np.random.normal(loc=data_input['TC57'][i], scale=0.16 * data_input['TC57'][i], size=10000)
    action['TC57'][action['TC57'] < 0] = 0.0001
    action['TC58'] = np.random.normal(loc=data_input['TC58'][i], scale=0.16 * data_input['TC58'][i], size=10000)
    action['TC58'][action['TC58'] < 0] = 0.0001
    action['TC59'] = np.random.normal(loc=data_input['TC59'][i], scale=0.16 * data_input['TC59'][i], size=10000)
    action['TC59'][action['TC59'] < 0] = 0.0001
    action['TC56789'] = 1 / (action['TC56'] + action['TC57'] + action['TC58'] + action['TC59'])
    action['RTC56'] = action['TC56'] * action['TC56789']
    action['RTC57'] = action['TC57'] * action['TC56789']
    action['RTC58'] = action['TC58'] * action['TC56789']
    action['RTC59'] = action['TC59'] * action['TC56789']
    
    action['TC613'] = np.random.normal(loc=data_input['TC613'][i], scale=0.05 * data_input['TC613'][i], size=10000)
    action['TC613'][action['TC613'] < 0] = 0.0001
    action['RTC613'] = action['TC613']
    
    action['TC710'] = np.random.normal(loc=data_input['TC710'][i], scale=0.16 * data_input['TC710'][i], size=10000)
    action['TC710'][action['TC710'] < 0] = 0.0001
    action['TC713'] = np.random.normal(loc=data_input['TC713'][i], scale=0.16 * data_input['TC713'][i], size=10000)
    action['TC713'][action['TC713'] < 0] = 0.0001
    action['TC71013'] = 1 / (action['TC710'] + action['TC713'])
    action['RTC710'] = action['TC710'] * action['TC71013']
    action['RTC713'] = action['TC713'] * action['TC71013']
    
    action['TC810'] = np.random.normal(loc=data_input['TC810'][i], scale=0.16 * data_input['TC810'][i], size=10000)
    action['TC810'][action['TC810'] < 0] = 0.0001
    action['TC813'] = np.random.normal(loc=data_input['TC813'][i], scale=0.16 * data_input['TC813'][i], size=10000)
    action['TC813'][action['TC813'] < 0] = 0.0001
    action['TC81013'] = 1 / (action['TC810'] + action['TC813'])
    action['RTC810'] = action['TC810'] * action['TC81013']
    action['RTC813'] = action['TC813'] * action['TC81013']
    
    action['TC910'] = np.random.normal(loc=data_input['TC910'][i], scale=0.16 * data_input['TC910'][i], size=10000)
    action['TC910'][action['TC910'] < 0] = 0.0001
    action['TC913'] = np.random.normal(loc=data_input['TC913'][i], scale=0.16 * data_input['TC913'][i], size=10000)
    action['TC913'][action['TC913'] < 0] = 0.0001
    action['TC91013'] = 1 / (action['TC910'] + action['TC913'])
    action['RTC910'] = action['TC910'] * action['TC91013']
    action['RTC913'] = action['TC913'] * action['TC91013']
    
    action['TC1011'] = np.random.normal(loc=data_input['TC1011'][i], scale=0.16 * data_input['TC1011'][i], size=10000)
    action['TC1011'][action['TC1011'] < 0] = 0.0001
    action['TC1012'] = np.random.normal(loc=data_input['TC1012'][i], scale=0.16 * data_input['TC1012'][i], size=10000)
    action['TC1012'][action['TC1012'] < 0] = 0.0001
    action['TC101112'] = 1 / (action['TC1011'] + action['TC1012'] )
    action['RTC1011'] = action['TC1011'] * action['TC101112']
    action['RTC1012'] = action['TC1012'] * action['TC101112']
    
    action['TC1114'] = np.random.normal(loc=data_input['TC1114'][i], scale=0.05 * data_input['TC1114'][i], size=10000)
    action['TC1114'][action['TC1114'] < 0] = 0.0001
    action['RTC1114'] = action['TC1114']
    
    action['TC1315'] = np.random.normal(loc=data_input['TC1315'][i], scale=0.42 * data_input['TC1315'][i], size=10000)
    action['TC1315'][action['TC1315'] < 0] = 0.0001
    action['TC1316'] = np.random.normal(loc=data_input['TC1316'][i], scale=0.42 * data_input['TC1316'][i], size=10000)
    action['TC1316'][action['TC1316'] < 0] = 0.0001
    action['TC131516'] = 1 / (action['TC1315'] + action['TC1316'])
    action['RTC1315'] = action['TC1315'] * action['TC131516']
    action['RTC1316'] = action['TC1316'] * action['TC131516']
    
    action['TC1415'] = np.random.normal(loc=data_input['TC1415'][i], scale=0.46 * data_input['TC1415'][i], size=10000)
    action['TC1415'][action['TC1415'] < 0] = 0.0001
    action['TC1417'] = np.random.normal(loc=data_input['TC1417'][i], scale=0.46 * data_input['TC1417'][i], size=10000)
    action['TC1417'][action['TC1417'] < 0] = 0.0001
    action['TC141517'] = 1 / (action['TC1415'] + action['TC1417'])
    action['RTC1415'] = action['TC1415'] * action['TC141517']
    action['RTC1417'] = action['TC1417'] * action['TC141517']
    
    action['TC1516'] = np.random.normal(loc=data_input['TC1516'][i], scale=0.16 * data_input['TC1516'][i], size=10000)
    action['TC1516'][action['TC1516'] < 0] = 0.0001
    action['TC1518'] = np.random.normal(loc=data_input['TC1518'][i], scale=0.16 * data_input['TC1518'][i], size=10000)
    action['TC1518'][action['TC1518'] < 0] = 0.0001
    action['TC151618'] = 1 / (action['TC1516'] + action['TC1518'])
    action['RTC1516'] = action['TC1516'] * action['TC151618']
    action['RTC1518'] = action['TC1518'] * action['TC151618']
    
    #BOX1—— 汽车轮胎产生的微塑料（单位吨）
    micro['BOX1'] = ((action['small1'] * (action['城市道路A'] * action['M1'] + action['农村道路A'] * action['M2'] + action['高速道路A'] * action['M3'])
                + action['medium1'] * (action['城市道路B'] * action['M4'] + action['农村道路B'] * action['M5'] + action['高速道路B'] * action['M6'])
                + action['big1'] * (action['城市道路C'] * action['M7'] + action['农村道路C'] * action['M8'] + action['高速道路C'] * action['M9'])) * action['轮胎合成比例'] * action['十档人群客车比例'] * 0.00001 
               + (action['small2'] * (action['城市道路D'] * action['M10'] + action['农村道路D'] * action['M11'] + action['高速道路D'] * action['M12'])
                + action['medium2'] * (action['城市道路E'] * action['M13'] + action['农村道路E'] * action['M14'] + action['高速道路E'] * action['M15'])
                + action['big2'] * (action['城市道路F'] * action['M16'] + action['农村道路F'] * action['M17'] + action['高速道路F'] * action['M18']))* action['轮胎合成比例'] * action['十档人群货车比例'] * 0.00001 ) 
    
    
    micro['BOX2'] = action['飞机input']
   
    micro['total'] = micro['BOX1'] + micro['BOX2']
    
    micro['BOX3'] = action['RTC13'] * micro['BOX1'] + action['RTC23'] * micro['BOX2']
    micro['BOX4'] = action['RTC14'] * micro['BOX1'] + action['RTC24'] * micro['BOX2']
    micro['BOX5'] = action['RTC15'] * micro['BOX1'] + action['RTC25'] * micro['BOX2']
    micro['BOX6'] = micro['BOX5'] * action['RTC56']
    micro['BOX7'] = micro['BOX5'] * action['RTC57']
    micro['BOX8'] = micro['BOX5'] * action['RTC58']
    micro['BOX9'] = micro['BOX5'] * action['RTC59']
    micro['BOX10'] = micro['BOX7'] * action['RTC710'] + micro['BOX8'] * action['RTC810'] + micro['BOX9'] * action['RTC910']
    micro['BOX11'] = micro['BOX10'] * action['RTC1011']
    micro['BOX12'] = micro['BOX10'] * action['RTC1012']
    micro['BOX13'] = micro['BOX7'] * action['RTC713'] + micro['BOX8'] * action['RTC813'] + micro['BOX9'] * action['RTC913'] + micro['BOX6'] * action['RTC613'] + micro['BOX4'] * action['RTC413']
    micro['BOX14'] = micro['BOX11'] * action['RTC1114'] + micro['BOX3'] * action['RTC314']
    micro['BOX15'] = micro['BOX13'] * action['RTC1315'] + micro['BOX14'] * action['RTC1415']
    micro['BOX16'] = micro['BOX13'] * action['RTC1316'] + micro['BOX15'] * action['RTC1516']
    micro['BOX17'] = micro['BOX14'] * action['RTC1417']
    micro['BOX18'] = micro['BOX15'] * action['RTC1518']
    
   
    a1 = [np.mean(micro['total']), np.std(micro['total'])]
    a1.extend(np.quantile(micro['total'], [0.05, 0.25, 0.75, 0.95])) 
    
    a2 = [np.mean(micro['BOX1']), np.std(micro['BOX1'])]
    a2.extend(np.quantile(micro['BOX1'], [0.05, 0.25, 0.75, 0.95])) 

    a3 = [np.mean(micro['BOX2']), np.std(micro['BOX2'])]
    a3.extend(np.quantile(micro['BOX2'], [0.05, 0.25, 0.75, 0.95]))

    a4 = [np.mean(micro['BOX16']), np.std(micro['BOX16'])] 
    a4.extend(np.quantile(micro['BOX16'], [0.05, 0.25, 0.75, 0.95]))

    a5 = [np.mean(micro['BOX17']), np.std(micro['BOX17'])] 
    a5.extend(np.quantile(micro['BOX17'], [0.05, 0.25, 0.75, 0.95]))

    a6 = [np.mean(micro['BOX18']), np.std(micro['BOX18'])] 
    a6.extend(np.quantile(micro['BOX18'], [0.05, 0.25, 0.75, 0.95]))

    t = np.concatenate((a1, a2, a3, a4, a5, a6))
    city[i] = t 


city.columns = data_input['city']
city.to_csv("TWP_result.csv", index=True)
