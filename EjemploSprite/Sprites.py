
import pygame


class Sprite:
    def __init__(self, x, y, w, h, archivo_imagen, pantalla):
        self.rect = pygame.Rect(x, y, w, h)
        self.imagen = pygame.image.load(archivo_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (w, h))
        self.pantalla = pantalla

    def dibujate(self):
        self.pantalla.blit(self.imagen, self.rect)

    def estaChocando(self, otro):
        return self.rect.colliderect(otro)


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
            self.velocidad = -abs(self.velocidad)

        elif self.rect.left <= self.x_min:
            self.rect.left = self.x_min
            self.velocidad = abs(self.velocidad)

        self.dibujate()


class Personaje(Sprite):
    def __init__(self, x, y, w, h, archivo_imagen,
                 pantalla, vel_base):
        super().__init__(x, y, w, h, archivo_imagen, pantalla)
        self.velocidad = vel_base
        self.vel_x = 0
        self.vel_y = 0

    def alternar(self, vx, vy):
        if self.vel_x == vx and self.vel_y == vy:
            self.vel_x = 0
            self.vel_y = 0
        else:
            self.vel_x = vx
            self.vel_y = vy

    def muevete(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False

                if evento.key == pygame.K_RIGHT:
                    self.alternar(self.velocidad, 0)

                elif evento.key == pygame.K_LEFT:
                    self.alternar(-self.velocidad, 0)

                elif evento.key == pygame.K_UP:
                    self.alternar(0, -self.velocidad)

                elif evento.key == pygame.K_DOWN:
                    self.alternar(0, self.velocidad)

        # Movimiento del personaje
        if self.vel_x != 0 and self.vel_y != 0:
            self.rect.x += round(self.vel_x * 0.707)
            self.rect.y += round(self.vel_y * 0.707)
        else:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

        # Evitar que salga de la ventana
        limite = self.pantalla.get_rect()

        if not limite.contains(self.rect):
            self.rect.clamp_ip(limite)
            self.vel_x = 0
            self.vel_y = 0

        self.dibujate()
        return True