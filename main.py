from jugador import Jugador
from isla import Isla#importaciones
import sys

def mostrar_mapa(isla, jugador): #se dibuja el mapa con lo que ha descubierto el jugador
    print("\n📜 Mapa de la isla:")# un mensaje del mapa
    for i in range(6):
        fila = ""
        for j in range(6):
            if (i, j) in jugador.exploradas:# toma lo que el jugador avanzo o seleccionó
                fila += f"[{isla.mapa[i][j].nombre[:1]}] "  # Muestra primeras letras del objeto
            else:
                fila += "[?] " # Celda sin descubrir
        print(fila)# se imprime el mapa actual
    print("\n")#saltos de pagina para recorrer columnas

def jugar():
    print("El mapa es de 6*6")#aviso pa q no te salgas we
    jugador = Jugador("Explorador Teemo de servicio") #iniciamos al jugador
    isla = Isla()#iniciamos la isla
    
    while jugador.vidas > 0:# mientras q el vato tenga mas vidas q 0
        mostrar_mapa(isla, jugador)
        jugador.mostrar_estado()# se actualiza estado y se muestra menu
        try:
            x, y = map(int, input("Ingresa coordenadas para explorar (fila columna): ").split())  # Se guarda x e y
            resultado = isla.explorar(x, y, jugador)  # Hace la exploración con parámetros

            if resultado == "🗝️Llave":  # Si el jugador encuentra la llave, gana
                print("🏆")
                break
            elif resultado == "🐊Cocodrilazo":  # Si encuentra un cocodrilo, pierde
                print("Perdiste ue🐊")
                break

        except ValueError:  # Si hay un error en la captura
            print("⚠️ Entrada inválida, usa números separados por espacio.")
    
    print("🌴 ¡Gracias por jugar! Fin del juego.")
    mostrar_mapa(isla, jugador)

def menu():  # Función que maneja el menú
    while True:
        print("\nOpciones:")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugar()  # Llama a la función jugar
        elif opcion == "2":
            print("🌴 ¡Nos vemos pronto!")
            sys.exit()  # Sale del programa
        else:
            print("⚠️ Opción inválida, elige una opción correcta.")

menu()  