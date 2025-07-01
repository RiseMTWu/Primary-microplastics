# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 19:03:32 2025

@author: DELL
"""
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=Warning)
from sklearn.ensemble import RandomForestRegressor


data_train = np.genfromtxt('training-480.csv' ,encoding='utf-8',delimiter=',')
data_test = np.genfromtxt('testing-438.csv' ,encoding='utf-8',delimiter=',')
print(data_train.shape)
print(data_test.shape)

x_point = data_train[:,1:-1]
y_point = data_train[:,-1]

x_test= data_test[:,1:]

RF = RandomForestRegressor()
RF.fit(x_point, y_point)

y_point_pred = RF.predict(x_point)
R2_train = r2_score(y_point,y_point_pred)
print(R2_train)
y_testing_pred=RF.predict(x_test)
