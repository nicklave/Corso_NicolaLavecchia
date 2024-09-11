class Ristorante:

    def __init__(self,nome,tipo_cucina):
        if isinstance(nome,str) and isinstance(tipo_cucina,str):
            self.nome = nome
            self.tipo_cucina = tipo_cucina
        else:
            print("Il nome e il tipo di cucina devono essere stringhe")
        
        self.aperto = False
        self.dizionario = {}
    
    def descrivi_ristorante(self):
        s = f"Il ristorante {self.nome} fa cucina di tipo {self.tipo_cucina}"
        print(s)
    
    def stato_apertura(self):
        if self.aperto == False:
            print("Il ristorante è chiuso")
        else:
            print("Il ristorante è aperto")
  
    def apri_ristorante(self):
        self.aperto = True
        self.stato_apertura()

    def chiudi_ristorante(self):
        self.aperto = False
        self.stato_apertura()
    
    def aggiungi_al_menu(self,chiave,valore):
        if isinstance(chiave,str) and isinstance(valore,float):
            if chiave not in self.dizionario:
                self.dizionario[chiave] = float(valore)
        else:
            print("Errore: i valori devono essere rispettivamente una stringa e un float")

    def togli_dal_menu(self,chiave):
        if chiave in self.dizionario:
            self.dizionario.pop(chiave)

    def stampa_menu(self):
        print(f"\nMenu del ristorante {self.nome}")
        for chiave,valore in self.dizionario.items():
            print(f"Piatto: {chiave} \nPrezzo: {valore} €\n")

r = Ristorante("Trattoria Nick","Tradizionale")
r.descrivi_ristorante()
r.stato_apertura()
r.apri_ristorante()
r.chiudi_ristorante()
r.aggiungi_al_menu("Fileja con la 'nduja",8.0)
r.aggiungi_al_menu("Tagliatelle al ragù",7.0)
r.aggiungi_al_menu("Grigliata mista",10.0)
r.togli_dal_menu("Tagliatelle al ragù")
r.stampa_menu()
        

    

