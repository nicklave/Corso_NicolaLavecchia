#  Chiedi all'utente di inserire un numero. Il programma
#  dovrebbe quindi fare un conto alla rovescia a partire da
#  quel numero fino a zero, stampando ogni numero. e chiederti
#  se vuoi ripetere o no Chiedi all'utente di inserire un
#  numero. 


x = int(input("Inserisci un numero: "))
b = True
while b == True:
    for i in range(x,-1,-1):
        print(i)
        
    y = input("Vuoi ripetere l'operazione? Digita s oppure u per uscire: ")
    if y == 's':
        x = int(input("Inserisci un numero: "))
    else:
        b = False

        

