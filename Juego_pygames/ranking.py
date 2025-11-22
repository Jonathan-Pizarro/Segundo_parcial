import json
from datetime import datetime

RUTA_RANKING = "partidas.json"


def cargar_ranking() -> list:
    """
    Carga el ranking desde partidas.json.
    Si no existe, devuelve lista vacía.
    """
    try:
        with open(RUTA_RANKING, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos
    except:
        return []


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