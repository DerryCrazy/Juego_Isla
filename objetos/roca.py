from objetos.objetoBase import ObjetoBase

class Roca(ObjetoBase):
    def __init__(self):
        super().__init__("🪨Roca") # no tiene efecto, solo le mandamos el nombre

    def interactuar(self):#No hacen nada
        return "Has encontrado una roca xd 🪨 , no hace nada we"        