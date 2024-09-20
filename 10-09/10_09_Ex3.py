# Scrivete un programma che prenda i nomi degli alunni di una
# classe e i loro voti, quando l’utente scrive media il programma
# andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10

# x = input("Inserisci uno studente e scrivi media per visualizzare: ")

# dizionario = {}

# while x!= 'media':
#     count = 0
#     for i in range(4):
#         y = int(input(f"Inserisci i voti dello studente {x}: "))
#         count+=y
#     dizionario[x] = count/4
#     x = input("Inserisci uno studente oppure digitare esci: ")

# print(dizionario)

x = input("Inserisci uno studente e scrivi media per visualizzare: ")

dizionario = {}

while x!= 'media':
    dizionario[x] =[]
    count = 0
    for i in range(4):
        y = int(input(f"Inserisci i voti dello studente {x}: "))
        count += y
        dizionario[x].append(y)
    x = input("Inserisci uno studente oppure scrivi media per visualizzare: ")



for chiave, valore in dizionario.items():
    print(f"{chiave}: {valore}")




