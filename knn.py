import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sl

dataset = pd.read_csv("iris.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,:4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =  train_test_split(x,y,test_size=0.20)
print(x)
print(y)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)

from sklearn.metrics import  classification_report,confusion_matrix

print(classification_report(y_test,y_pred))
