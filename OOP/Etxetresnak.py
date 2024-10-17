class Etxetresna:
    def __init__(self):
        self.piztuta = False

    def setIzena(self, izena):
        self.izena = izena

    def getIzena(self):
        return self.izena
    
    def piztu(self):
        if(self.piztuta):
            print("Etxetresna jada piztuta zegoen.")
        else:
            self.piztuta = True
            print("Etxetresna piztu duzu.")

    def itzali(self):
        if(self.piztuta):
            self.piztuta = False
            print("Etxetresna itzali duzu.")
        else:
            print("Etxetresna jada itzalita zegoen.")

class Telefonoa:
    def deitu(self):
        print("Deitzen...")
    def eskegi(self):
        print("Telefonoa eskegi da.")

class Mugikorra(Etxetresna, Telefonoa):
    def __init__(self, izena, sistema_eragilea):
        super().__init__()
        self.setIzena(izena)
        self.sistema_eragilea = sistema_eragilea
    
    def getSistemaEragilea(self):
        print(f"Mugikorraren sistema eragilea {self.sistema_eragilea} da.")
    
class Garbigailua(Etxetresna):
    def __init__(self, izena, garbitze_tenperaturak):
        super().__init__()
        self.setIzena(izena)
        self.garbitze_tenperaturak = garbitze_tenperaturak

    def getGarbitzeTenperaturak(self):
         print(f"Garbitzailearen garbitze-tenperaturak {self.garbitze_tenperaturak}  ºC dira.")