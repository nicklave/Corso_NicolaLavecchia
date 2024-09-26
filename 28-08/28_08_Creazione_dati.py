# Creare un if con else semplice, dentro l’if inserire una strttura di
#  creazione di dati ( nome, password, id dato dal sistema a crescere  ) e
#  nell’else il controllo automatico la dove è presente l’accout nel sistema
#  e solo se si passa dall’else concludere lo script


# Definisco nome utente, password e id predefinite
nome_utente = 'admin' 
password = '12345'
identificativo = 0

# Fase di login dell'utente esterno da console
x = input('Inserisci il nome utente: ')
y = input('Inserisci la password: ')

#Controllo che il nome utente sia corretto, se non esiste permetto la creazione di un nuovo account
if not (x == nome_utente): 
    new = input("Account non esistente, premere invio per crearne uno nuovo")
    print('Nuovo utente ')
    nome_utente = input('Inserisci il nome utente: ')
    password = input('Inserisci la password: ')
    identificativo += 1

    #Permetto la visualizzazione in console delle credenziali
    stampa = "Nuovo utente\n" + "Nome utente:" + nome_utente + "\n" + "Identificativo: " + str(identificativo)
    print(stampa)

#Controllo che nome utente e password siano contemporaneamente corretti
#Se la password è errata permetto di resettarla
elif (x==nome_utente and y !=password): 
    err = input("Password errata, premere invio per resettarla")
    password = input('Inserisci la nuova password: ')
    print("Esegui nuovamente il programma per effettuare il login")

#Se le credenziali inserite sono corrette do la possibilità di modifica delle stesse o di logout
else:
    z = int(input("Digita 1 per modificare le credenziali o invio per uscire: "))
    if z == 1:
        nome = input('Inserisci il nome utente: ')
        password = input('Inserisci la password: ')
        stampa_mod = "Nuove credenziali\n" + "Nome utente:" + nome + "\n" + "Identificativo: " + str(identificativo)
        print(stampa_mod)
    else:
        print('Hai effettuato il logout')








    

