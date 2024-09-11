class Libro:
    
    def __init__(self,titolo,autore,isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def getIsbn(self):
        return self.isbn
    
    def getTitolo(self):
        return self.titolo

    # def __str__(self):
    #     s = "Il libro " + self.titolo + " è stato scritto da " + self.autore + " e ha pagine " + str(self.isbn)
    #     return s

    def descrizione(self):
        s = "Il libro " + self.titolo + " è stato scritto da " + self.autore + " e ha isbn " + str(self.isbn)
        return s
    
# l = Libro("Pinocchio","Carlo Collodi",150)
# if type(l) == Libro:
#     print(l.descrizione())

