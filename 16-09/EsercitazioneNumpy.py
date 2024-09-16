import numpy as np
import copy


#TIPO DI DATO E FORMA

#  Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
a = np.arange(10,50)

#  Verifica il tipo di dato dell'array e stampa il risultato.
print(f"Tipo iniziale dell'array: {a.dtype}")

#  Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
a.dtype = 'float64'

print("Tipo modificato dell'array: ",a.dtype)

#  Stampa la forma dell'array.
print("Forma dell'array: ",a.shape)


# SLICING E INDEXING

array = np.random.randint(10,50,size = 20)
print(f"Array originale: {array}")

#estraggo i primi 10 elementi

print(f"Primi 10 elementi: {array[:11]}")

#estraggo gli ultimi 5 elementi

print(f"Ultimi 5 elementi: {array[-5:]}")

#da indice 5 a indice 15

print(f"Da indice 5 a indice 15 {array[5:15]}")

#ogni terzo elemento

print(f"Ogni terzo elemento: {array[2:21:3]}")

#modifico tramite slicing
array2 = copy.copy(array)
array3 = copy.copy(array)

array3[5:10] = 99

indici = np.array([5,6,7,8,9])

array2[indici] = 99 

print(f"Array modificato tramite fancy indexing: {array2}")

print(f"Array modificato tramite slicing: {array3}")