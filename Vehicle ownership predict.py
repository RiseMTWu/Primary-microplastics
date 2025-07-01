# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:09:14 2024

@author: lenovo
"""
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=Warning)
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

data_train = np.genfromtxt('car_ML_train.csv' ,encoding='utf-8',delimiter=',')
data_test = np.genfromtxt('car_ML_test.csv' ,encoding='utf-8',delimiter=',')
print(data_train.shape)
print(data_test.shape)

# 初始化回归模型
models = {
"RandomForest": RandomForestRegressor(),
"XGBoost": XGBRegressor(),
"LinearRegression": LinearRegression(),
"MLPRegressor": MLPRegressor(),
"SVR": SVR()
}

results = []

for i in range(0,20):
    
    #np.random.shuffle(data_train)
   
    x_point = data_train[:,:-1]
    y_point = data_train[:,-1]
    
    Xtrain, Xtest, ytrain, ytest = train_test_split(x_point,y_point,test_size= 0.3)
    
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler() 
    # Xtrain_std = scaler.fit_transform(Xtrain)
    # Xtest_std = scaler.transform(Xtest)
    
    for name, model in models.items():
    

        model.fit(Xtrain, ytrain)
    
        R2_Train = np.mean(cross_val_score(model,  Xtrain, ytrain, cv=5, scoring='r2'))
        MSE_Train = np.mean(cross_val_score(model,  Xtrain, ytrain, cv=5, scoring='neg_mean_squared_error'))
        MAE_Train = np.mean(cross_val_score(model,  Xtrain, ytrain, cv=5, scoring='neg_mean_absolute_error'))
       
    
        y_testing_pred = model.predict(Xtest)
        
  
        R2_Test = r2_score(ytest,y_testing_pred)
        MSE_Test = mean_squared_error(ytest,y_testing_pred)
        MAE_Test = mean_absolute_error(ytest,y_testing_pred)
    
        results.append((name, R2_Train, R2_Test, MSE_Train,MSE_Test,MAE_Train,MAE_Test))


results1 = np.array(results)
#%%
#Hyper-parameters tunning
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=Warning)
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

data_train = np.genfromtxt('car_ML_train.csv' ,encoding='utf-8',delimiter=',')
data_test = np.genfromtxt('car_ML_test.csv' ,encoding='utf-8',delimiter=',')
print(data_train.shape)
print(data_test.shape)

circle=0
result= np.zeros((135,10))

for a in [100,200,500,1000,2000]:
    for b in [5,15,None]:
        for c in [2,8,15]:
            for d in [2,5,7]:

                R2_Trainresult= []
                R2_Testresult=[]
                MSE_Trainresult = []
                MSE_Testresult = []
                MAE_Trainresult = []
                MAE_Testresult = []
                
                print(circle)
                for i in range(0,10):
                    
                    
                    x_point = data_train[:,:-1]
                    y_point = data_train[:,-1]
                    
                    Xtrain, Xtest, ytrain, ytest = train_test_split(x_point,y_point,test_size= 0.3)
                    
                    RF = RandomForestRegressor(n_estimators=a,max_depth=b,
                               min_samples_leaf=c,min_samples_split=d)
                    
                    R2_Train = np.mean(cross_val_score(RF,  Xtrain, ytrain, cv=5, scoring='r2'))
                    MSE_Train = np.mean(cross_val_score(RF,  Xtrain, ytrain, cv=5, scoring='neg_mean_squared_error'))
                    MAE_Train = np.mean(cross_val_score(RF,  Xtrain, ytrain, cv=5, scoring='neg_mean_absolute_error'))
                    
                  
                    MSE_Trainresult.append(MSE_Train)
                    MAE_Trainresult.append(MAE_Train)
                    R2_Trainresult.append(R2_Train)            
                    
                    RF.fit(Xtrain,ytrain)
                    y_testing_pred = RF.predict(Xtest)
                    
                    R2_Test= r2_score(ytest,y_testing_pred)
                    MSE_Test= mean_squared_error(ytest,y_testing_pred)
                    MAE_Test= mean_absolute_error(ytest,y_testing_pred)
                    
                    R2_Testresult.append(R2_Test)
                    MSE_Testresult.append(MSE_Test)
                    MAE_Testresult.append(MAE_Test)



                R2_Train_mean=np.mean(R2_Trainresult)   
                R2_Test_mean=np.mean(R2_Testresult)
                
                MSE_Train_mean=np.mean(MSE_Trainresult)
                MSE_Test_mean=np.mean(MSE_Testresult)
                
                MAE_Train_mean=np.mean(MAE_Trainresult)
                MAE_Test_mean=np.mean(MAE_Testresult)
    
                result[circle,:]=[a,b,c,d,R2_Train_mean, R2_Test_mean,MSE_Train_mean,MSE_Test_mean,MAE_Train_mean,MAE_Test_mean]
        
                circle+=1
                
np.savetxt('result.csv',result,delimiter=',')                   
#%%
#Optimal model determined
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=Warning)
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

data_train = np.genfromtxt('car_ML_train.csv' ,encoding='utf-8',delimiter=',')
data_test = np.genfromtxt('car_ML_test.csv' ,encoding='utf-8',delimiter=',')
print(data_train.shape)
print(data_test.shape)


R2_Trainresult = []
R2_Testresult = []
MSE_Trainresult = []
MSE_Testresult = []
MAE_Trainresult = []
MAE_Testresult = []

for j in range(0,10):
    
    np.random.shuffle(data_train)
   
    x_point = data_train[:,:-1]
    y_point = data_train[:,-1]
    
    Xtrain, Xtest, ytrain, ytest = train_test_split(x_point,y_point,test_size= 0.3)
    
    RF = RandomForestRegressor(n_estimators=200,max_depth=15,
               min_samples_leaf=8,min_samples_split=5)
    
    R2_Train = np.mean(cross_val_score(RF,  Xtrain, ytrain, cv=5, scoring='r2'))
    MSE_Train = np.mean(cross_val_score(RF,  Xtrain, ytrain, cv=5, scoring='neg_mean_squared_error'))
    MAE_Train = np.mean(cross_val_score(RF,  Xtrain, ytrain, cv=5, scoring='neg_mean_absolute_error'))
    
  
    MSE_Trainresult.append(MSE_Train)
    MAE_Trainresult.append(MAE_Train)
    R2_Trainresult.append(R2_Train)            
    
    RF.fit(Xtrain,ytrain)
    y_testing_pred = RF.predict(Xtest)
    
    R2_Test= r2_score(ytest,y_testing_pred)
    MSE_Test= mean_squared_error(ytest,y_testing_pred)
    MAE_Test= mean_absolute_error(ytest,y_testing_pred)
    
    R2_Testresult.append(R2_Test)
    MSE_Testresult.append(MSE_Test)
    MAE_Testresult.append(MAE_Test)

print(" ****************     R2           Training:")    
print(np.mean(R2_Trainresult))
print("*****************     R2            Testing:")    
print(np.mean(R2_Testresult))
print(" ****************     MSE           Training:")   
print(np.mean(MSE_Trainresult))
print("*****************     MSE            Testing:")
print(np.mean(MSE_Testresult))
print(" ****************     MAE           Training:")    
print(np.mean(MAE_Trainresult))
print("*****************     MAE            Testing:")    
print(np.mean(MAE_Testresult))
#%%
#Vehicle ownership predict
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=Warning)

from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

data_train = np.genfromtxt('../car_ML_train.csv' ,encoding='utf-8',delimiter=',')
data_test = np.genfromtxt('../car_ML_test.csv' ,encoding='utf-8',delimiter=',')
print(data_train.shape)
print(data_test.shape)

x_point = data_train[:,:-1]
y_point = data_train[:,-1]

x_test= data_test[:,:]

RF = RandomForestRegressor(n_estimators=200,max_depth=15,min_samples_leaf=8,min_samples_split=5)

RF.fit(x_point, y_point)

y_point_pred = RF.predict(x_point)
R2_train = r2_score(y_point,y_point_pred)
print(R2_train)
y_testing_pred=RF.predict(x_test)