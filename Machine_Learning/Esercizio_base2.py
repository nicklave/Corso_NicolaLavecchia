from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import numpy as np

class ModelloML:

    def __init__(self):

        self.X, self.y = self.caricamento_dati()
        self.X_scaled = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.predizioni = None
        self.model = None

    def caricamento_dati():
        data = load_iris()

        X = data.data
        y = data.target

        return X,y

    def standardizzazione(X):
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        return X_scaled


    def split_test(X,y):
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

        return X_train,X_test,y_train,y_test


    def modello(X_train,X_test,y_train,y_test):
        model = DecisionTreeClassifier()
        model.fit(X_train,y_train)

        predizioni = model.predict(X_test)

        prestazioni = accuracy_score(y_test,predizioni)


    def report(y_test,predizioni):
        report = classification_report(y_test, predizioni)
        cm = confusion_matrix(y_test, predizioni)


