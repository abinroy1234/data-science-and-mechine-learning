import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
data=pd.read_csv("iris.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,4].values
data.head(5)
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
classifier=GaussianNB()
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
print(y_pred)
cm=confusion_matrix(y_test,y_pred)
print("Accuracy :",accuracy_score(y_test,y_pred))
print("array",cm)
df=pd.DataFrame({'Real Values':y_test,'predicted values':y_pred})
print(df)
