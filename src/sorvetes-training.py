#import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#load dataset sorvetes.csv
print("Loading dataset...")
data = pd.read_csv("sorvetes.csv")

#split dataset into features and labels
X, y = sorvetes[['Temperatura']].values, sorvetes['Vendas'].values

#split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#set regularization hyperparameter
reg = 0.01

#train a logistic regression model
print('Training a logistic regression model with regularization rate of', reg)
model = LogisticRegression(C=1/reg, solver='liblinear').fit(X__train, y_train)

#calculate accuracy
y_hat = model.predict(X_test)
acc = np.avarage(y_hat == y_test)
print('Accuracy is', acc)

#calculate AUC
y_scores = model.predict_proba(X_test)
auc = roc_auc_score(y_test, y_scores[:,1])
print('AUC: ' + str(auc))
