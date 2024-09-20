# Finita la prima parte aggiungete al programma la possibilità di modificare voti e alunni

import studenti_scuola


'''with open("voti.csv","r") as file:
    contenuto = file.readlines()
    id = int(contenuto[-1].split(',')[1])
    id +=1
    
dizionario = studenti_scuola.crea_dizionario_voti()

with open("voti.csv","a") as file:
    
    for i,j in dizionario.items():
        file.write("\n" + i + ',' + str(id) +',' +j)
        id = 1 + int(id)'''

#studenti_scuola.aggiungi_voto(1,5)

studenti_scuola.rimuovi_studente(1)