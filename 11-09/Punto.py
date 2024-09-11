import math

class Punto:

    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    
    def muovi(self,dx,dy):
        self.x += dx
        self.y += dy
    
    def distanza_da_origine(self):
        somma = self.x**2 + self.y**2
        d = math.sqrt(somma)
        return d
    


    
