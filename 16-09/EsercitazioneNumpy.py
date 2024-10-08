import numpy as np
import copy


#TIPO DI DATO E FORMA

#  Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
a = np.arange(10,50)

#  Verifica il tipo di dato dell'array e stampa il risultato.
print(f"Tipo iniziale dell'array: {a.dtype}\n")

#  Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
a.dtype = 'float64'

print("Tipo modificato dell'array: ",a.dtype,"\n")

#  Stampa la forma dell'array.
print("Forma dell'array: ",a.shape,"\n")


# SLICING E INDEXING

array = np.random.randint(10,50,size = 20)
print(f"Array originale: {array}\n")

#estraggo i primi 10 elementi

print(f"Primi 10 elementi: {array[:11]}\n")

#estraggo gli ultimi 5 elementi

print(f"Ultimi 5 elementi: {array[-5:]}\n")

#da indice 5 a indice 15

print(f"Da indice 5 a indice 15 {array[5:15]}\n")

#ogni terzo elemento

print(f"Ogni terzo elemento: {array[2:21:3]}\n")

#modifico tramite slicing
array2 = copy.copy(array)
array3 = array.copy()

array3[5:10] = 99

indici = np.array([5,6,7,8,9])

array2[indici] = 99 

print(f"Array modificato tramite fancy indexing: {array2}\n")

print(f"Array modificato tramite slicing: {array3}\n")

# OPERAZIONI SU ARRAY

# Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.

ar = np.linspace(0,1,12)
arr = np.round(ar,3)
print(f"Array di 12 numeri equidistanti: {arr}\n")


#  Cambia la forma dell'array a una matrice 3x4.

arr.reshape(3,4)
print(f"Array ridimensionato: {arr}\n")

#  Genera una matrice 3x4 di numeri casuali tra 0 e 1.

matr = np.random.rand(3,4)
matrice = np.round(matr,3)

print(f"Matrice 3x4:\n {matrice}\n")

print(f"Matrice 4x3:\n {matrice.reshape(4,3)}\n")


#  Calcola e stampa la somma degli elementi di entrambe le matrici.

somma_arr = np.sum(arr)
somma_matr = np.sum(matrice)

print(f"La somma dell'array è {somma_arr}\nLa somma della matrice è {somma_matr}\n")


# Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.

equi = np.linspace(0,10,50)
new_array = np.round(equi,3)
print(f"Array di 50 numeri equidistanti:\n {new_array}\n")

#  Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.

new_arr = np.random.random(size = 50)
new_arr2 = np.round(new_arr,3)
print(f"Array random da 0 a 1:\n {new_arr2}\n")


#  Somma i due array elemento per elemento per ottenere un nuovo array.

somma = new_array + new_arr2
print(f"Somma elemento per elemento:\n {somma}\n")

#  Calcola la somma totale degli elementi del nuovo array.

print(f"Somma del nuovo array: {np.sum(somma)}\n")

#  Calcola la somma degli elementi del nuovo array che sono maggiori di 5.

maggiori = somma[somma>5]
print(f"Elementi maggiori di 5:\n {maggiori}\n")

#  Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.