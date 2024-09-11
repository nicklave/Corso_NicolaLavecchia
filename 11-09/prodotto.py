import datetime
class Elettronica:
    
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        self.nome = nome
        self.costo_produzione = float(costo_produzione)
        self.prezzo_vendita = float(prezzo_vendita)
        self.reso = False
        self.data_acquisto = datetime.datetime.now()

    def getReso(self):
        return self.reso
    
    def __str__(self):
        s = self.nome
        return s 
    
    def stampa(self):
        if self.reso() == False:
            s = f"Il prodotto {self.nome} è nuovo e costa alla fabbrica {self.costo_produzione}€ e viene venduto a {self.prezzo_vendita} €"
        else:
            s = f"Il prodotto {self.nome} proviene da un reso e costa alla fabbrica {self.costo_produzione}€ e viene venduto a {self.prezzo_vendita} €"
        return s
    
    def calcola_profitto(self):
        ris = self.prezzo_vendita - self.costo_produzione
        return ris
    
    def calcola_scadenza_garanzia(self):
        print("Data acquisto: ", self.data_acquisto.strftime("%d/%m/%Y"))
        d = self.data_acquisto + datetime.timedelta(days = 730)
        d_format = d.strftime("%d/%m/%Y")
        print("Scadenza garanzia: ", d_format)
    
    def prodottoReso(self):
        self.reso = True
    
class BicchieriPlastica:
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.reso = False

    def getReso(self):
        return self.reso
    
    def __str__(self):
        s = self.nome
        return s 
    
    def calcola_profitto(self):
        ris = self.prezzo_vendita - self.costo_produzione
        return ris
    
    def prodottoReso(self):
        self.reso = True
    
    def stampa(self):
        if not self.reso():
            s = f"Il prodotto {self.nome} è nuovo e costa alla fabbrica {self.costo_produzione}€ e viene venduto a {self.prezzo_vendita} €"
        else:
            s = f"Il prodotto {self.nome} proviene da un reso e costa alla fabbrica {self.costo_produzione}€ e viene venduto a {self.prezzo_vendita} €"
        return s


