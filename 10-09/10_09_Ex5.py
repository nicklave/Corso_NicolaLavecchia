# Scrivete un programma che utilizza il cifrario di Cesare per criptare una
# parola o decriptarla.
# Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
# ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
# sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
# di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
# una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
# Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
# conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
# di posti corrispondente alla chiave.

def controllocar(funzione):
    def wrapper(parola,chiave):
        if parola.isalpha():
            return funzione(parola,chiave)
        else:
            print('Errore: La parola deve contenere solo lettere')
            parola_new = input("Inserisci una parola corretta: ")
            return funzione(parola_new,chiave)
    return wrapper

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
stampa = ''

@controllocar
def criptare(parola,chiave):
    global stampa
    global alfabeto
    s = ''
    for c in parola:
        i = alfabeto.index(c)
        if (i+chiave)<= len(alfabeto):
            s+=alfabeto[i+chiave]
        else:
            s+= alfabeto[(i+chiave)%26]
    stampa += "La parola " +str(parola) + " criptata per " + str(chiave) + " è: " +str(s)
    return s

@controllocar
def decriptare(parola,chiave):
    global alfabeto
    global stampa
    s = ''
    for c in parola:
        i = alfabeto.index(c)
        if i>=chiave:
            s+=alfabeto[i-chiave]
        else:
            s+=alfabeto[i]
    stampa += "La parola" +str(parola) + "decriptata per" + str(chiave) + "è" +str(s)
    return s
    
def main():
    x = input("c per criptare, d per decriptare: ")
    z = input("Inserisci la parola da criptare o decriptare: ")
    y = int(input("Inserisci la chiave di criptaggio: "))

    if x == 'c':
        criptare(z,y)
        print(stampa)
    elif x == 'd':
        print(f"La parola {z} decriptata per {y} è {decriptare(z,y)}")

main()