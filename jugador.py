class Jugador:
    def __init__(self, nombre):#se inicia por defecto todo esto
        self.nombre = nombre
        self.vidas= 5
        self.exploradas = set()#arreglo

    def registrar_exploracion(self, x, y):#se guardan las cordenadas en arreglo
        self.exploradas.add((x,y))

    def modificar_vidas(self, efecto):#aqui se aplica efecto
        self.vidas += efecto

    def mostrar_estado(self):#se actualiza
        print(f"Jugador: {self.nombre} | Vidas ♥️  {self.vidas}")