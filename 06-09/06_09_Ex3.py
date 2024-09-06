# Scrivi una funzione chiamata area_triangolo che
#  prenda in input la base e l'altezza di un triangolo e restituisca la
#  sua area. fare la stessa cosa con quadrato e rettagolo e rendere
#  ripetibile salvando in una lista tutti i risultati

def area_triangolo(base,altezza):
    area = (base*altezza)/2
    return area

def area_rettangolo(base,altezza):
    area = base*altezza
    return area

def area_quadrato(lato):
    area = lato**2
    return area

def main():
    x = input("Digita t per triangolo, r per rettangolo, q per quadrato, u per uscire: ")

    l = []
    count = 0

    while x != 'u':
        count+=1
        if x == 't':
            b_tr = int(input("Inserisci la base del triangolo: "))
            h_tr = int(input("Inserisci l'altezza del triangolo: "))
            ris = area_triangolo(b_tr,h_tr)
            l.append((count,ris))
        elif x == 'r':
            b_rett = int(input("Inserisci la base del rettangolo: "))
            h_rett = int(input("Inserisci la base del rettangolo: "))
            ris = area_triangolo(b_rett,h_rett)
            l.append((count,ris))
        elif x == 'q':
            l_quadr = int(input("Inserisci il lato del quadrato: "))
            ris = area_quadrato(l_quadr)
            l.append((count,ris))
        
        x = input("Digita t per triangolo, r per rettangolo, q per quadrato, u per uscire: ")
    
    print("Ecco la lista di tuple i cui valori sono: (iterazione,risultato)")
    print(l)

main()


    



