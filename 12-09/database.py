# creare un programma per la gestione degli studenti di una scuola,
# all'avvio se il db è presente legge i dati da db altrimenti lo crea,
# l'utente puoi inserire studenti e voti all'interno del db
#Finita la prima parte aggiungete al programma la possibilità di modificare voti e alunni

def crea_dizionario():

    x = input("Inserisci uno studente o esci per uscire: ")

    dizionario = {}

    while x!= 'esci':
        dizionario[x] =[]
        count = 0
        for i in range(4):
            y = int(input(f"Inserisci i voti dello studente {x}: "))
            count += y
            dizionario[x].append(y)
        x = input("Inserisci uno studente oppure scrivi o esci per uscire: ")
    return dizionario

dizionario = crea_dizionario()

with open("Database","w") as file:
    file.write("Id,Nome,Voti")

with open("Database","a") as file:
    id = 0
    for i,j in dizionario.items():
        file.write(str(id)+i+str(j))
        id = int(id) + 1
