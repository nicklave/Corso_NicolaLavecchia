import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#  Hai a disposizione un dataset, che devi autogenerare,
#  contenuto in un DataFrame pandas con una singola colonna
#  temperature che rappresenta la temperatura giornaliera in
#  una città per un mese. 

# Scrivi un programma Python che calcoli e stampi le seguenti
#  statistiche:
#  La temperatura massima
#  La temperatura minima
#  La temperatura media
#  La mediana delle temperature

temperature = np.random.uniform(15,41,size=31)


df = pd.DataFrame({'Temperatura':temperature})

print(df)

max_val = df['Temperatura'].max()
min_val = df['Temperatura'].min()
mean_val = df['Temperatura'].mean()
median_val = df['Temperatura'].median()


plt.plot(df['Temperatura'])
plt.title('Grafico a linee')
plt.xlabel('Data')
plt.ylabel('Temperatura')


plt.axhline(y=max_val, color='r', linestyle='--', label='Massimo')
plt.axhline(y=min_val, color='b', linestyle='--', label='Minimo')
plt.axhline(y=mean_val, color='g', linestyle='--', label='Media')
plt.axhline(y=median_val, color='orange', linestyle='--', label='Mediana')

plt.legend()
plt.tight_layout()  # Migliora il layout per evitare sovrapposizioni

plt.show()