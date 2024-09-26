# Andare a creare un if con vari elif e un else finale che gestisca un
#  menu per la selezione di un crud basilare (aggiungi rimuovi elimina )
#  su una lista di stringhe


s = input('Scrivi una parola: ')
x = int(input("Digita 0 per aggiungere una parola, 1 per modificare, qualsiasi altro numero per eliminare: "))

if x == 0:
    y = input('Che parola vuoi aggiungere? ')
    s = s + ' ' + y     #concateno la stringa iniziale a quella data dall'utente esterno
elif x == 1:
    z = input('Qual è la nuova parola? ')
    s = z       #sostituisco la stringa iniziale con quella data dall'utente esterno
else:
    s = ''      #svuoto la stringa

print(s)



