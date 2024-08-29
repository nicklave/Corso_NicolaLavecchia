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
n = int(input("Inserisci un numero oppure -1 per uscire: "))
while n != -1:
    if n%2==0:
        print("Il numero",n,"è pari")
    else:
        print("Il numero",n,"è dispari")
    n = int(input("Inserisci un numero: "))
print("Fine primo punto\n")

#Secondo punto
print("Inizio secondo punto\n")
x = int(input("Inserisci un numero: "))
while x >= 0:
    print(x)
    x -= 1

print("Fine secondo punto\n")

#Terzo punto
print("Inizio terzo punto\n")
l = [1,2,3,4,5]
for elem in l:
    print("Il quadrato di",elem, "è ", elem**2)
print("Fine terzo punto\n")

#Quarto punto
print("Inizio quarto punto\n")
l = []
for i in range(10):
    n = randint(0,25)
    l.append(n)

print("La lista è",l)

if len(l)>0:
    massimo = 0
    for i in range(len(l)):
        if l[i]>massimo:
            massimo = l[i]
    print("Il massimo in lista è:", massimo)

    count = 0
    while count < len(l):
        count += 1
    print("Il numero di elementi in lista è",count)
else:
    print("La lista è vuota")
    
print("Fine quarto punto")





    