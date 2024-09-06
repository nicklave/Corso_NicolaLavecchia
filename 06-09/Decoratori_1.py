def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione")
        funzione()
        print("Dopo l'esecuzione")
    return wrapper


@decoratore
def saluta():
    print("Ciao")
    
    
saluta()
