#Es 3:  Crea un sistema che permetta di valorizzare una lista di 5 numeri per due volte,
#  dopodiché somma ogni posizione con la corrispettiva dell'altra aggregazione e 
# stampa i risultati, alla fine chiedi se si vuole ripete. 

x = ''

while x != 'no':
    l = []
    l2 = []
    l_ris = []
    for i in range(5):
        n = int(input("Quale numero si vuole inserire in lista: "))
        l.append(n)
        l2.append(n)
        l_ris.append(l[i]+l2[i])
    print("Ecco la lista formata dalle somme degli elementi delle prime due: ", l_ris)
    x = input("Vuoi ripetere? digitare no per uscire: ")

