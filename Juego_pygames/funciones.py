import pygame
import csv
import random
from constantes import *
def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def mostrar_datos_juego_pygame(pantalla: pygame.Surface, datos_juego: dict):
    mostrar_texto(pantalla, f"Puntuación: {datos_juego.get('puntuacion', 0)}", (10, 35), FUENTE_ARIAL_20, pygame.Color("white"))
    mostrar_texto(pantalla, f"Vidas: {datos_juego.get('vidas', 0)}", (10, 60), FUENTE_ARIAL_20, pygame.Color("white"))

# def mostrar_datos_juego_pygame(pantalla:pygame.Surface, datos_juego:dict):
#     mostrar_texto(pantalla,f"Tiempo restante: {datos_juego.get('tiempo_restante')} s",(10,10),FUENTE_ARIAL_20)
#     mostrar_texto(pantalla,f"Puntuacion: {datos_juego.get('puntuacion')}",(10,35),FUENTE_ARIAL_20)
#     mostrar_texto(pantalla,f"Vidas: {datos_juego.get('cantidad_vidas')}",(10,60),FUENTE_ARIAL_20)

def leer_preguntas_csv(ruta_archivo: str) -> list:
    """
    Lee el archivo CSV y devuelve una lista de preguntas.
    Cada pregunta es un diccionario con:
    - 'pregunta'
    - 'opciones': lista de 4 strings
    - 'correcta': texto de la opción correcta
    """
    preguntas = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        next(lector, None)  # saltamos la primera fila (encabezado)

        for fila in lector:
            if len(fila) >= 6:
                texto_pregunta = fila[0]
                opciones = [fila[1], fila[2], fila[3], fila[4]]
                correcta = fila[5]
                pregunta = {
                    "pregunta": texto_pregunta,
                    "opciones": opciones,
                    "correcta": correcta
                }
                preguntas.append(pregunta)

    return preguntas

def crear_datos_juego() -> dict:
    datos = {
        "puntuacion": 0,
        "vidas": CANTIDAD_VIDAS,
        "indice": 0,
        "tiempo_restante": TIEMPO_TOTAL
    }
    return datos

def mezclar_preguntas(lista_preguntas: list) -> None:
    """
    Mezcla la lista de preguntas de forma aleatoria.
    Modifica la lista original.
    """
    if len(lista_preguntas) > 0:
        random.shuffle(lista_preguntas)

def verificar_respuesta(pregunta_actual: dict, respuesta_usuario, datos_juego: dict) -> bool:
    """
    Verifica si la respuesta seleccionada es correcta.
    Actualiza la puntuación y las vidas del jugador.
    Retorna True si fue correcta, False en caso contrario.
    """
    es_correcta = False

    if type(pregunta_actual) == dict and "correcta" in pregunta_actual:
        correcta = pregunta_actual["correcta"]

        # Comparación directa del texto (modo Pygame)
        if respuesta_usuario == correcta:
            modificar_puntuacion(datos_juego, PUNTOS_ACIERTO)
            es_correcta = True
        else:
            modificar_puntuacion(datos_juego, PUNTOS_ERROR)
            modificar_vida(datos_juego, -1)

    return es_correcta

def modificar_puntuacion(datos: dict, incremento: int):
    """
    Suma o resta puntos según 'incremento'.
    """
    if "puntuacion" in datos:
        datos["puntuacion"] = datos["puntuacion"] + incremento

def obtener_pregunta_actual(datos: dict, preguntas: list) -> dict | None:
    """
    Devuelve la pregunta correspondiente al índice actual.
    Si el índice está fuera de rango, devuelve None.
    """
    pregunta_actual = None
    if "indice" in datos:
        indice = datos["indice"]
        if indice >= 0 and indice < len(preguntas):
            pregunta_actual = preguntas[indice]
    return pregunta_actual


def modificar_vida(datos: dict, incremento: int):
    """
    Suma o resta vidas según 'incremento'.
    """
    if "vidas" in datos:
        datos["vidas"] = datos["vidas"] + incremento


def avanzar_pregunta(datos: dict, preguntas: list):
    """
    Avanza al siguiente índice de pregunta.
    Si se acaban las preguntas, vuelve a mezclar y reinicia el índice.
    """
    if "indice" in datos:
        datos["indice"] = datos["indice"] + 1
        if datos["indice"] >= len(preguntas):
            datos["indice"] = 0
            mezclar_preguntas(preguntas)