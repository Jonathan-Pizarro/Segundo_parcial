import pygame
from constantes import *
from ventanas.menu import *
from ventanas.juego import *
from ventanas.ranking import *
from ventanas.configuracion import *

pygame.init()

def main():
    ventana_actual = "menu"

    while True:
        if ventana_actual == "menu":
            ventana_actual = mostrar_menu()

        elif ventana_actual == "juego":
            ventana_actual = mostrar_juego()

        elif ventana_actual == "ranking":
            ventana_actual = mostrar_ranking()

        elif ventana_actual == "configuracion":
            ventana_actual = mostrar_configuracion()

        elif ventana_actual == "salir":
            break

    pygame.quit()


main()