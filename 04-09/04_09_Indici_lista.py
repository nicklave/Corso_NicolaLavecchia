# Create un programma che genera una lista da 10 input dell'utente, 
# dovrà restituire il numero medio, il numero massimo e il numero minimo


def massimo(lista):
    print("Lista max: ",lista)
    massimo = lista[0]
    for i in range(len(lista)):
        if lista[i] > massimo:
            massimo = lista[i]
    return massimo

def minimo(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

def medio(lista):
    l = len(lista)
    if l%2 == 0:
        n1 = lista[int(l/2) -1]
        n2 = lista[int(l/2)]  
        return (n1 + n2) /2
    else:
        return lista(l//2)
    
def ordinaLista(lista):
    l_ris = []
    l2 = list(lista)

    for i in range(len(l2)):
        m = minimo(l2)
        l_ris.append(m)
        l2.remove(m)
    
    return l_ris

def main():

    l = [3,4,5,1,7,8,2,10]
    
    print("la lista è:", l)
    print("La lista ordinata è:",ordinaLista(l))
    
    print("Il numero massimo è: ",massimo(l))
    print("Il numero minimo è: ",minimo(l))
    print("Il numero medio è: ",medio(ordinaLista(l)))

main()

