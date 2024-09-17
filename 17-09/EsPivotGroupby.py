import numpy as np
import pandas as pd


date = pd.date_range(start='2024-08-16', periods=30, freq='D')

#print(date)

lista_citta = ['Roma', 'Milano', np.nan, 'Firenze'] 

lista_prodotti = ['Smartphone','Tablet', np.nan, 'Computer']

data = {
    'Data': date,
    'Città': np.random.choice(lista_citta, size=30),
    'Prodotto': np.random.choice(lista_prodotti, size=30),
    'Vendite': np.random.randint(100, 1000, size=30)
}



df = pd.DataFrame(data)

df['Data'] = df['Data'].dt.strftime('%Y-%m-%d')

df = df.drop_duplicates()

prod_casuale = np.random.choice(lista_prodotti)

citta_casuale = np.random.choice(lista_citta)

df['Prodotto'] = df['Prodotto'].fillna(prod_casuale)
df['Città'] = df['Città'].fillna(citta_casuale)


tabella_pivot = df.pivot_table(values = 'Vendite', index = 'Città', columns = 'Prodotto')

grouped_df = df.groupby('Prodotto')['Vendite'].sum()

print("Data frame:\n",df)

print("\nData frame pivot:\n",tabella_pivot)

print("\nData frame raggruppato:\n",grouped_df)