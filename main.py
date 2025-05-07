from jugador import Jugador
from isla import Isla#importaciones

def mostrar_mapa(isla, jugador): #se dibuja el mapa con lo que ha descubierto el jugador
    print("\n📜 Mapa de la isla:")# un mensaje del mapa
    for i in range(6):
        fila = ""
        for j in range(6):
            if (i, j) in jugador.exploradas:# toma lo que el jugador avanzo o seleccionó
                fila += f"[{isla.mapa[i][j].nombre[:2]}] "  # Muestra primeras letras del objeto
            else:
                fila += "[??] "  # Celda sin descubrir
        print(fila)# se imprime el mapa actual
    print("\n")#saltos de pagina para recorrer columnas

def jugar():
    print("El mapa es de 5*5")#aviso pa q no te salgas we
    jugador = Jugador("Explorador Teemo de servicio") #iniciamos al jugador
    isla = Isla()#iniciamos la isla
    
    while jugador.vidas > 0:# mientras q el vato tenga mas vidas q 0
        jugador.mostrar_estado()# se actualiza estado y se muestra menu
        print("\nOpciones:")
        print("1. Explorar una celda")
        print("2. Ver mapa")
        print("3. Salir")
        opcion = input("Elige una opción: ")# introduce opc

        if opcion == "1":# cuando sea 1 explorar celda

            try:
                x, y = map(int, input("Ingresa coordenadas (fila columna): ").split())#se guarda x y y
                resultado = isla.explorar(x, y, jugador)# hace la exploracion con parametros llamando funcion de isla
                
                if resultado == "Llave": #depende que encontraste
                    print("🏆")
                    break
                elif resultado == "Cocodrilazo":
                    print("Perdiste 🐊")
                    break

            except ValueError: #si hay un error en la captura
                print("⚠️ Entrada inválida, usa números separados por espacio.")

        elif opcion == "2":  # Ver el mapa
            mostrar_mapa(isla, jugador)#muestra mapa

        elif opcion == "3":  # Salir
            print("🌴 ¡Gracias por jugar! Nos vemos pronto.")
            break

        else:
            print("⚠️ Opción inválida, elige una opción del menú.")

    print("Fin del juego.")

jugar()