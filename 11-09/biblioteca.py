from Libro import *

class Biblioteca:
    def __init__(self):
        self.biblioteca = []

    def creaLibro(self,titolo,autore,isbn):
        l = libro.Libro(titolo,autore,isbn)
        return l
    
    def aggiungiLibro(self,l):
        if isinstance(l,libro.Libro):
            self.biblioteca.append(l)
        else:
            print("L'oggetto inserito non è un Libro")
    
    def stampa(self):
        for libro in self.biblioteca:
            print(libro.descrizione())

b = Biblioteca()

check = input("Digitare si per creare un Libro, no per uscire: ")

while check != 'no':
    titolo = input("Inserisci il titolo: ")
    autore = input("Inserisci l'autore: ")
    isbn = input("Inserisci l'isbn: ")
    # Oz = b.creaLibro("Il mago di Oz", "Baum",543)
    # Got = b.creaLibro("Game of thrones","Martin",123)
    libro = b.creaLibro(titolo,autore,isbn)
    b.aggiungiLibro(libro)
    check = input("Digitare si per creare un Libro, no per uscire: ")
b.stampa()




