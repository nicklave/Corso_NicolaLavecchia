
# Definisco nome utente, password e id predefinite
nome_utente = 'admin' 
password = '12345'

# Fase di login dell'utente esterno da console
x = input('Inserisci il nome utente: ')
y = input('Inserisci la password: ')

#Controllo che il nome utente sia corretto, se non esiste permetto la creazione di un nuovo account
if (x == nome_utente and y == password): 
    #Permetto la visualizzazione in console delle credenziali
    stampa = "Benvenuto " + nome_utente
    print(stampa)

    #Permetto la scelta di una domanda segreta e la conseguente risposta
    z = input('Premere invio per andare avanti')
    domanda = input("Inserire una domanda segreta tra: \nQual è il colore preferito? \nQual è il tuo animale preferito?\n")
    risposta= input("Inserisci una risposta: ")

    #Permetto la modifica di una delle credenziali o entrambe
    uscita = input('Digitare m per modificare oppure u per uscire')
    if uscita == 'm':
          modifica = input("Digitare 1 per modificare solo il nome, 2 solo per la password, both per entrambe o invio per andare avanti ")
          if modifica == '1':
             x = input('Inserisci il nuovo nome utente: ')
             print("Il tuo nuovo nome utente è", x)
          elif modifica == '2':
             y = input('Inserisci la nuova password: ')
             print("La tua nuova password è", y)
          elif modifica == 'both':
             x = input('Inserisci il nuovo nome utente: ')
             y = input('Inserisci la nuova password: ')
             print("Le tue nuove credenziali sono", x, " ", y)
    else:
         exit()


#Se le credenziali sono errate stampo un avviso
else:
        print("Credenziali errate")
