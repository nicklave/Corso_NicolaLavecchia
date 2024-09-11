class Libro:
    
    def __init__(self,titolo,autore,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = int(pagine)


    def __str__(self):
        s = "Il libro " + self.titolo + " è stato scritto da " + self.autore + " e ha pagine " + str(self.pagine)
        return s

    def descrizione(self):
        s = "Il libro " + self.titolo + " è stato scritto da " + self.autore + " e ha pagine " + str(self.pagine)
        return s
    
l = Libro("Pinocchio","Carlo Collodi",150)
print(l)
if type(l) == Libro:
    print(l.descrizione())