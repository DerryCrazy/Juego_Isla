from objetos.peligro import Peligro #heredacion

class Escorpion(Peligro): 
    def __init__(self):
        super().__init__("🦂Escorpion", efecto=-1) #nombre y efecto