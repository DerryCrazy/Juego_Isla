import random
from objetos.fruta import Fruta#Importaciones
from objetos.roca import Roca
from objetos.escorpion import Escorpion
from objetos.serpiente import Serpiente
from objetos.coco import Coco
from objetos.llave import Llave

class Isla: #clase isla
    def __init__(self):
        self.mapa = [[None for _ in range(6)] for _ in range(6)] #6 * 6
        self.generar_objetos()

    def generar_objetos(self):
        objetos = [Llave(), Coco()] + [Fruta()]*3 + [Escorpion()]*3 + [Serpiente()]*3 #numero de objetos, las rocas se llenaran en vacios
        random.shuffle(objetos) #Aqui variamos orden de los objetos

        for i in range(6):
            for j in range(6):#llenado del mapa
                if objetos:
                    self.mapa[i][j] = objetos.pop()#se saca del arreglo de objetos aleatorio
                else:
                    self.mapa[i][j] = Roca()#vacios con rocas

    def explorar(self, x, y, jugador):#el movimiento
        if(x, y) in jugador.exploradas:# se guarda en casillas de exploracion
            print("⚠️ Ya exploraste esta celda, elige otra.")
            return None
        
        if not (0 <= x < 6 and 0 <= y < 6):
            print("Coordenadas no validas man")#se sale del terreno de juego
            return None
        
        objeto = self.mapa[x][y] #el objeto sera lo que tenga el mapa ahi
        jugador.registrar_exploracion(x, y) #se guarda
        print(objeto.interactuar()) #se interactua con el objeto en cuestion
        if objeto.efecto: #si tiene efecto de aplica al vato
            jugador.modificar_vidas(objeto.efecto)

        return objeto.nombre# se regresa lo que se topó el men