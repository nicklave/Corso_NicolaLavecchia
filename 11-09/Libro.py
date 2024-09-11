class Libro:
    
    def __init__(self,titolo,autore,pagine):
        try:
            if not self.titolo.isalnum():
                self.titolo = titolo
        except:
            print("Il titolo non è valido")

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