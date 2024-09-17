from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np


data = load_iris()
X = data.data  # caratteristiche
y = data.target  # target


# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

print("Prime 5 righe di X (caratteristiche):\n", X[:5])
print("\nPrime 5 righe di y (target):\n", y[:5])

#print("\nPrime 5 righe di X scalato:\n", X_scaled[:5])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("\nPrimi 5 valori del test set(target): ",y_test[:5])

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_predictions = knn.predict(X_test)

print("\nPrime 5 righe di X predette con KNN:\n", knn_predictions[:5])

accuracy = accuracy_score(y_test, knn_predictions)

print("\nAccuratezza: ",accuracy)

#if (y_test[:45] == knn_predictions[:45]).all():
# if np.array_equal(y_test[:45], knn_predictions[:45]):
#     print("\nI valori sono tutti uguali!")
# else:
#     print("\nNon sono tutti uguali")

print("\n CROSS VALIDATION\n")
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5)  # 5-fold cross-validation
    print(f"k={k}, Accuracy: {np.mean(scores)}")
