from Prodotto import *

class Fabbrica:

    def __init__(self):
        self.inventario = {}
        self.count = 0
        self.quantita_venduta = 0

    def aggiungi_prodotti(self,prodotto):
        self.inventario[prodotto] = []
        if prodotto not in self.inventario:
            self.count = 1
            self.inventario[prodotto].insert(0,self.count)
        else:
            self.count+=1
            self.inventario[prodotto].insert(0,self.count)
        
    def vendi_prodotto(self, prodotto):
        if prodotto in self.inventario:
            self.count -= 1
            self.quantita_venduta +=1
            self.inventario[prodotto][0] = self.count
            self.inventario[prodotto].insert(1,prodotto.calcola_profitto()*self.quantita_venduta)
    
    def resi_prodotto(self, prodotto):
        if prodotto.getReso():
            self.count += 1
            self.inventario[prodotto][0] = self.count
    
    def visualizza(self):
        for key,values in self.inventario.items():
            print(f"La quantità di prodotto {key} è {values[0]} e il guadagno generato è {values[1]}")

prod = prodotto.Elettronica("Ps5",300,550)
prod1 = prodotto.BicchieriPlastica("Bio",0.60,1.20)
f = fabbrica()
f.aggiungi_prodotti(prod)
prod.stampa()
# f.aggiungi_prodotti(prod1)
# f.aggiungi_prodotti(prod)
# f.aggiungi_prodotti(prod)
# f.vendi_prodotto(prod)
# f.vendi_prodotto(prod1)
# prod.prodottoReso()
# f.resi_prodotto(prod)
# f.resi_prodotto(prod1)
# f.visualizza()
# prod.calcola_scadenza_garanzia()



