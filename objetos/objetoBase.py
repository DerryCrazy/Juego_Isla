class ObjetoBase: #Objeto baseeee para heredar a los demas
    def __init__(self, nombre, efecto=None):  #La iniciacion encapsulada
        self.nombre = nombre
        self.efecto = efecto # daño

    def interactuar(self): #Interactuar basico
        return f"Has encontrado {self.nombre}."