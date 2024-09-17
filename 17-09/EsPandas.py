import numpy as np
import pandas as pd

def creazione():
    lista_nomi = ['Alice', 'Maria', 'Marco', 'Maria']
    lista_citta = ['Roma', 'Milano', None , 'Firenze', 'Firenze'] 

    nomi = []
    eta = []
    citta = []
    stipendio = []

    for i in range(5):
        indice_nomi = np.random.randint(0,len(lista_nomi))
        nomi.append(lista_nomi[indice_nomi])
        indice_citta = np.random.randint(0,len(lista_citta))
        citta.append(lista_citta[indice_citta])
        eta.append(np.random.randint(18,45))
        stipendio.append(np.random.randint(1200,2500))
    
    eta.pop(np.random.randint(0,5))
    eta.append(np.nan)
    
    dizionario = {'Nome' : nomi , 'Eta' : eta , 'Città' : citta , 'Stipendio' : stipendio}

    df = pd.DataFrame(dizionario)

    return df

def main():
    df = creazione()
    print(f"Data frame originale:\n {df}\n")
    #print(df.head)

    media_eta = df['Eta'].mean()
    media_stip = df['Stipendio'].mean()

    mediana_eta = df['Eta'].median()
    mediana_stip = df['Stipendio'].median()

    std_eta = df['Eta'].std()
    std_stip = df['Stipendio'].std()

    df = df.drop_duplicates()

    df['Eta'].fillna(df['Eta'].mean(), inplace = True)
    df['Città'].fillna('Roma', inplace = True)

    print(f"Nuovo data frame:\n {df}\n")

main()






    
