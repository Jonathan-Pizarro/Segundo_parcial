from Funciones import *
from Ranking import *
import os

def mostrar_menu_principal():
    print("====================================")
    print("          🎮 PREGUNTADOS UTN 🎮     ")
    print("====================================")
    print("1) Jugar")
    print("2) Ver Ranking")
    print("3) Salir")
    print("====================================")

def pedir_opcion_menu():
    opcion = input("Seleccione una opción (1-3): ")
    while opcion not in ["1", "2", "3"]:
        opcion = input("Opción inválida. Seleccione (1-3): ")
    return opcion

def main():
    seguir = True
    while seguir == True:
        os.system("cls")
        mostrar_menu_principal()
        opcion = pedir_opcion_menu()

        if opcion == "1":
            jugar_una_partida()

        elif opcion == "2":
            mostrar_ranking()
            input("\nPresione ENTER para volver al menú...")

        elif opcion == "3":
            print("\nSaliendo del juego... ¡Gracias por jugar! 👋")
            seguir = False

main()