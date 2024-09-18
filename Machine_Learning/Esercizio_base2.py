from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import numpy as np

data = load_iris()

X = data.data
y = data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

predizioni = model.predict(X_test)

prestazioni = accuracy_score(y_test,predizioni)

print("\nAccuratezza: ",prestazioni)

report = classification_report(y_test, predizioni)
print("\\nReport: \n",report)

cm = confusion_matrix(y_test, predizioni)
print("\\nMatrice di confusione: \n",cm)