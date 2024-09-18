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

    def caricamento_dati(self):

        data = load_iris()
        X = data.data
        y = data.target
        return X, y

    def standardizzazione(self):

        scaler = StandardScaler()
        self.X_scaled = scaler.fit_transform(self.X)
        return self.X_scaled

    def split_test(self):

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_scaled, self.y, test_size=0.3, random_state=42)
        return self.X_train, self.X_test, self.y_train, self.y_test

    def modello(self):

        self.model = DecisionTreeClassifier()
        self.model.fit(self.X_train, self.y_train)
        self.predizioni = self.model.predict(self.X_test)
        return self.predizioni

    def report(self):
  
        try:
            report = classification_report(self.y_test, self.predizioni)
            cm = confusion_matrix(self.y_test, self.predizioni)

            print("Classification Report:")
            print(report)
            print("Confusion Matrix:")
            print(cm)

            return report, cm

        except:
            print("Il modello non è stato eseguito. Esegui il metodo 'modello' prima di 'report'.")


        

ml_model = ModelloML()
ml_model.standardizzazione()
ml_model.split_test()
#ml_model.modello()
ml_model.report()


