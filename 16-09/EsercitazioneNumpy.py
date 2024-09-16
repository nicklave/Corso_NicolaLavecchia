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