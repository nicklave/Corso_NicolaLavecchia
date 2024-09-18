import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parametri
giorni = 305
media_visitatori = 1200
deviazione_standard = 900
trend = np.linspace(0, 200, giorni)  # Trend crescente nel tempo

# Generazione dei dati casuali con distribuzione normale
visitatori_in = np.random.normal(media_visitatori,deviazione_standard,giorni)

# Aggiungere il trend crescente
visitatori = visitatori_in - trend

date = pd.date_range(start='2023-08-16', periods=305, freq='D')

patologie = ['Ossa','Testa','Cuore']

df = pd.DataFrame({'Data': date,'Visitatori':visitatori, 'Patologia': np.random.choice(patologie,size=305)})

df['Mese'] = df['Data'].dt.month

print(df.head)

somma_mese = df.groupby('Mese')['Visitatori'].mean()
std_mese = df.groupby('Mese')['Visitatori'].std()

somma_patologie = df['Patologia'].value_counts()

minima = somma_patologie.idxmin()
massima = somma_patologie.idxmax()

print(f"\nMedia visitatori per mese:\n {somma_mese}")
print(f"\nStd visitatori per mese\n {std_mese}")
print(f"\nLa patologia più trovata è: {massima}")
print(f"\nLa patologia meno trovata è: {minima}")







