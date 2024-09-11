def decoratore(funzione):
    def wrapper():
        print("Introduzione a Python")
        funzione()
        print("Scritta tramite decoratore")
    return wrapper


@decoratore
def introProgrammazione():
    print("Python è un linguaggio di programmazione ad alto livello, dinamico ma fortemente tipizzato")

def uml():
    print("UML è un linguaggio usato per la modellazione di software")
    print("Questo è standardizzato,visuale,polivalente ed estensibile")

def liste():
    l = []
    a='Le liste'
    b = 'sono una'
    c = 'collezione ordinata'
    d = 'e modificabile di elementi'
    e = 'boh'
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    print(l)

def cicli():
    s = 'con il for scorro gli iterabili'
    s.split('')
    for elemento in s:
        print(s)

    s2 = 'con il while ho bisogno di una condizione'
    s.split('')
    i = 0
    while i < len(s2):
        print(s2)
        i+=1

def metodologie():
    print("Le metodologie sono Agile e Waterfall, la prima più libera e adatta a progetti da sviluppare con i committenti")
    print("La seconda più rigida adatta a progetti con specifiche chiare dall'inizio")

def tasking():
    print("I task sono i compiti che una persona coinvolta in un progetto deve svolgere")

def ide():
    print("Stai visualizzando questo messaggio su un Ide")

def ruoliAziendali():
    print("Data science o business analyst?")

def github():
    "Menomale che ci sono le repository"

def decoratore_argomenti(funzione):
    def wrapper(*args,**kwargs):
        print("Tabellina del 2")
        risultato = funzione()
        return risultato
    return wrapper

@decoratore_argomenti
def range():
    print(range(0,20,2))

def condizioni():
    if True:
        print("Se la condizione è vera vedi questo")
    else:
        print("Se la condizione è falsa vedi questo")


def main():
    x = input("Scrivi un numero da 0 a 10 e ti restituisco una funzione a sorpresa oppure maggiore di 10 per uscire")
    while x < 10:
        if x == 0:
            print(condizioni())
        elif x == 1:
            print(range())
        elif x == 2:
            print(github())
        elif x == 3:
            print(ruoliAziendali())
        elif x == 4:
            print(ide())
        elif x == 5:
            print(tasking())
        elif x == 6:
            print(metodologie())
        elif x == 7:
            print(cicli())
        elif x == 8:
            print(liste())
        elif x == 9:
            print(uml())
        elif x == 10:
            print(introProgrammazione())
    x = input("Scrivi un numero da 0 a 10 e ti restituisco una funzione a sorpresa oppure maggiore di 10 per uscire")
    
