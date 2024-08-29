# Il programma dovrebbe controllare se il numero inserito è
#  primo o no. 
# Se è primo, lo salva e stampa "Il numero è primo".
#  Altrimenti, stampa "Il numero non è primo". si ferma il
#  tutto quando ha 5 numeri primi

x = int(input("Inserisci un numero: "))

b = True
for i in range(2,x+1):
    if x/i != 1:
        b = False
if b == True:
    print(x, "è un numero primo")
else:
    print(x,"non è un numero primo")


