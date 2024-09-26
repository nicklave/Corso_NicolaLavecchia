

class Punto:

    def __init__(self,x,y):
        try:
            if not isinstance(x,float):
                self.x = float(x)
        except:
            print("Il punto in un piano deve essere un numero!")
        self.y = float(y)
    
    def muovi(self,dx,dy):
        self.x += dx
        self.y += dy
    
    def distanza_da_origine(self):
        somma = self.x**2 + self.y**2
        d = round(math.sqrt(somma),1)
        return d

p = Punto(10,3)
p.muovi(3,2)
print(p.distanza_da_origine())

    


    
