# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:35:24 2024

@author: DELL
"""
#######################################       TWP
import pandas as pd
import warnings
import numpy as np

warnings.filterwarnings('ignore')

for year in range(2020, 2036):
    print(year)
    filename = f'../TWP_{year}BAU.csv'
    #filename = f'TWP_{year}reduce.csv'
    data_input = pd.read_csv(filename, encoding="GBK")

    print(data_input.shape)  
    
    para_df = pd.read_csv(r"../TWP_para_score.csv",encoding="GBK")
    score_mapping = dict(zip(para_df['Parameters'], para_df['Score']))

    action_columns = ['small1', 'cityroadA', 'M1', 'ruralroadA', 'M2', 'highwayA', 'M3',
                  'medium1', 'cityroadB', 'M4', 'ruralroadB', 'M5', 'highwayB', 'M6',
                  'big1', 'cityroadC', 'M7', 'ruralroadC', 'M8', 'highwayC', 'M9',
                  'small2', 'cityroadD', 'M10', 'ruralroadD', 'M11', 'highwayD', 'M12',
                  'medium2', 'cityroadE', 'M13', 'ruralroadE', 'M14', 'highwayE', 'M15',
                  'big2', 'cityroadF', 'M16', 'ruralroadF', 'M17', 'highwayF', 'M18',
                  'Airplaneinput','TCR',
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

        action['small1'] = np.random.normal(loc=data_input['small1'][i], scale=score_mapping['small1'] * data_input['small1'][i], size=10000)
        action['cityroadA'] = np.random.normal(loc=data_input['cityroadA'][i], scale=score_mapping['cityroadA']  * data_input['cityroadA'][i], size=10000)
        action['M1'] = np.random.normal(loc=data_input['M1'][i], scale=score_mapping['M1'] * data_input['M1'][i], size=10000)
        action['ruralroadA'] = np.random.normal(loc=data_input['ruralroadA'][i], scale=score_mapping['ruralroadA']  * data_input['ruralroadA'][i], size=10000)
        action['M2'] = np.random.normal(loc=data_input['M2'][i], scale= score_mapping['M2'] * data_input['M2'][i], size=10000)
        action['highwayA'] = np.random.normal(loc=data_input['highwayA'][i], scale=score_mapping['highwayA']  * data_input['highwayA'][i], size=10000)
        action['M3'] = np.random.normal(loc=data_input['M3'][i], scale=score_mapping['M3']  * data_input['M3'][i], size=10000)
        
        action['medium1'] = np.random.normal(loc=data_input['medium1'][i], scale=score_mapping['medium1'] * data_input['medium1'][i], size=10000)
        action['cityroadB'] = np.random.normal(loc=data_input['cityroadB'][i], scale=score_mapping['cityroadB'] * data_input['cityroadB'][i], size=10000)
        action['M4'] = np.random.normal(loc=data_input['M4'][i], scale=score_mapping['M4'] * data_input['M4'][i], size=10000)
        action['ruralroadB'] = np.random.normal(loc=data_input['ruralroadB'][i], scale=score_mapping['ruralroadB'] * data_input['ruralroadB'][i], size=10000)
        action['M5'] = np.random.normal(loc=data_input['M5'][i], scale=score_mapping['M5'] * data_input['M5'][i], size=10000)
        action['highwayB'] = np.random.normal(loc=data_input['highwayB'][i], scale=score_mapping['highwayB'] * data_input['highwayB'][i], size=10000)
        action['M6'] = np.random.normal(loc=data_input['M6'][i], scale=score_mapping['M6'] * data_input['M6'][i], size=10000)
        
        action['big1'] = np.random.normal(loc=data_input['big1'][i], scale=score_mapping['big1'] * data_input['big1'][i], size=10000)
        action['cityroadC'] = np.random.normal(loc=data_input['cityroadC'][i], scale=score_mapping['cityroadC'] * data_input['cityroadC'][i], size=10000)
        action['M7'] = np.random.normal(loc=data_input['M7'][i], scale=score_mapping['M7'] * data_input['M7'][i], size=10000)
        action['ruralroadC'] = np.random.normal(loc=data_input['ruralroadC'][i], scale=score_mapping['ruralroadC'] * data_input['ruralroadC'][i], size=10000)
        action['M8'] = np.random.normal(loc=data_input['M8'][i], scale=score_mapping['M8'] * data_input['M8'][i], size=10000)
        action['highwayC'] = np.random.normal(loc=data_input['highwayC'][i], scale=score_mapping['highwayC'] * data_input['highwayC'][i], size=10000)
        action['M9'] = np.random.normal(loc=data_input['M9'][i], scale=score_mapping['M9'] * data_input['M9'][i], size=10000)
        
        action['small2'] = np.random.normal(loc=data_input['small2'][i], scale=score_mapping['small2'] * data_input['small2'][i], size=10000)
        action['cityroadD'] = np.random.normal(loc=data_input['cityroadD'][i], scale=score_mapping['cityroadD']  * data_input['cityroadD'][i], size=10000)
        action['M10'] = np.random.normal(loc=data_input['M10'][i], scale=score_mapping['M10'] * data_input['M10'][i], size=10000)
        action['ruralroadD'] = np.random.normal(loc=data_input['ruralroadD'][i], scale=score_mapping['ruralroadD'] * data_input['ruralroadD'][i], size=10000)
        action['M11'] = np.random.normal(loc=data_input['M11'][i], scale=score_mapping['M11'] * data_input['M11'][i], size=10000)
        action['highwayD'] = np.random.normal(loc=data_input['highwayD'][i], scale=score_mapping['highwayD'] * data_input['highwayD'][i], size=10000)
        action['M12'] = np.random.normal(loc=data_input['M12'][i], scale=score_mapping['M12'] * data_input['M12'][i], size=10000)
        
        action['medium2'] = np.random.normal(loc=data_input['medium2'][i], scale=score_mapping['medium2'] * data_input['medium2'][i], size=10000)
        action['cityroadE'] = np.random.normal(loc=data_input['cityroadE'][i], scale=score_mapping['cityroadE'] * data_input['cityroadE'][i], size=10000)
        action['M13'] = np.random.normal(loc=data_input['M13'][i], scale=score_mapping['M13'] * data_input['M13'][i], size=10000)
        action['ruralroadE'] = np.random.normal(loc=data_input['ruralroadE'][i], scale=score_mapping['ruralroadE'] * data_input['ruralroadE'][i], size=10000)
        action['M14'] = np.random.normal(loc=data_input['M14'][i], scale=score_mapping['M14'] * data_input['M14'][i], size=10000)
        action['highwayE'] = np.random.normal(loc=data_input['highwayE'][i], scale=score_mapping['highwayE']* data_input['highwayE'][i], size=10000)
        action['M15'] = np.random.normal(loc=data_input['M15'][i], scale=score_mapping['M15'] * data_input['M15'][i], size=10000)
    
        action['big2'] = np.random.normal(loc=data_input['big2'][i], scale=score_mapping['big2'] * data_input['big2'][i], size=10000)
        action['cityroadF'] = np.random.normal(loc=data_input['cityroadF'][i], scale=score_mapping['cityroadF'] * data_input['cityroadF'][i], size=10000)
        action['M16'] = np.random.normal(loc=data_input['M16'][i], scale=score_mapping['M16'] * data_input['M16'][i], size=10000)
        action['ruralroadF'] = np.random.normal(loc=data_input['ruralroadF'][i], scale=score_mapping['ruralroadF'] * data_input['ruralroadF'][i], size=10000)
        action['M17'] = np.random.normal(loc=data_input['M17'][i], scale=score_mapping['M17'] * data_input['M17'][i], size=10000)
        action['highwayF'] = np.random.normal(loc=data_input['highwayF'][i], scale=score_mapping['highwayF'] * data_input['highwayF'][i], size=10000)
        action['M18'] = np.random.normal(loc=data_input['M18'][i], scale=score_mapping['M18'] * data_input['M18'][i], size=10000)
        
        action['small1'][action['small1'] < 0] = 0.0001
        action['cityroadA'][action['cityroadA'] < 0] = 0.0001
        action['M1'][action['M1'] < 0] = 0.0001
        action['ruralroadA'][action['ruralroadA'] < 0] = 0.0001
        action['M2'][action['M2'] < 0] = 0.0001
        action['highwayA'][action['highwayA'] < 0] = 0.0001
        action['M3'][action['M3'] < 0] = 0.0001
        
        action['medium1'][action['medium1'] < 0] = 0.0001
        action['cityroadB'][action['cityroadB'] < 0] = 0.0001
        action['M4'][action['M4'] < 0] = 0.0001
        action['ruralroadB'][action['ruralroadB'] < 0] = 0.0001
        action['M5'][action['M5'] < 0] = 0.0001
        action['highwayB'][action['highwayB'] < 0] = 0.0001
        action['M6'][action['M6'] < 0] = 0.0001
        
        action['big1'][action['big1'] < 0] = 0.0001
        action['cityroadC'][action['cityroadC'] < 0] = 0.0001
        action['M7'][action['M7'] < 0] = 0.0001
        action['ruralroadC'][action['ruralroadC'] < 0] = 0.0001
        action['M8'][action['M8'] < 0] = 0.0001
        action['highwayC'][action['highwayC'] < 0] = 0.0001
        action['M9'][action['M6'] < 0] = 0.0001
        
        action['small2'][action['small2'] < 0] = 0.0001
        action['cityroadD'][action['cityroadD'] < 0] = 0.0001
        action['M10'][action['M10'] < 0] = 0.0001
        action['ruralroadD'][action['ruralroadD'] < 0] = 0.0001
        action['M11'][action['M11'] < 0] = 0.0001
        action['highwayD'][action['highwayD'] < 0] = 0.0001
        action['M12'][action['M12'] < 0] = 0.0001
        
        action['medium2'][action['medium2'] < 0] = 0.0001
        action['cityroadE'][action['cityroadE'] < 0] = 0.0001
        action['M13'][action['M13'] < 0] = 0.0001
        action['ruralroadE'][action['ruralroadE'] < 0] = 0.0001
        action['M14'][action['M14'] < 0] = 0.0001
        action['highwayE'][action['highwayE'] < 0] = 0.0001
        action['M15'][action['M15'] < 0] = 0.0001
        
        action['big2'][action['big2'] < 0] = 0.0001
        action['cityroadF'][action['cityroadF'] < 0] = 0.0001
        action['M16'][action['M16'] < 0] = 0.0001
        action['ruralroadF'][action['ruralroadF'] < 0] = 0.0001
        action['M17'][action['M17'] < 0] = 0.0001
        action['highwayF'][action['highwayF'] < 0] = 0.0001
        action['M18'][action['M18'] < 0] = 0.0001
    
        
        action['Airplaneinput'] = np.random.normal(loc=data_input['Airplaneinput'][i], scale=score_mapping['Airplaneinput'] * data_input['Airplaneinput'][i], size=10000)
        action['Airplaneinput'][action['Airplaneinput'] < 0] = 0.0001
        
        action['TCR'] = np.random.normal(loc=data_input['TCR'][i], scale=score_mapping['TCR'] * data_input['TCR'][i], size=10000)
        action['TCR'][action['TCR'] < 0] = 0.0001
        
        action['TC13'] = np.random.normal(loc=data_input['TC13'][i], scale=score_mapping['TC13']* data_input['TC13'][i], size=10000)
        action['TC13'][action['TC13'] < 0] = 0.0001
        action['TC14'] = np.random.normal(loc=data_input['TC14'][i], scale=score_mapping['TC14'] * data_input['TC14'][i], size=10000)
        action['TC14'][action['TC14'] < 0] = 0.0001
        action['TC15'] = np.random.normal(loc=data_input['TC15'][i], scale=score_mapping['TC15'] * data_input['TC15'][i], size=10000)
        action['TC15'][action['TC15'] < 0] = 0.0001
        action['TC1345'] = 1 / (action['TC13'] + action['TC14'] + action['TC15'])
        action['RTC13'] = action['TC13'] * action['TC1345']
        action['RTC14'] = action['TC14'] * action['TC1345']
        action['RTC15'] = action['TC15'] * action['TC1345']
        
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
        
        #BOX1—— Vehicle TWP（t）
        micro['BOX1'] = ((action['small1'] * (action['cityroadA'] * action['M1'] + action['ruralroadA'] * action['M2'] + action['highwayA'] * action['M3'])
                    + action['medium1'] * (action['cityroadB'] * action['M4'] + action['ruralroadB'] * action['M5'] + action['highwayB'] * action['M6'])
                    + action['big1'] * (action['cityroadC'] * action['M7'] + action['ruralroadC'] * action['M8'] + action['highwayC'] * action['M9'])) * action['TCR']  * 0.00001 
                   + (action['small2'] * (action['cityroadD'] * action['M10'] + action['ruralroadD'] * action['M11'] + action['highwayD'] * action['M12'])
                    + action['medium2'] * (action['cityroadE'] * action['M13'] + action['ruralroadE'] * action['M14'] + action['highwayE'] * action['M15'])
                    + action['big2'] * (action['cityroadF'] * action['M16'] + action['ruralroadF'] * action['M17'] + action['highwayF'] * action['M18']))* action['TCR'] * 0.00001 ) 
        
        
        micro['BOX2'] = action['Airplaneinput']
       
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
        a1.extend(np.quantile(micro['total'], [0.05, 0.25, 0.75, 0.95]))  #TWP
        
        a2 = [np.mean(micro['BOX1']), np.std(micro['BOX1'])]
        a2.extend(np.quantile(micro['BOX1'], [0.05, 0.25, 0.75, 0.95])) # Vehicle TWP（t）
    
        a3 = [np.mean(micro['BOX2']), np.std(micro['BOX2'])]
        a3.extend(np.quantile(micro['BOX2'], [0.05, 0.25, 0.75, 0.95])) # Airplane TWP（t）
    
        a4 = [np.mean(micro['BOX16']), np.std(micro['BOX16'])] 
        a4.extend(np.quantile(micro['BOX16'], [0.05, 0.25, 0.75, 0.95])) #Ocean
    
        a5 = [np.mean(micro['BOX17']), np.std(micro['BOX17'])] 
        a5.extend(np.quantile(micro['BOX17'], [0.05, 0.25, 0.75, 0.95])) #Soil
    
        a6 = [np.mean(micro['BOX18']), np.std(micro['BOX18'])] 
        a6.extend(np.quantile(micro['BOX18'], [0.05, 0.25, 0.75, 0.95])) #Riber
    
        t = np.concatenate((a1, a2, a3, a4, a5, a6))
        city[i] = t 
    
    
    city.columns = data_input['City']
    city.to_csv("../TWP_{year}result_BAU.csv", index=True)  
   # city.to_csv("../TWP_{year}result_reduce.csv", index=True) 
#%%
#######################################  MFs
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

for year in range(2020, 2036):
    print(year)
    
    filename = f'../MFs_{year}BAU.csv'
    # filename = f'../MFs_{year}reduce.csv'
    data_input = pd.read_csv(filename, encoding="GBK")
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
    city.to_csv("../MFs_{year}result_BAU.csv", index=True)     
    #city.to_csv("../MFs_{year}result_reduce.csv", index=True)  