import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics,tree
from sklearn.model_selection import train_test_split

data = pd.read_csv("car.csv",names=["buying" ,'maint', 'doors', 'persons', 'lug_boot', 'safety',
'class'])

print(data.head())
data.info()

data['class'],class_names=pd.factorize(data['class'])
print(class_names)
print(data['class'].unique())

data['buying'] = pd.factorize(data['buying'])
data['maint'] = pd.factorize(data['maint'])
data['doors'] = pd.factorize(data['doors'])
data['persons'] = pd.factorize(data['persons'])
data['lug_boot'] = pd.factorize(data['lug_boot'])
data['safety'] = pd.factorize(data['safety'])

x = data.iloc[:,:-1]
y=data.iloc[:,:1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
dtree=tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
dtree.fit(x_train,y_train)
y_pred=dtree.predict(x_test)

count_misclassified = (y_test != y_pred).sum()
print("misclassified_count: {}\n".format(count_misclassified))
accuracy=metrics.accuracy_score(y_test,y_pred)
print("accuracy: \n {:.2f}".format(accuracy))
