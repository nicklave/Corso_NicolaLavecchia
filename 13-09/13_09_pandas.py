import pandas as pd
import datetime

# Create un DataFrame sulla base di un elenco di almeno 10 clienti forniti dall'utente tramite input e salvatelo in formato csv.
# Per ogni cliente verranno forniti:</h4>
# Numero Cliente, Nome, Cognome, Data di Nascita, Regione di Residenza.</li>

# Partendo dal dataframe creato nell'esercizio precedente, aggiungete 3 colonne:
# La prima contiene una X in corrispondenza dei clienti minorenni;
# La seconda contiene una X in corrispondenza dei clienti con età maggiore di 17 anni;
# La terza contiene una X in corrispondenza dei clienti con età maggiore di 20 anni.


utente = {}
utente['Nome'] = []
utente['Cognome'] = []
utente['Data nascita'] = []
utente['Regione residenza'] = []
utente['Età'] = []

data_ora = datetime.datetime.now()

for i in range(3):
    # print("Nuovo utente")
    # nome = input("Inserisci il nome: ")
    # cognome = input("Inserisci il cognome: ")
    # data = input("Inserisci la data di nascita: ")
    # regione = input("Inserisci la regione di residenza: ")
    nome = ['Nicola','Mario','Giuseppe']
    cognome = ['Lavecchia','Rossi','Verdi']
    data = ['12/09/2009','30/12/2002','12/11/2008']
    regione = ['Calabria','Puglia','Lombardia']
    utente['Nome'].append(nome[i])
    utente['Cognome'].append(cognome[i])
    data_nascita = datetime.datetime.strptime(data[i], '%d/%m/%Y')
    utente['Data nascita'].append(data_nascita)
    eta = round((((data_ora-data_nascita).days)/365.25),1)
    utente['Età'].append(eta)
    utente['Regione residenza'].append(regione[i])

for utenti, valori in utente.items():
    print(f"{utenti} : {valori}")

df = pd.DataFrame(utente)

df = df.rename_axis('ID')


df.loc[df['Età'] < 18, 'Prima verifica'] = 'X'
df.loc[df['Età'] > 17, 'Seconda_verifica'] = 'X'
df.loc[df['Età'] > 20, 'Terza_verifica'] = 'X'


df.to_csv('Utenti.csv', index=True)

print(df)
