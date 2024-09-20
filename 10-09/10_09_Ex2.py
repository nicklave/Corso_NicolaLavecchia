#Scrivete un programma che chiede un numero all’utente e
# restituisce un dizionario con il quadrato del numero, se è pari o
# dispari e quante cifre contiene.
# Esempio:
# Numero 12
# Risultato
# {‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }

dizionario = {}

x = int(input("Inserisci un numero: "))

dizionario['quadrato'] = x**2
if x%2 == 0:
    dizionario['pari o dispari'] = 'pari'
else: 
    dizionario['pari o dispari'] = 'dispari'
stringa = str(x)
dizionario['cifre'] = len(stringa)

print(dizionario)

dizionario2 = {}

for i in range(4):
    y = int(input("Inserisci un numero: "))
    dizionario2[y] = []
    dizionario2[y].append(y**2)
    if y%2== 0:
        dizionario2[y].append('pari')
    else: 
        dizionario2[y].append('dispari')
    stringa = str(y)
    dizionario2[y].append(len(stringa))

print(dizionario2)
