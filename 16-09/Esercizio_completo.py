import numpy as np

#  Parte UNO: 
# Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 
# Il programma deve presentare un menu interattivo che consente all'utente di
# eseguire varie operazioni sulla matrice. Le operazioni disponibili includono:

# Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
#  Estrarre e stampare la sotto-matrice centrale.
#  Trasporre la matrice e stamparla.
#  Calcolare e stampare la somma di tutti gli elementi della matrice.
#  Uscire dal programma.

#  Parte DUE: 
#  Andare a specializzare per aggiungere nuove operazioni:
#  Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di
#  creare una seconda matrice delle stesse dimensioni della prima e moltiplicarle
#  elemento per elemento e stampare il risultato.
#  Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media
#  di tutti gli elementi della matrice.



def main():
    creata = False

    
    while True:
        menu = input("""Menù\nPremi 1 per creare una matrice\nPremi 2 per creare la sottomatrice centrale\nPremi 3 per trasporre la matrice e stamparla\nPremi 4 per la somma della matrice\nPremi 5 per creare una matrice con le stesse dimensioni e moltiplicarla alla prima\nPremi 6 per la media degli elementi della matrice\nPremi 7 per il determinante della matrice\nPremi esci per uscire\n""")

        if menu == '1':
            riga = int(input("Quante righe deve avere la matrice? "))
            colonna = int(input("Quante colonne deve avere la matrice? "))
            matrice = np.random.rand(riga,colonna)
            print(f"La matrice creata è:\n{matrice}")
            creata = True
        
        elif menu == '2':
            if not creata:
                print("Non hai ancora creato una matrice!")
            else:
                print(f"Sottomatrice centrale:\n {matrice[1:riga-1,1:colonna-1]}")

        elif menu == '3':
            if not creata:
                print("Non hai ancora creato una matrice!")
            else:
                print(f"La trasposta della matrice è:\n {matrice.reshape(colonna,riga)}")

        elif menu == '4':
            if not creata:
                print("Non hai ancora creato una matrice!")
            else:
                print(f"La somma della matrice è {np.sum(matrice)}")

        elif menu == '5':
            if not creata:
                print("Non hai ancora creato una matrice!")
            else:
                matrice2 = np.random.rand(riga,colonna)
                prodotto = matrice*matrice2
                print(f"La matrice prodotto è:\n {prodotto}")

        elif menu == '6':
            if not creata:
                print("Non hai ancora creato una matrice!")
            else:
                media = np.sum(matrice)/(riga*colonna)
                print("La media degli elementi della matrice è:",media)

        elif menu == '7':
            if not creata:
                print("Non hai ancora creato una matrice!")
            else:
                if riga == colonna:
                    det = np.linalg.det(matrice)
                    print("Il determinante della matrice è",det)
                else:
                    print("La matrice non è quadrata!")
        
        
        elif menu == 'esci':
            print("Uscita dal programma")
            break

main()