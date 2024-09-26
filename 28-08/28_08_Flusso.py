# Creare una serie di condizioni una dentro l’altra che a fronte di un
#  imput per ogni if decidano se farti passare o no ( 3 livelli, fate un
#  paragone con == )


x = int(input('Digita un numero: ')) #Permetto l'inizializzazione di un intero da console
s = 'ciao'  #inizializzo una stringa
b = False  #inizializzo un booleano

if x % 2 == 0:  #controllo che il numero sia pari
    if len(s) > 0:   #controllo che la stringa non sia vuota
        if not(b == False):     #controllo che il booleano non sia False
            print(s.replace('ciao','End'))  
            #Se tutte le condizioni sono soddisfatte sostituisco nella stringa la parola End e stampo
        else:
            print('La variabile booleana è False') #Se la terza condizione non è soddisfatta
    else:
        print('Il contatore non è maggiore di 0')  #Se la seconda condizione non è soddisfatta
else:
    print('Il numero è dispari')  #Se la prima condizione non è soddisfatta




    