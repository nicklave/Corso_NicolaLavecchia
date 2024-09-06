#  Esercizio 3 (Difficile): Sviluppa una funzione chiamata comprimi_stringa che prenda in
#  input una stringa e restituisca una versione "compressa" di essa. La compressione dovrebbe
#  funzionare in questo modo: per ogni gruppo consecutivo di caratteri identici nella
#  stringa, la funzione dovrebbe aggiungere il carattere seguito dal numero di volte che
#  appare consecutivamente.
#  Per esempio, la stringa "aaabbc" dovrebbe diventare "a3b2c1". Se la "compressione" non
#  riduce la lunghezza della stringa, la funzione dovrebbe semplicemente restituire la
#  stringa originale.
l = []

def decoratore(funzione):
    def wrapper(*args,**kwargs):
        global l
        ris=funzione(*args,**kwargs)
        l.append(ris)
        return ris
    return wrapper

@decoratore
def comprimi_stringa(s):
    s_new = ''
    i = 0
    while i < len(s):
        count = 0
        char = s[i]
        for j in range(i,len(s)-1):
            if s[j] == char:
                count+=1
                i+=1
        if count > 0:
            s_new += char + str(count)
        else:
            i+=1
            s_new +=char
        
    return s_new

def main():
    x = input("Inserisci una stringa oppure u per uscire: ")
    while x != 'u':
        comprimi_stringa(x)
        x = input("Inserisci una stringa oppure u per uscire: ")

    print(l)
    
main()




            
            

