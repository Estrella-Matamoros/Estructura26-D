import pygame
import Sprite

# Inicializar pygame
pygame.init()

# Tamaño de pantalla
ancho_pantalla = 800
alto_pantalla = 600

pantalla = pygame.display.set_mode(
    (ancho_pantalla, alto_pantalla)
)

pygame.display.set_caption("Mi videojuego")

reloj = pygame.time.Clock()

# Crear personaje
personaje = Sprite.Personaje(
    500, 500, 80, 80,
    "imagen1.png",
    pantalla,
    6
)

# Crear mapa
mapa = Sprite.Mapa(pantalla)

# Cargar mapa CSV
mapa.cargarMapaCSV("mapa.csv")

# Ciclo principal
ejecutando = True

while ejecutando:

    # Fondo negro
    pantalla.fill((0, 0, 0))

    # Mover personaje y detectar colisiones
    ejecutando = personaje.muevete(mapa.Tiles)

    # Dibujar ladrillos
    mapa.Tiles.dibujarElementos()

    # Dibujar personaje
    personaje.dibujate()

    # Actualizar pantalla
    pygame.display.flip()

    # Velocidad del juego
    reloj.tick(60)

# Cerrar pygame
pygame.quit()