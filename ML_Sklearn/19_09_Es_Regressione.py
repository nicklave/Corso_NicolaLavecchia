from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import Ridge,Lasso,LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd


data = load_diabetes()

#print(data['DESCR'])

X = data.data
y = data.target

print(pd.DataFrame(X, columns=data.feature_names).head(),"\n")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(),
    'Lasso Regression': Lasso(alpha=0.1),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    predict = model.predict(X_test)

    mse = mean_squared_error(y_test,predict)
    r2 = r2_score(y_test,predict)

    print(f"MSE tramite {name}: {mse}\n")
    print(f"R2 tramite {name}: {r2}\n")






