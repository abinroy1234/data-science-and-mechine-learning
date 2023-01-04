import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
student = pd.read_csv('student_scores.csv')
student.head()
x = student.iloc[:, :-1]
y = student.iloc[:, 1]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
y_pred = regressor.predict(x_test)
for (i, j) in zip(y_test, y_pred):
    if i != j:
     print("Actual value:", i, "predicted value:", j)
     print("Number of mislabeled points from test data set", (y_test !=
y_pred).sum())
from sklearn import metrics
print(("Mean absolute error:", metrics.mean_absolute_error(y_test,
y_pred)))
print("Mean squared error:", metrics.mean_squared_error(y_test, y_pred))
print("RootMeansquarederror:",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
