# Scrivi un programma che chieda all'utente di inserire due
#  numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
#  moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
#  l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
#  per zero, il programma dovrebbe stampare "Errore: Divisione per zero". 
# Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
#  non valida".

#chiedo in input due numeri
n1 = int(input('Inserire il primo numero: '))
n2 = int(input('Inserire il secondo numero: '))

#chiedo in input l'operazione 
op = input("Inserire l'operazione da svolgere tra + - * /   :")

#inizializzo una variabile intera
ris= 0

#controllo quale sia l'operazione inserita e la svolgo
if op == '+':
    ris = n1+n2
elif op == '-':
    ris = n1-n2
elif op == '*':
    ris = n1*n2
elif op == '/' and not n2==0: #controllo che il divisore non sia zero
    ris = n1/n2
elif op == '/' and n2==0: #se il divisore è zero stampo l'errore ed esco dal programma
    print("Errore: divisione per zero")
    exit()
else:
    print("Operazione non valida") #se l'operazione non è valida stampo il messaggio ed esco
    exit()
    

print(ris)



