import libro

class Libreria:

    def __init__(self,catalogo):
        try:
            if type(catalogo) == list:
                self.catalogo = catalogo
        except:
            print("Input errato! Serve una lista vuota")
    
    def aggiungiLibro(self,l):
        if isinstance(l,libro.Libro):
            self.catalogo.append(l)
    
    def rimuoviLibro(self,isbn):
        for libro in self.catalogo:
            if libro.getIsbn() == isbn:
                self.catalogo.remove(libro)
    
    def mostra_catalogo(self):
        for libro in self.catalogo:
            print(libro.descrizione())

    def cerca_per_titolo(self,titolo):
        l = []
        for libro in self.catalogo:
            if libro.getTitolo().startswith(titolo):
                l.append(libro)
        return l

Lib = Libreria([])
l = libro.Libro("One piece", "Eichiro Oda", 123)
l1 = libro.Libro("Dragon ball", "Akira Toriyama", 345)
Lib.aggiungiLibro(l)
Lib.aggiungiLibro(l1)
Lib.rimuoviLibro(123)
Lib.mostra_catalogo()
