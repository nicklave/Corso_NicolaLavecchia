def crea_dizionario_voti():
    dizionario_voti = {}
    while True:
        nome = input("Inserisci nome: ")
        voti = []
        while True:
            voto = input("Inserisci voto o 's' per terminare ")
            if voto =='s':
                break
            else:
                voti.append((voto))
        
        voti2 = ' '.join(voti)
                
        dizionario_voti[nome] =  voti2
        
        check = input("vuoi continuare (y) o uscire (esci)? ")
        if check== 'esci':
            break
    return dizionario_voti

def aggiungi_voto(id_studente, nuovo_voto):
    
    with open("voti.csv", "r") as file:
        righe = file.readlines()

    with open("voti.csv", "w") as file:
        for riga in righe:
            campi = riga.strip().split(',')  
            
            if campi[1].strip() == str(id_studente):
                
                voti_esistenti = campi[2].strip()   
                nuovi_voti = voti_esistenti +' '+ str(nuovo_voto)  
                campi[2] = nuovi_voti  

            riga_modificata = ','.join(campi)
            file.write(riga_modificata + "\n")

def rimuovi_studente(id_studente):
    
    with open("voti.csv", "r") as file:
        righe = file.readlines()

    with open("voti.csv", "w") as file:
        for riga in righe:
            campi = riga.strip().split(',')  
            
            if campi[1].strip() == str(id_studente):
                continue

            riga_modificata = ','.join(campi)
            file.write(riga_modificata + "\n")

if __name__=='__main__':
    dizionario = crea_dizionario_voti()

    with open("voti.csv","w") as file:
        file.write("nome,id,voti")
        
    with open("voti.csv","a") as file:
        id = 0
        for i,j in dizionario.items():
            file.write("\n" + i + ',' + str(id) +',' +j)
            id += 1
            
        
            
    print(dizionario.items())