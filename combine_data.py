import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


files=[
    'Solar/Dataset/2020.csv',
    'Solar/Dataset/2021.csv',
    'Solar/Dataset/2022.csv',
    'Solar/Dataset/2023.csv'
]
df=[pd.read_csv(file,skiprows=2) for file in files]
combined=pd.concat(df,ignore_index=True)

combined.to_csv('combined_data',index=False)
print('Combined Successfully')X=combined[['Year','Month','Day','Hour','DNI','DHI','Temperature','Relative Humidity','Wind Speed']]
y=combined['GHI']
print(X.isnull().sum())
print(y.isnull().sum())
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
