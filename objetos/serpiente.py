from objetos.peligro import Peligro

class Serpiente(Peligro):
    def __init__(self):# lo mismo que el escorpion pero mas largo
        super().__init__("🐍Serpiente", efecto=-1)