import os
import csv
import random

from Constantes import *
from Ranking import *

def es_digito(caracter: str) -> bool:
    """
    Devuelve True si el caracter está entre '0' y '9'
    usando su código ASCII (48 al 57).
    """
    codigo = ord(caracter)
    if codigo >= 48 and codigo <= 57:
        return True
    else:
        return False
    
def es_numero_valido(texto: str) -> bool:
    """
    Devuelve True si TODOS los caracteres del string son dígitos.
    No permite negativos, ni espacios, ni puntos.
    """
    if len(texto) == 0:
        return False

    for i in range(len(texto)):
        if es_digito(texto[i]) == False:
            return False

    return True


# ==========================
# UTILIDAD CONSOLA
# ==========================

def limpiar_pantalla(pausar: bool = False):
    """
    Limpia la pantalla.
    Si pausar=True, primero pausa con ENTER.
    """
    if pausar == True:
        input("\nPresione ENTER para continuar...")

    # Windows
    os.system("cls")


def pedir_opcion_numerica(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    texto = input(mensaje)
    numero = 0
    valido = False

    while valido == False:
        if es_numero_valido(texto):
            numero = int(texto)

            if numero >= minimo and numero <= maximo:
                valido = True
            else:
                texto = input(mensaje_error)
        else:
            texto = input(mensaje_error)

    return numero


# ==========================
# PREGUNTAS (CSV)
# ==========================

def leer_preguntas_csv(ruta_archivo: str) -> list:
    """
    Lee el archivo CSV y devuelve una lista de preguntas.
    """
    preguntas = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        # Saltamos la primera fila (títulos de columnas)
        next(lector, None)
        for fila in lector:
            # Esperamos 6 columnas: pregunta, op1, op2, op3, op4, correcta
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

def mezclar_preguntas(lista_preguntas: list) -> None:
    """
    Mezcla la lista de preguntas de forma aleatoria.
    Modifica la lista original.
    """
    if len(lista_preguntas) > 0:
        random.shuffle(lista_preguntas)


# ==========================
# DATOS DEL JUEGO
# ==========================

def crear_datos_juego() -> dict:
    """
    Crea el diccionario con el estado del juego.
    """
    datos = {
        "puntuacion": 0,
        "vidas": CANTIDAD_VIDAS,
        "indice": 0
    }
    return datos


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


def modificar_puntuacion(datos: dict, incremento: int):
    """
    Suma o resta puntos según 'incremento'.
    """
    if "puntuacion" in datos:
        datos["puntuacion"] = datos["puntuacion"] + incremento


def mostrar_datos_juego(datos: dict):
    """
    Muestra puntuación y vidas actuales.
    """
    print(f"\nVIDAS: {datos.get('vidas', 0)}")
    print(f"PUNTOS: {datos.get('puntuacion', 0)}\n")


# ==========================
# LÓGICA DE PREGUNTAS
# ==========================

def mostrar_pregunta_consola(pregunta: dict):
    """
    Muestra la pregunta y sus 4 opciones numeradas.
    """
    print("=================================")
    print(pregunta["pregunta"])
    print("=================================")
    opciones = pregunta["opciones"]
    print(f"1) {opciones[0]}")
    print(f"2) {opciones[1]}")
    print(f"3) {opciones[2]}")
    print(f"4) {opciones[3]}")
    print("=================================")


def verificar_respuesta(pregunta: dict, indice_opcion: int, datos: dict) -> bool:
    """
    Compara la opción elegida con la correcta.
    Actualiza puntuación y vidas.
    Devuelve True si es correcta, False si es incorrecta.
    """
    es_correcta = False

    opciones = pregunta["opciones"]
    # indice_opcion viene entre 1 y 4 -> lo pasamos a índice de lista (0 a 3)
    respuesta_usuario = opciones[indice_opcion - 1]
    respuesta_correcta = pregunta["correcta"]

    if respuesta_usuario == respuesta_correcta:
        modificar_puntuacion(datos, PUNTOS_ACIERTO)
        es_correcta = True
    else:
        modificar_puntuacion(datos, PUNTOS_ERROR)
        modificar_vida(datos, -1)
        es_correcta = False

    return es_correcta


def mostrar_resultado_pregunta(es_correcta: bool, pregunta: dict):
    """
    Muestra si la respuesta fue correcta o incorrecta
    e informa cuál era la correcta cuando se falla.
    """
    limpiar_pantalla(False)  # limpia sin pausar
    if es_correcta:
        print("✅ ¡Respuesta CORRECTA!")
    else:
        print("❌ Respuesta INCORRECTA.")
        print(f"La respuesta correcta era: {pregunta['correcta']}")
    limpiar_pantalla(True)  # limpia con pausar


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


# ==========================
# JUEGO PRINCIPAL (UNA PARTIDA)
# ==========================

def jugar_una_partida() :
    """
    Ejecuta una partida completa:
    - Carga preguntas desde el CSV
    - Mezcla la lista
    - Maneja vidas y puntuación
    - Al terminar pide nombre y guarda en el ranking
    """
    preguntas = leer_preguntas_csv(RUTA_PREGUNTAS_CSV)
    if len(preguntas) == 0:
        print("No hay preguntas disponibles. Verifique el archivo CSV.")
        limpiar_pantalla(False)  # limpia sin pausar
    else:
        mezclar_preguntas(preguntas)
        datos = crear_datos_juego()

        seguir_jugando = True
        while seguir_jugando == True and datos["vidas"] > 0:
            limpiar_pantalla(False)  # limpia sin pausar
            mostrar_datos_juego(datos)
            pregunta_actual = obtener_pregunta_actual(datos, preguntas)

            if pregunta_actual is None:
                seguir_jugando = False
            else:
                mostrar_pregunta_consola(pregunta_actual)
                opcion = pedir_opcion_numerica(
                    "Elija una opción (1-4): ",
                    "Opción inválida. Elija entre 1 y 4: ",
                    1,
                    4
                )
                es_correcta = verificar_respuesta(pregunta_actual, opcion, datos)
                mostrar_resultado_pregunta(es_correcta, pregunta_actual)

                if datos["vidas"] > 0:
                    avanzar_pregunta(datos, preguntas)
                else:
                    seguir_jugando = False

        limpiar_pantalla(False)  # limpia sin pausar
        print("🎮 GAME OVER 🎮")
        print(f"Puntuación final: {datos['puntuacion']} puntos")
        nombre = input("Ingrese su nombre para el ranking: ")
        if nombre.strip() == "":
            nombre = "Jugador anónimo"
        guardar_puntaje(nombre, datos["puntuacion"])
        limpiar_pantalla(True)  # limpia Con pausar