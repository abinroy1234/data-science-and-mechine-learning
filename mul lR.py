import numpy as np
import pandas as pd
import matplotlib as plt
advertising=pd.read_csv('Company_data.csv')
advertising.head()
advertising.describe()
advertising.info()
x=advertising.iloc[:,:1]
print(x)
y=advertising.iloc[:,-1]
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_train)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
print(regressor.intercept_)
print(regressor.coef_)
y_pred=regressor.predict(x_test)
for(i,j) in zip(y_test,y_pred):
 if i!=j:
  print("Actual value:",i,"predicted value:",j)
  print("Number of mislabeled points from test data set",(y_test!=y_pred).sum())
