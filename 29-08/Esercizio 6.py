# Scrivi un programma che chieda all'utente di inserire due
#  numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
#  moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
#  l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
#  per zero, il programma dovrebbe stampare "Errore: Divisione per zero". 
# Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
#  non valida".

n1 = int(input('Inserire il primo numero: '))
n2 = int(input('Inserire il secondo numero: '))

op = input("Inserire l'operazione da svolgere tra + - * /   :")

ris= 0

if op == '+':
    ris = n1+n2
elif op == '-':
    ris = n1-n2
elif op == '*':
    ris = n1*n2
elif op == '/' and not n2==0:
    ris = n1/n2
elif op == '/' and n2==0:
    print("Errore: divisione per zero")
    exit()
else:
    print("Operazione non valida")
    exit()
    

print(ris)



