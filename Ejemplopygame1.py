import pygame
pygame.init()

pantalla = pygame.display.set_mode((800, 600))
rectangulo = pygame.Rect(0, 0, 40, 40)

x = 0
y = 0

ejecutando = True

while ejecutando:
    pantalla.fill((0, 0, 0))

    rectangulo.left = x
    rectangulo.top = y

    pygame.draw.rect(pantalla, (255, 255, 255), rectangulo)

    teclas = pygame.key.get_pressed()

    # Velocidad normal
    velocidad = 10

   
    if teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]:
        velocidad = 100

    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

            elif evento.key == pygame.K_RIGHT:
                x += velocidad

            elif evento.key == pygame.K_LEFT:
                x -= velocidad

            elif evento.key == pygame.K_UP:
                y -= velocidad

            elif evento.key == pygame.K_DOWN:
                y += velocidad

    pygame.display.update()

pygame.quit()