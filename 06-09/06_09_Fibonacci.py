#Nella versione ricorsiva vado da n fino a 0
def fibonacci_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonacci_r(n-1)+(fibonacci_r(n-2))

#Nella versione iterativa vado da 0 fino ad n
def fibonacci_iter(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        n2=0    #variabile di partenza
        n1=1    #seconda variabile di partenza
        i=2     #parto dalla seconda iterazione avendo già specificato le prime due
        while(i<=n):
            temp = n1   #salvo la variabile maggiore di partenza
            n1 = n2+n1  #la variabile maggiore diventa essa stessa sommata al suo precedente
            n2 = temp   #l'ex variabile maggiore diventa quella minore
            i = i + 1   #contatore per ciclo while
        return n1   