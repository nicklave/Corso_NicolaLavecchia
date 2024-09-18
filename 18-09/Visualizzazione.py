import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

 # Configura Seaborn
sns.set_theme(style="darkgrid")

 # Crea alcuni dati
data = np.random.normal(size=100)
print(data)

 # Crea un grafico
sns.histplot(data, kde=True)

plt.title('Distribuzione dei dati')
plt.show()