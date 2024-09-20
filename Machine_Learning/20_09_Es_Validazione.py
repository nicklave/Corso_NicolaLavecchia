from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV,KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,classification_report
from sklearn.pipeline import Pipeline
from scipy.stats import randint,uniform
import pandas as pd

wine = load_wine()
x = wine.data
y = wine.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

pipeline = Pipeline([
    ('Scaler', StandardScaler()),
    ('Rfc' , RandomForestClassifier())
])

parametri = {
    'Rfc__n_estimators' : [100,110,120],
    'Rfc__max_depth' : [3],
    'Rfc__max_features': ['auto', 'sqrt', 'log2', None]
}

cv = KFold(n_splits=5, shuffle=True, random_state=42)

modello = GridSearchCV(pipeline,param_grid = parametri, cv=cv,
    scoring='accuracy', n_jobs=-1)



modello.fit(x_train,y_train)
best = modello.best_estimator_
predizione = best.predict(x_test)

accuracy = accuracy_score(y_test,predizione)
precisione = precision_score(y_test,predizione, average='weighted')
cr = classification_report(y_test,predizione)
matrice = confusion_matrix(y_test,predizione)

df = pd.DataFrame(data=x, columns=wine.feature_names)
df['target'] = y

print(f"Visualizzo le prime 5 righe del dataset Wine:\n {df.head()}")

print()

for parametro,valore in modello.best_params_.items():
    print(f"Miglior valore per il parametro {parametro} è {valore}")

print(f"\nL'accuratezza del modello è {accuracy}")
print(f"\nLa precisione del modello è {precisione}")

print(f"Classification report:\n {cr}")
print(f"\nMatrice di confusione:\n {matrice}")


