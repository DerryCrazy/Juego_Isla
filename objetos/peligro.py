from objetos.objetoBase import ObjetoBase #heredar de objeto base

class Peligro(ObjetoBase):
    def __init__(self, nombre, efecto=1):
        super().__init__(nombre, efecto=-1)# se sobreescribe su iniciacion con un -1 porque es toxica como mi ex:´v

    def interactuar(self):# mensaje de q te hizo daño como ella:c
        return f"Cuidao cuñao, Has encontrado {self.nombre}. Pierdes una vida"
