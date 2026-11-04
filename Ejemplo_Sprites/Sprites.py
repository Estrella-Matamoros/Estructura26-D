import pygame
#prectica11
pygame.init()


# PERSONAJE QUE CONTROLA EL USUARIO
class Personaje(pygame.sprite.Sprite):

    def __init__(self, x, y, ancho, alto, imagen, velocidad):
        super().__init__()

        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(
            self.image, (ancho, alto)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.pantalla = pygame.display.get_surface()
        self.velocidad = velocidad

    def muevete(self):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad

        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad

        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad

        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

        return True

    def dibujate(self):
        self.pantalla.blit(self.image, self.rect)

    def estaChocando(self, rect):
        return self.rect.colliderect(rect)


# NUEVA CLASE: ENEMIGO QUE PERSIGUE AL PERSONAJE
class EnemigoPerseguidor(pygame.sprite.Sprite):

    def __init__(self, x, y, ancho, alto, imagen, pantalla):
        super().__init__()

        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(
            self.image, (ancho, alto)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.pantalla = pantalla
        self.velocidad = 2

    def muevete(self, personaje):

        # Sigue al personaje horizontalmente
        if self.rect.x < personaje.rect.x:
            self.rect.x += self.velocidad

        elif self.rect.x > personaje.rect.x:
            self.rect.x -= self.velocidad

        # Sigue al personaje verticalmente
        if self.rect.y < personaje.rect.y:
            self.rect.y += self.velocidad

        elif self.rect.y > personaje.rect.y:
            self.rect.y -= self.velocidad

    def dibujate(self):
        self.pantalla.blit(self.image, self.rect)