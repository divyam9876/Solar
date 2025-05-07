import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import explained_variance_score,r2_score, mean_squared_error
from google.colab import files
uploaded = files.upload()
df=pd.read_csv('combined_data')
X=df[['Year','Month','Day','Hour','DNI','DHI','Temperature','Relative Humidity','Wind Speed']]
y=df['GHI']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model=RandomForestRegressor(n_estimators=100,random_state=42)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(explained_variance_score(y_test,y_pred))
efficiency=0.18
df['power_per_m2']=efficiency*df['GHI']
y1=df['power_per_m2']
X_train, X_test, y_train_power, y_test_power = train_test_split(X, y1, test_size=0.2, random_state=42)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train_power)
y_pred_power = rf.predict(X_test)
print(explained_variance_score(y_test_power,y_pred_power))
print("R² Score:", r2_score(y_test_power, y_pred_power))
print("MSE:", mean_squared_error(y_test_power, y_pred_power))
