import numpy as np

#  Utilizza la funzione np.arange per creare
#  un array di numeri interi da 10 a 49.
#  Verifica il tipo di dato dell'array e
#  stampa il risultato.
#  Cambia il tipo di dato dell'array in
#  float64 e verifica di nuovo il tipo di
#  dato.
#  Stampa la forma dell'array.

a = np.arange(10,50)

print(a.dtype)

a.dtype = 'float64'

print(a.dtype)

print(a.shape)


# SLICING E INDEXING

array = np.random.randint(10,50,size = 20)
print(array)

#estraggo i primi 10 elementi

print(array[:11])

#estraggo gli ultimi 5 elementi

print(array[-5:])

#da indice 5 a indice 15

print(array[5:15])

#ogni terzo elemento

print(array[::3])

#modifico tramite slicing

indici = np.array([5,6,7,8,9])

array[indici] = 99 

print(array)