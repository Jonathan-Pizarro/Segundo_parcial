import json
import os
from datetime import datetime

RUTA_RANKING = "partidas.json"


def cargar_ranking() -> list:
    """
    Carga el ranking desde partidas.json.
    Si el archivo no existe, devuelve lista vacía.
    """
    datos = []

    if os.path.exists(RUTA_RANKING):
        archivo = open(RUTA_RANKING, "r", encoding="utf-8")
        contenido = archivo.read()

        if len(contenido) > 0:
            datos = json.loads(contenido)

        archivo.close()

    return datos


def guardar_puntaje(nombre: str, puntaje: int):
    """
    Guarda una nueva entrada en el ranking.
    """
    ranking = cargar_ranking()

    nueva_partida = {
        "nombre": nombre,
        "puntaje": puntaje,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    ranking.append(nueva_partida)

    with open(RUTA_RANKING, "w", encoding="utf-8") as archivo:
        json.dump(ranking, archivo, indent=4, ensure_ascii=False)