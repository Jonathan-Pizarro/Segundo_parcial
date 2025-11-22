import pygame
from constantes import *
from utilidades.botones import *
from funciones import *

def mostrar_juego():
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Preguntados - Juego")

    fuente_titulo = pygame.font.SysFont("Arial", 50)
    fuente_texto = pygame.font.SysFont("Arial", 28)

    # === Inicialización ===
    preguntas = leer_preguntas_csv(RUTA_PREGUNTAS_CSV)
    datos = crear_datos_juego()
    siguiente_ventana = "menu"  # valor por defecto

    # Si no hay preguntas, volvemos al menú
    if len(preguntas) == 0:
        print("⚠️ No hay preguntas disponibles.")
        pygame.time.wait(2000)
        return siguiente_ventana

    # === Rectángulos de opciones ===
    opciones_rect = []
    for i in range(4):
        opciones_rect.append(pygame.Rect(150, 250 + (i * 70), 700, 50))

    boton_volver = pygame.Rect(ANCHO // 2 - 150, ALTO - 100, 300, 60)

    ejecutando = True
    while ejecutando:
        pantalla.fill((10, 20, 40))
        pregunta = obtener_pregunta_actual(datos, preguntas)

        # === Dibujar elementos ===
        titulo = fuente_titulo.render("PREGUNTADOS", True, (255, 255, 255))
        pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 40))

        mostrar_datos_juego_pygame(pantalla, datos)

        if pregunta is not None:
            texto_pregunta = fuente_texto.render(pregunta["pregunta"], True, (240, 240, 240))
            pantalla.blit(texto_pregunta, (100, 150))

            for i in range(4):
                pygame.draw.rect(pantalla, (60, 100, 200), opciones_rect[i], border_radius=8)
                texto_opcion = fuente_texto.render(f"{i+1}) {pregunta['opciones'][i]}", True, (255, 255, 255))
                pantalla.blit(texto_opcion, (opciones_rect[i].x + 15, opciones_rect[i].y + 10))

        # === Eventos ===
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                siguiente_ventana = "salir"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Clic en opciones
                for i in range(4):
                    if opciones_rect[i].collidepoint(pos):
                        # usamos tu función ya hecha
                        respuesta_correcta = verificar_respuesta(pregunta, pregunta["opciones"][i], datos)

                        if datos["vidas"] > 0:
                            avanzar_pregunta(datos, preguntas)
                        else:
                            ejecutando = False

                # Clic en volver
                if boton_volver.collidepoint(pos):
                    ejecutando = False
                    siguiente_ventana = "menu"

        pygame.display.update()

    return siguiente_ventana