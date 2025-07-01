# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:02:21 2024

@author: lenovo
"""
#kmeans optimal k value determination method - elbow method

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('cluster-306.csv',encoding="GBK")

features =df.iloc[:,1:]

SSE = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k)  
    kmeans.fit(features)
    SSE.append(kmeans.inertia_) 
X = range(1,11)
plt.xlabel('number of clusters')
plt.ylabel('SSE')
plt.plot(X,SSE,'o-')
plt.show()
print(SSE)
#%%
# Cluster of different city groups
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('Cluster-306.csv',encoding="GBK")

features =df.iloc[:,1:]

# K-means 
kmeans = KMeans(n_clusters=4)
kmeans.fit(features)

df['Cluster'] = kmeans.labels_

cluster_counts = df['Cluster'].value_counts().sort_index()
print(cluster_counts)
