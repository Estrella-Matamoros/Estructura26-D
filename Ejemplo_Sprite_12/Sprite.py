import pygame
import csv
from pathlib import Path
import math

BASE_DIR = Path(__file__).resolve().parent


# CLASE SPRITE
class Sprite:

    def __init__(self, x, y, w, h, archivo_imagen, pantalla):

        self.rect = pygame.Rect(x, y, w, h)

        ruta = Path(archivo_imagen)

        if not ruta.is_absolute():
            ruta = BASE_DIR / ruta

        self.imagen = pygame.image.load(
            str(ruta)
        ).convert_alpha()

        self.imagen = pygame.transform.scale(
            self.imagen, (w, h)
        )

        self.pantalla = pantalla

    def dibujate(self):
        self.pantalla.blit(self.imagen, self.rect)

    def estaChocando(self, otro):
        return self.rect.colliderect(otro)


# ENEMIGO 1
class Enemigo1(Sprite):

    def __init__(self, x, y, w, h, archivo_imagen,
                 pantalla, x_min, x_max):

        super().__init__(x, y, w, h, archivo_imagen, pantalla)

        self.x_min = x_min
        self.x_max = x_max
        self.velocidad = 7

    def muevete(self):

        self.rect.x += self.velocidad

        if self.rect.right >= self.x_max:
            self.rect.right = self.x_max
            self.velocidad = -self.velocidad

        elif self.rect.left <= self.x_min:
            self.rect.left = self.x_min
            self.velocidad = -self.velocidad

        self.dibujate()


# ENEMIGO 2
class Enemigo2(Sprite):

    def __init__(self, x, y, w, h, archivo_imagen,
                 pantalla, x_min, x_max, velocidad):

        super().__init__(x, y, w, h, archivo_imagen, pantalla)

        self.x_min = x_min
        self.x_max = x_max
        self.velocidad = velocidad

    def muevete(self):

        self.rect.x += self.velocidad

        if self.rect.right >= self.x_max:
            self.rect.right = self.x_max
            self.velocidad = -self.velocidad

        elif self.rect.left <= self.x_min:
            self.rect.left = self.x_min
            self.velocidad = -self.velocidad

        self.dibujate()


# ENEMIGO 3
class Enemigo3(Sprite):

    def __init__(self, x, y, w, h, archivo_imagen,
                 pantalla, velocidad):

        super().__init__(x, y, w, h, archivo_imagen, pantalla)

        self.velocidad = velocidad
        self.pos_x = float(x)
        self.pos_y = float(y)

    def muevete(self, objetivo):

        dx = objetivo.centerx - self.rect.centerx
        dy = objetivo.centery - self.rect.centery

        distancia = math.hypot(dx, dy)

        if distancia > self.velocidad:

            self.pos_x += dx / distancia * self.velocidad
            self.pos_y += dy / distancia * self.velocidad

            self.rect.x = round(self.pos_x)
            self.rect.y = round(self.pos_y)

        self.dibujate()


# PERSONAJE
class Personaje(Sprite):

    def __init__(self, x, y, w, h, archivo_imagen,
                 pantalla, vel_base):

        super().__init__(x, y, w, h, archivo_imagen, pantalla)

        self.velocidad = vel_base

    def muevete(self, obstaculos):

        # Revisar si se quiere cerrar el juego
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    return False

        # Leer las teclas
        teclas = pygame.key.get_pressed()

        movimiento_x = 0
        movimiento_y = 0

        if teclas[pygame.K_RIGHT]:
            movimiento_x = self.velocidad

        if teclas[pygame.K_LEFT]:
            movimiento_x = -self.velocidad

        if teclas[pygame.K_UP]:
            movimiento_y = -self.velocidad

        if teclas[pygame.K_DOWN]:
            movimiento_y = self.velocidad

        # Evitar mayor velocidad en diagonal
        if movimiento_x != 0 and movimiento_y != 0:

            movimiento_x = round(movimiento_x * 0.707)
            movimiento_y = round(movimiento_y * 0.707)

        # MOVIMIENTO HORIZONTAL
        self.rect.x += movimiento_x

        # Revisar choque con ladrillos
        if obstaculos.estaChocando(self.rect):

            self.rect.x -= movimiento_x

        # MOVIMIENTO VERTICAL
        self.rect.y += movimiento_y

        # Revisar choque con ladrillos
        if obstaculos.estaChocando(self.rect):

            self.rect.y -= movimiento_y

        # No salir de la pantalla
        limite = self.pantalla.get_rect()
        self.rect.clamp_ip(limite)

        return True


# NODO
class Nodo:

    def __init__(self, dato):

        self.dato = dato
        self.siguiente = None


# LISTA ENLAZADA
class ListaSprites:

    def __init__(self):

        self.primero = None

    def insertarInicio(self, sprite):

        nuevo = Nodo(sprite)
        nuevo.siguiente = self.primero
        self.primero = nuevo

    def dibujarElementos(self):

        actual = self.primero

        while actual is not None:

            actual.dato.dibujate()
            actual = actual.siguiente

    def estaChocando(self, otro):

        actual = self.primero

        while actual is not None:

            if actual.dato.estaChocando(otro):
                return True

            actual = actual.siguiente

        return False


# MAPA
class Mapa:

    def __init__(self, pantalla):

        self.Tiles = ListaSprites()
        self.pantalla = pantalla

    def inicializarMapa1(self):

        for i in range(10):

            sprite = Sprite(
                50 * i, 100, 50, 50,
                "imagen2.png", self.pantalla
            )

            self.Tiles.insertarInicio(sprite)

    def cargarMapaCSV(self, archivo):

        ruta = Path(archivo)

        if not ruta.is_absolute():
            ruta = BASE_DIR / ruta

        if not ruta.exists():

            raise FileNotFoundError(
                f"No se encontro el archivo: {ruta}"
            )

        with open(
            ruta,
            newline="",
            encoding="utf-8-sig"
        ) as archivo_csv:

            lector = csv.reader(archivo_csv)

            for fila, valores in enumerate(lector):

                for columna, valor in enumerate(valores):

                    if valor.strip() == "1":

                        sprite = Sprite(
                            columna * 50,
                            fila * 50,
                            50,
                            50,
                            "imagen2.png",
                            self.pantalla
                        )

                        self.Tiles.insertarInicio(sprite)

        # Tres ladrillos arriba
        for i in range(3):

            sprite = Sprite(
                250 + (i * 50),
                50,
                50,
                50,
                "imagen2.png",
                self.pantalla
            )

            self.Tiles.insertarInicio(sprite)



