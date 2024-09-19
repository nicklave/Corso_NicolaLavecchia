import numpy as np
import pandas as pd

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from scipy.stats import randint as sp_randint
from scipy.stats import uniform

data = load_wine()

#print(data['DESCR'])

class ModelloConPipeline:

    def __init__(self):
        self.X = None
        self.Y = None
    
    def caricamento_dati(self):

        self.data = load_wine()
        self.X = self.data.data
        self.y = self.data.target

        return self.X, self.y

    def divisione_dati(self):
        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.3,random_state=42)

        return self.X_train,self.X_test,self.y_train,self.y_test

    def pipeline(self):
        self.pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA()),
        ('gbc', GradientBoostingClassifier(random_state=42))
        ])

        return self.pipeline
    
    def distribuzione_parametri(self):
        self.paramametri = {
        'pca__n_components': np.random.randint(5, 13, size=10),
        'gbc__n_estimators': np.random.randint(50, 200, size=10),
        'gbc__learning_rate': np.random.uniform(0.01, 0.21, size=10),
        'gbc__max_depth': np.random.randint(1, 5, size=10),
        'gbc__subsample': np.random.uniform(0.6, 1, size=10),
        'gbc__min_samples_split': np.random.randint(2, 10, size=10),
        'gbc__min_samples_leaf': np.random.randint(1, 10, size=10),
        'gbc__max_features': ['auto', 'sqrt', 'log2', None]
        }

        return self.paramametri
    
    def modello(self):

        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

        self.random_search = RandomizedSearchCV(
            self.pipeline, param_distributions=self.paramametri, n_iter=50, cv=cv,
            scoring='accuracy', random_state=42, n_jobs=-1)

        self.random_search.fit(self.X_train,self.y_train)
        self.predizione = self.random_search.predict(self.X_test)

        return self.predizione
    
    def score(self):
        try:
            self.accuracy = accuracy_score(self.y_test,self.predizione)

            return self.accuracy
        except:
            print("Non hai ancora eseguito il modello!")
    
    def performance(self):

        try:
            self.report = classification_report(self.y_test,self.predizione)
            self.matrice = confusion_matrix(self.y_test,self.predizione)

            return self.report, self.matrice
        except:
            print("Non hai ancora eseguito il modello!")
    

    def visualizzazione_dati(self):

        df = pd.DataFrame(data=self.X, columns=self.data.feature_names)
        df['target'] = self.y

        print(f"Visualizzo le prime 5 righe del dataset Wine:\n {df.head()}")

        print()
        print(f"Migliori parametri trovati tramite RandomizedSearch: {self.random_search.best_params_}")

        print(f"\nL'accuratezza del modello è {self.accuracy}")

        print(f"Classification report:\n {self.report}")
        print(f"\nMatrice di confusione:\n {self.matrice}")

modello = ModelloConPipeline()
modello.caricamento_dati()
modello.divisione_dati()
modello.pipeline()
modello.distribuzione_parametri()
modello.modello()
modello.score()
modello.performance()
modello.distribuzione_parametri()