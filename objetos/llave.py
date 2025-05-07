from objetos.objetoBase import ObjetoBase #Herencia

class Llave(ObjetoBase):
    def __init__(self):
        super().__init__("🗝️Llave") #Polimorfismo

    def interactuar(self):
        return "Felicidades pa, encontraste la llave y ganaste este pex"