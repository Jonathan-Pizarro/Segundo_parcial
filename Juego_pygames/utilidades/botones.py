import pygame

def dibujar_boton(pantalla, rect, texto, color_fondo, color_texto):
    pygame.draw.rect(pantalla, color_fondo, rect, border_radius=10)
    fuente = pygame.font.SysFont("Arial", 36)
    superficie_texto = fuente.render(texto, True, color_texto)
    pantalla.blit(
        superficie_texto,
        (rect.x + rect.width//2 - superficie_texto.get_width()//2,
         rect.y + rect.height//2 - superficie_texto.get_height()//2)
    )

def mouse_sobre_boton(rect):
    return rect.collidepoint(pygame.mouse.get_pos())
