import os

# Carpeta donde está este archivo (Constantes.py)
BASE = os.path.dirname(os.path.abspath(__file__))

# Rutas absolutas a los CSV
RUTA_PREGUNTAS_CSV = os.path.join(BASE, "preguntas.csv")
RUTA_RANKING_CSV = os.path.join(BASE, "ranking.csv")

# Configuración del juego
CANTIDAD_VIDAS = 3
PUNTOS_ACIERTO = 100
PUNTOS_ERROR = -25