# Esercizio 1: Oggetti
# Descrizione:  Crea un programma in Python per gestire una semplice libreria di libri. 
# Il programma dovrebbe presentare un menu all'utente con le seguenti opzioni:

# Aggiungere un nuovo libro: L'utente può inserire il titolo, l'autore e l'anno di pubblicazione 
# del libro e quantità.

# Visualizzare tutti i libri: Mostra una lista di tutti i libri attualmente nella libreria.

# Cercare un libro per titolo: L'utente inserisce un titolo e il programma cerca e mostra i
#  dettagli del libro se trovato.

# Gestione libri: Far rimuovere modificare e/o aggiungere una compia in più del libro

# Uscire dal programma: Termina l'esecuzione del programma.
from datetime import datetime

class Libro:
    def __init__(self, titolo, autore, anno, quantita):
        self.titolo = ''
        self.autore = ''
        self.anno = datetime.datetime.strptime(anno, '%d/%m/%Y')
        self.quantita = 0

    def __str__(self):
        return f'{self.titolo} - {self.autore} - {self.anno} - {self.quantita}'
    
def Programma():
    
    while True:
        menu = input("Cosa vuoi fare? 1 per aggiungere un libro, 2 per visualizzare tutti i libri, 3 per cercare un libro per titolo, 4 per gestire i libri, 5 per uscire dal programma: ")
        lista_libri = []
        if menu == '1':
            titolo = input('Inserisci il titolo del libro: ')
            autore = input('Inserisci l\'autore del libro: ')
            anno = input('Inserisci l\'anno di pubblicazione del libro in formato d/m/Y: ')
            quantita = int(input('Inserisci la quantita del libro: '))
            libro = Libro(titolo, autore, anno, quantita)
            lista_libri.append(libro)
        
        if menu == '2':
            if len(lista_libri) == 0:
                print('Non ci sono libri nella libreria')
            else:  
                for libro in lista_libri:
                    print(libro,'\n')
        if menu == 3:
            titolo = input('Inserisci il titolo del libro da cercare: ')
            for libro in lista_libri:
                if libro.titolo == titolo:
                    print(libro)
        if menu == 4:
            titolo = input('Inserisci il titolo del libro da gestire: ')
            azione = input('Premi 1 per rimuovere una copia, 2 per aggiungere una copia: ')
            for libro in lista_libri:
                if libro.titolo == titolo:
                    if azione == '1' and libro.quantita > 0:
                        libro.quantita -= 1
                    else:
                        print('Non ci sono copie disponibili')
                    if azione == '2':
                        libro.quantita += 1
        if menu == 5:
            break

Programma()



    