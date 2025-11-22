import csv
from Constantes import RUTA_RANKING_CSV

# ---------------------------
#   Cargar ranking
# ---------------------------
def cargar_ranking() -> list:
    """
    Lee el archivo CSV del ranking.
    Devuelve una lista de diccionarios: {"nombre": str, "puntaje": int}
    Si el archivo no existe o está vacío: devuelve lista vacía.
    """
    ranking = []

    archivo = open(RUTA_RANKING_CSV, "a", encoding="utf-8")
    archivo.close()

    archivo = open(RUTA_RANKING_CSV, "r", encoding="utf-8")
    lector = csv.reader(archivo, delimiter=";")

    for fila in lector:
        if len(fila) == 2:
            nombre = fila[0]
            puntaje = int(fila[1])
            ranking.append({"nombre": nombre, "puntaje": puntaje})

    archivo.close()
    return ranking


# ---------------------------
#   Guardar puntaje
# ---------------------------
def guardar_puntaje(nombre: str, puntaje: int):
    """
    Agrega una línea al archivo del ranking.
    """
    archivo = open(RUTA_RANKING_CSV, "a", encoding="utf-8")
    archivo.write(f"{nombre};{puntaje}\n")
    archivo.close()


# ---------------------------
#   Mostrar Ranking
# ---------------------------
def mostrar_ranking():
    """
    Carga el ranking, lo ordena y lo muestra en consola.
    """
    ranking = cargar_ranking()

    if len(ranking) == 0:
        print("\nNo hay puntajes guardados.\n")
        return

    # Ordenar de mayor a menor puntaje sin usar sort()
    # Hacemos burbujeo manual para cumplir el parcial
    for i in range(len(ranking) - 1):
        for j in range(len(ranking) - 1 - i):
            if ranking[j]["puntaje"] < ranking[j + 1]["puntaje"]:
                aux = ranking[j]
                ranking[j] = ranking[j + 1]
                ranking[j + 1] = aux

    print("\n===== RANKING GENERAL =====\n")
    for jugador in ranking:
        print(f"{jugador['nombre']} - {jugador['puntaje']} puntos")
    print()