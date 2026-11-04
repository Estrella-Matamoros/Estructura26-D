import pygame
import Sprites
#practica11
pygame.init()


# Configuracion de pantalla
ancho_pantalla = 800
alto_pantalla = 600

pantalla = pygame.display.set_mode(
    (ancho_pantalla, alto_pantalla)
)

pygame.display.set_caption("Practica 11")

reloj = pygame.time.Clock()


# Crear personaje que controla el usuario
personaje = Sprites.Personaje(
    100, 300, 80, 80,
    "imagen1.jpg", 6
)


# Crear enemigo que persigue al personaje
enemigo = Sprites.EnemigoPerseguidor(
    600, 400, 80, 80,
    "imagen1.jpg", pantalla
)


# Ciclo principal
ejecutando = True

while ejecutando:

    # Movimiento del personaje
    ejecutando = personaje.muevete()

    # Fondo negro
    pantalla.fill((0, 0, 0))

    # Movimiento del enemigo siguiendo al personaje
    enemigo.muevete(personaje)

    # Dibujar enemigo
    enemigo.dibujate()

    # Dibujar personaje
    personaje.dibujate()

    # Detectar colision
    if personaje.estaChocando(enemigo.rect):
        print("¡El enemigo atrapo al personaje!")

    # Actualizar pantalla
    pygame.display.update()

    reloj.tick(60)


pygame.quit()