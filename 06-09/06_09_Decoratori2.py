# Crea uno script che chiede nome e nun numero poi una chiama la
#  funzione primo_o_no che determini se un numero dato è primo o no. La funzione dovrebbe
#  restituire True se il numero è primo, e False altrimenti a quel punto se è primo lo salva
#  e continua il ciclo altrimenti ti dice quante volte sta non divisore più piccolo


def decoratore(funzione):
    def wrapper(x,*args,**kwargs):
        def primo_o_no(x):
            for i in range(2,x):
                resto = x - (x/i)
                if resto.is_integer() :
                    return False
            return True
        if primo_o_no(x) == False:
            ris = funzione(x,*args,**kwargs)
            return ris
        else:
            return True
    return wrapper
    
        
        
@decoratore
def primoDivisore(x):
    for i in range(2,x):
        if x%i == 0:
            return i


def main():
    l = []
    nome = input("Inserisci il nome oppure 'no' per uscire: ")
    while nome != 'no':
        n = int(input("Inserisci un numero: "))
        risultato = primoDivisore(n)
        l.append((nome,n,risultato))
        nome = input("Inserisci il nome oppure 'no' per uscire: ")
        
    
    print(l)

main()
    

        





