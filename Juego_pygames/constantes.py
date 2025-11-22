import pygame
pygame.init()

COLOR_JUEGO = (10, 40, 60)
BLANCO = (255, 255, 255)
COLOR_FONDO = (20, 20, 40)
FUENTE_ARIAL_20 = pygame.font.SysFont("Arial",20,False)
FUENTE_ARIAL_30 = pygame.font.SysFont("Arial",30,False)

# =============================
# CONFIGURACIÓN GENERAL DEL JUEGO
# =============================

ANCHO = 900
ALTO = 600
COLOR_MENU = (50, 90, 160)

# =============================
# REGLAS DE PUNTUACIÓN Y VIDAS
# =============================

CANTIDAD_VIDAS = 3
TIEMPO_TOTAL = 60
PUNTOS_ACIERTO = 100
PUNTOS_ERROR = -25

# =============================
# ARCHIVOS
# =============================

RUTA_PREGUNTAS_CSV = "Juego_pygames/preguntas.csv"
RUTA_RANKING_CSV = "Juego_pygames/ranking.csv"

# =============================
# FUENTES Y OTROS AJUSTES
# =============================

FUENTE_PRINCIPAL = "Arial"
TAM_TITULO = 60
TAM_TEXTO = 32