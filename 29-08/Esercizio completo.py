from random import randint

# Punto 1: Utilizzo di if 
# Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari
#  e "Dispari" se il numero è dispari.
#  Punto 2: Utilizzo di while e range
#  Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i
#  numeri da n a 0 (compreso), decrementando di 1.Deve potersi ripete all’infinito
#  Punto 3: Utilizzo di for 
# Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di
#  ciascun numero nella lista.
#  1.
#  Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema che prende in input
#  una lista di numeri interi che precedente è stata valorizzata dall’utente. 
# Il sistema deve:
#  Utilizzare un ciclo for per trovare il numero massimo nella lista.
#  2.
#  3.
#  Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
#  Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
#  altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.

#Primo punto
print("Inizio primo punto\n")
n = int(input("Inserisci un numero oppure -1 per uscire: "))  #inizializzo un intero da console
while n != -1:  #finchè non si passa la condizione di terminazione
    if n%2==0:  #se il resto della divisione intera per due è uguale a zerp il numero è pari
        print("Il numero",n,"è pari")
    else:
        print("Il numero",n,"è dispari")
    n = int(input("Inserisci un numero: "))  #finchè il ciclo non termina do la possibilità di inserire un altro numero
print("\nFine primo punto\n")

#Secondo punto
print("Inizio secondo punto\n")
x = int(input("Inserisci un numero: ")) #inizializzo un intero da console
while x >= 0: #finchè il numero dato è >= 0 lo stampo
    print(x)
    x -= 1  #decremento il contatore fino ad arrivare alla condizione di terminazione

print("\nFine secondo punto\n")

#Terzo punto
print("Inizio terzo punto\n")
l = [1,2,3,4,5]   #inizializzo una lista
for elem in l:    #inizializzo un ciclo
    print("Il quadrato di",elem, "è ", elem**2)  #stampo direttamente il quadrato elemento per elemento
print("\nFine terzo punto\n")

#Quarto punto
print("Inizio quarto punto\n")
l = []    #inizializzo una lista vuota
for i in range(10):  #inizializzo un ciclo di 10 elementi
    n = int(input("Inserisci un numero: "))  #Faccio scegliere un numero all'utente
    l.append(n)   #inserisco il suddetto numero in lista fino ad arrivare a 10 elementi

print("La lista è: ",l)   #stampo la lista

if len(l)>0:
    massimo = 0  #inizializzo un intero
    for i in range(len(l)):   #inizializzo un ciclo che segue gli indici della lista
        if l[i]>massimo:      # se il numero preso attualmente è maggiore del massimo memorizzato fino ad ora 
            massimo = l[i]    #sostituisco a massimo quel numero
    print("Il massimo in lista è:", massimo)

    count = 0    #inizializzo un contatore
    while count < len(l):   #finchè il contatore è minore della lunghezza della lista
        count += 1          #aumento il contatore
    print("Il numero di elementi in lista è: ",count)   #stampo il contatore

else:
    print("La lista è vuota")
    
print("\nFine quarto punto")





    