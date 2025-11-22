import pygame
from constantes import *
from utilidades.botones import *


def mostrar_menu():
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Preguntados - Menú")

    ejecutando = True

    # Rectángulos de botones
    boton_jugar = pygame.Rect(ANCHO//2 - 150, ALTO//2 - 50, 300, 60)
    boton_ranking = pygame.Rect(ANCHO//2 - 150, ALTO//2 + 30, 300, 60)
    boton_config = pygame.Rect(ANCHO//2 - 150, ALTO//2 + 110, 300, 60)
    boton_salir = pygame.Rect(ANCHO//2 - 150, ALTO//2 + 190, 300, 60)

    fuente_titulo = pygame.font.SysFont("Arial", 60)

    while ejecutando:
        pantalla.fill(COLOR_MENU)

        # TÍTULO
        texto = fuente_titulo.render("PREGUNTADOS", True, (240, 240, 240))
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 90))

        # Colores dinámicos sin ternarios
        if mouse_sobre_boton(boton_jugar):
            color_jugar = (60, 200, 120)
        else:
            color_jugar = (40, 160, 90)

        if mouse_sobre_boton(boton_ranking):
            color_ranking = (120, 150, 220)
        else:
            color_ranking = (90, 120, 190)

        if mouse_sobre_boton(boton_config):
            color_config = (200, 180, 80)
        else:
            color_config = (170, 150, 50)

        if mouse_sobre_boton(boton_salir):
            color_salir = (220, 80, 80)
        else:
            color_salir = (180, 50, 50)

        # DIBUJAR BOTONES (reutilizando utilidades)
        dibujar_boton(pantalla, boton_jugar, "JUGAR", color_jugar, (255, 255, 255))
        dibujar_boton(pantalla, boton_ranking, "RANKING", color_ranking, (255, 255, 255))
        dibujar_boton(pantalla, boton_config, "CONFIG", color_config, (255, 255, 255))
        dibujar_boton(pantalla, boton_salir, "SALIR", color_salir, (255, 255, 255))

        # EVENTOS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if mouse_sobre_boton(boton_jugar):
                    return "juego"
                if mouse_sobre_boton(boton_ranking):
                    return "ranking"
                if mouse_sobre_boton(boton_config):
                    return "configuracion"
                if mouse_sobre_boton(boton_salir):
                    return "salir"

        pygame.display.update()