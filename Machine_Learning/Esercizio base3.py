from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

data = load_wine()

print(data['DESCR'])


class ModelloWine:

    def __init__(self):
        data = load_wine
        self.X = data.data
        self.Y = data.target
    
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
            accuracy = accuracy_score(self.y_test,self.predizione)
            mse = mean_squared_error(self.y_test,self.predizione)

            print(f"L'accuratezza del modello è {accuracy}")
            print(f"\nL'errore quadratico medio del modello è {mse}")

            return accuracy,mse
        except:
            print("Non hai ancora eseguito il modello!")
    
    def performance(self):

        try:
            report = classification_report(self.y_test,self.predizione)
            matrice = confusion_matrix(self.y,self.predizione)
            cross_validation = cross_val_score(DecisionTreeClassifier(),self.X_train,self.y_train)

            print(f"Classification report:\n {report}")
            print(f"\nMatrice di confusione:\n {matrice}")
            print(f"\nCross validation:\n {cross_validation}")


            return report, matrice
        except:
            print("Non hai ancora eseguito il modello!")



