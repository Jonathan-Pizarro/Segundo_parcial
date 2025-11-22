import pygame
from constantes import *
from utilidades.botones import *
from ranking import cargar_ranking

def mostrar_ranking():
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Ranking")

    boton_volver = pygame.Rect(ANCHO//2 - 150, ALTO - 120, 300, 60)
    fuente = pygame.font.SysFont("Arial", 48)
    fuente_lista = pygame.font.SysFont("Arial", 32)

    ejecutando = True
    while ejecutando:
        pantalla.fill((50,50,80))

        titulo = fuente.render("RANKING", True, (255,255,255))
        pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 40))

        ranking = cargar_ranking()

        y = 150
        for nombre, puntos in ranking:
            texto = fuente_lista.render(f"{nombre} — {puntos}", True, (255,255,255))
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, y))
            y += 40

        color_volver = (200,120,100) if mouse_sobre_boton(boton_volver) else (160,90,70)
        dibujar_boton(pantalla, boton_volver, "VOLVER", color_volver, (255,255,255))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if mouse_sobre_boton(boton_volver):
                    return "menu"

        pygame.display.update()