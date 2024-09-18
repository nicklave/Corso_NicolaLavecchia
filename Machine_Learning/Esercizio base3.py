from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
import pandas as pd

data = load_wine()

#print(data['DESCR'])

class ModelloWine:

    def __init__(self):
        self.X = None
        self.Y = None
    
    def caricamento_dati(self):

        self.data = load_wine()
        self.X = self.data.data
        self.y = self.data.target

        return self.X, self.y

    def standardizzazione(self):
        stdX = StandardScaler().fit_transform(self.X)

        return stdX
    
    def divisione_dati(self):
        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.3,random_state=42)

        return self.X_train,self.X_test,self.y_train,self.y_test
    
    def modello(self):
        clf = DecisionTreeClassifier()
        clf.fit(self.X_train,self.y_train)
        self.predizione = clf.predict(self.X_test)

        return self.predizione
    
    def score(self):
        try:
            self.accuracy = accuracy_score(self.y_test,self.predizione)
            self.mse = mean_squared_error(self.y_test,self.predizione)

            return self.accuracy,self.mse
        except:
            print("Non hai ancora eseguito il modello!")
    
    def performance(self):

        try:
            self.report = classification_report(self.y_test,self.predizione)
            self.matrice = confusion_matrix(self.y_test,self.predizione)
            self.cross_validation = cross_val_score(DecisionTreeClassifier(),self.X_train,self.y_train,cv=5)

            return self.report, self.matrice
        except:
            print("Non hai ancora eseguito il modello!")

    def visualizzazione_dati(self):


        df = pd.DataFrame(data=self.X, columns=self.data.feature_names)
        df['target'] = self.y

        print(f"Visualizzo le prime 5 righe del dataset Wine:\n {df.head()}")


        print(f"\nL'accuratezza del modello è {self.accuracy}")
        print(f"\nL'errore quadratico medio del modello è {self.mse}")

        print(f"Classification report:\n {self.report}")
        print(f"\nMatrice di confusione:\n {self.matrice}")
        print(f"\nCross validation:\n {self.cross_validation}")


modello = ModelloWine()
modello.caricamento_dati()
modello.standardizzazione()
modello.divisione_dati()
modello.modello()
modello.score()
modello.performance()

