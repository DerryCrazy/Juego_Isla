from objetos.peligro import Peligro #Herencia del objeto peligro

class Coco(Peligro): #Instancia del objeto a partir de heredar de peligro
    def __init__(self):
        super().__init__("Cocodrilazo", efecto=-1000) #le ponemos el nombre y el efecto mandela con polimorfismo

    def interactuar(self): #la funcion cuando el jugador lo encuentra y ps el mensaje
        return "Oh no, Encontraste al master de masters"