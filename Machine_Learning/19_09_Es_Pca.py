import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

digits = load_digits()
X = digits.data
y = digits.target

df = pd.DataFrame(X, columns=digits.feature_names)
df['Target'] = y

#print(f"Head del dataframe \n {df.head()}\n")

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

pca2 = PCA(n_components=4)
X_pca2 = pca2.fit_transform(X)

# Calcola la percentuale di varianza spiegata dalle prime due componenti principali
varianza_spiegata = pca2.explained_variance_ratio_

var_totale = np.sum(varianza_spiegata)

# Visualizza la percentuale di variabilità spiegata
print(f"Percentuale di varianza spiegata dalla prima componente: {varianza_spiegata[0] * 100:.2f}%")
print(f"Percentuale di varianza spiegata dalla seconda componente: {varianza_spiegata[1] * 100:.2f}%")
print(f"Percentuale di varianza spiegata dalla terza componente: {varianza_spiegata[2] * 100:.2f}%")
print(f"Percentuale di varianza spiegata dalla quarta componente: {varianza_spiegata[3] * 100:.2f}%")

# Visualizza l'andamento della varianza spiegata cumulativa
# varianza_cumulata = np.cumsum(varianza_spiegata)
print(f"Varianza cumulata spiegata dalle prime 4 componenti: {var_totale * 100:.2f}%")

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', s=50, edgecolor='k')
plt.colorbar(scatter)
plt.title('Visualizzazione delle cifre nel nuovo spazio (PCA - 2 Componenti)')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy_original = accuracy_score(y_test, y_pred)
print(f"Accuratezza con dati originali (64 dimensioni): {accuracy_original:.2f}")


# Trasforma i dati di training e test con PCA a 2 componenti
X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y, test_size=0.3, random_state=42)

# Addestra e valuta il modello sui dati ridotti a 2 componenti
model_pca = LogisticRegression(max_iter=10000)
model_pca.fit(X_train_pca, y_train_pca)
y_pred_pca = model_pca.predict(X_test_pca)
accuracy_pca = accuracy_score(y_test_pca, y_pred_pca)
print(f"Accuratezza con dati ridotti (PCA - 2 dimensioni): {accuracy_pca:.2f}")

# Trasforma i dati di training e test con PCA a 4 componenti
X_train_pca2, X_test_pca2, y_train_pca2, y_test_pca2 = train_test_split(X_pca2, y, test_size=0.3, random_state=42)

# Addestra e valuta il modello sui dati ridotti a 4 componenti
model_pca2 = LogisticRegression(max_iter=10000)
model_pca2.fit(X_train_pca2, y_train_pca2)
y_pred_pca2 = model_pca2.predict(X_test_pca2)
accuracy_pca2 = accuracy_score(y_test_pca2, y_pred_pca2)
print(f"Accuratezza con dati ridotti (PCA - 4 dimensioni): {accuracy_pca2:.2f}")