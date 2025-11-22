import pygame
from constantes import *
from utilidades.botones import dibujar_boton, mouse_sobre_boton


def mostrar_configuracion():
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Preguntados - Configuración")

    ejecutando = True

    # Botón VOLVER
    boton_volver = pygame.Rect(ANCHO//2 - 150, ALTO - 150, 300, 60)
    fuente_titulo = pygame.font.SysFont("Arial", 60)

    while ejecutando:
        pantalla.fill((70, 70, 70))  # Fondo gris oscuro

        # -------------------------
        # TÍTULO
        # -------------------------
        texto = fuente_titulo.render("CONFIGURACIÓN", True, (255, 255, 255))
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 80))

        # -------------------------
        # BOTÓN VOLVER 
        # -------------------------
        color_volver = (130, 80, 180)

        if mouse_sobre_boton(boton_volver):
            color_volver = (160, 110, 210)

        dibujar_boton(pantalla, boton_volver, "VOLVER", color_volver, (255, 255, 255))

        # -------------------------
        # EVENTOS
        # -------------------------
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if mouse_sobre_boton(boton_volver):
                    return "menu"

        pygame.display.update()