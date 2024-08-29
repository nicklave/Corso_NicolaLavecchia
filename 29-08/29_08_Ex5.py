# Il programma dovrebbe controllare se il numero inserito è
#  primo o no. 
# Se è primo, lo salva e stampa "Il numero è primo".
#  Altrimenti, stampa "Il numero non è primo". si ferma il
#  tutto quando ha 5 numeri primi

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
count = 0
l = []
while count < 5:
    x = int(input("Inserisci un numero: "))
    b = True
    for i in range(2,x):
        resto = x - (x/i)
        if resto.is_integer() :
            b = False
    if b == True:
<<<<<<< Updated upstream
        print(x," è un numero primo")
        l.append(x)
        count+=1
    else:
        print(x," non è un numero primo")
=======
        print(x,"è un numero primo")
        l.append(x)
        count+=1
    else:
        print(x,"non è un numero primo")
>>>>>>> Stashed changes
   
if count == 5:
    print("Hai trovato 5 numeri primi: ",l)


