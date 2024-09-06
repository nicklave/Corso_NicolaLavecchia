import random

def casuale():
    numero = random.randint(1,100)  #inizializzo un numero random
    return numero

def indovinaNumero(numero):

    n = int(input("Indovina il numero: "))  #chiedo un numero all'utente

    while True:   #loop che interromperò con il return

        # Condizioni
        if n == numero:
            s = 'Hai indovinato il numero'
            return s
        elif n > numero:
            print("Il numero da indovinare è minore di quello digitato")
            n = int(input("Indovina il numero: "))
        else:
            print("Il numero da indovinare è maggiore di quello digitato")
            n = int(input("Indovina il numero: "))
        
def main():
    n = casuale()
    #print("Numero da indovinare: ",n)
    print(indovinaNumero(n))

main()


            
