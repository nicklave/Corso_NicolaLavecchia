# Scrivi una funzione chiamata area_triangolo che
#  prenda in input la base e l'altezza di un triangolo e restituisca la
#  sua area. fare la stessa cosa con quadrato e rettagolo e rendere
#  ripetibile salvando in una lista tutti i risultati

lista = []
count = 0

def risultato(funzione):
    def wrapper(*args,**kwargs):
        global lista
        global count
        count+=1
        ris = funzione(*args,**kwargs)
        ris = round(ris,1)
        figura_geo = funzione.__name__.replace('area_','')
        lista.append((count,figura_geo,ris))
        return ris
    return wrapper
        

@risultato
def area_triangolo(base,altezza):
    area = (base*altezza)/2
    return area

@risultato
def area_rettangolo(base,altezza):
    area = base*altezza
    return area

@risultato
def area_quadrato(lato):
    area = lato**2
    return area

def num_input(s):
    numero = input(s)
    try:
        return int(numero)
    except ValueError:        
        try:
            return float(numero)
        except ValueError:
            print("Errore, non hai inserito un numero")


def main():

    global lista

    x = input("Digita t per triangolo, r per rettangolo, q per quadrato, u per uscire: ")

    while x != 'u':
        if x == 't':
            s1 = "Inserisci la base del triangolo: "
            b_tr = num_input(s1)
            s2 = "Inserisci l'altezza del triangolo: "
            h_tr= num_input(s2)
            ris = area_triangolo(b_tr,h_tr)
        elif x == 'r':
            s1 = "Inserisci la base del rettangolo: "
            b_rett = num_input(s1)
            s2 = "Inserisci l'altezza del rettangolo: "
            h_rett = num_input(s2)
            ris = area_triangolo(b_rett,h_rett)
        elif x == 'q':
            s = "Inserisci il lato del quadrato: "
            l_quadr = num_input(s)
            ris = area_quadrato(l_quadr)
        
        x = input("Digita t per triangolo, r per rettangolo, q per quadrato, u per uscire: ")

    print("Lista di tuple i cui valori sono: (iterazione,forma geometrica,risultato)")
    print(lista)
main()


    



