import numpy as np
import pandas as pd

def creazione():
    lista_nomi = ['Alice', 'Maria', 'Marco', 'Maria']
    lista_citta = ['Roma', 'Milano', np.nan , 'Firenze', 'Firenze'] 

    nomi = []
    eta = []
    citta = []
    stipendio = []

    for i in range(10):
        indice_nomi = np.random.randint(0,len(lista_nomi))
        nomi.append(lista_nomi[indice_nomi])
        indice_citta = np.random.randint(0,len(lista_citta))
        citta.append(lista_citta[indice_citta])
        eta.append(np.random.randint(18,80))
        stipendio.append(np.random.randint(1200,2500))
    
    eta.pop(np.random.randint(0,5))
    eta.append(np.nan)
    
    dizionario = {'Nome' : nomi , 'Eta' : eta , 'Città' : citta , 'Stipendio' : stipendio}

    df = pd.DataFrame(dizionario)

    return df

def categoria_eta(eta):
    if eta <= 18:
        return 'Giovane'
    elif eta > 18 and eta <= 65:
        return 'Adulto'
    else:
        return 'Senior'
    

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


    df['Eta'] = df['Eta'].fillna(df['Eta'].median())
    df['Città'] = df['Città'].fillna('Roma')

    df = df.drop_duplicates(subset=['Nome', 'Città'])

    print(f"Nuovo data frame:\n {df}\n")

    df['Categoria Eta'] = df['Eta'].apply(categoria_eta)

    print(f"Nuovo data frame con nuova colonna:\n {df}\n")

    df.to_csv('Dipendenti.csv')



main()






    
