from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Iris:
    def __init__(self):
        self.X, self.y = self.caricamento_dati()

    def caricamento(self):

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

        self.model = KNeighborsClassifier(n_neighbors=5)
        self.model.fit(self.X_train, self.y_train)
        self.predizioni = self.model.predict(self.X_test)
        return self.predizioni

    def report(self):
            
        report = classification_report(self.y_test, self.predizioni)
        cm = confusion_matrix(self.y_test, self.predizioni)

        print("Classification Report:")
        print(report)

        plt.figure(figsize=(10,8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Matrice di Confusione')
        plt.xlabel('Predizione')
        plt.ylabel('Vero Valore')
        plt.show()

        return report


ml = Iris()
ml.standardizzazione()
ml.split_test()
ml.modello()
ml.report()