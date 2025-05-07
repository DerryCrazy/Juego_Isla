from objetos.objetoBase import ObjetoBase #Herencia de objeto

class Fruta(ObjetoBase):
    def __init__(self, nombre ="🍇Fruta"): #Nombre y efecto
        super().__init__(nombre, efecto=1) # gana una vida

    def interactuar(self): #Polimorfismo
        return "Encontraste una fruta, Ganas una vida:D"    