n = input("Inserisci un numero oppure premere invio per uscire: ")
if n != '':
    n = int(n)
l = []
while n != '':
    l.append(n)
    n = input("Inserisci un numero oppure premere invio per uscire: ")
    if n != '':
        n = int(n)

print(l)

