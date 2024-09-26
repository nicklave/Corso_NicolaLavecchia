# Scrivete un programma che chiede una stringa all’utente e
# restituisce un dizionario rappresentante la "frequenza di
# comparsa" di ciascun carattere componente la stringa.
# Esempio:
# Stringa "ababcc",
# Risultato
# {"a": 2, "b": 2, "c": 2}


x = 'aaabbbbcca'

l = []
dizionario = {}

for elem in x:
    if elem not in l:
        l.append(elem)


for i in range(len(l)):
    count = 0
    for j in x:
        if j == l[i]:
            count+=1
    dizionario[l[i]] = count


for chiave,elemento in dizionario.items():
    print(f"La lettera {chiave} appare {elemento} volte")    
    
