import pygame
import Sprites


pygame.init()


# Cada nodo se va a guardar un enemigo y un enlace al nodo de la lista
class nodo:
    def __init__(self, enemigo):
        self.enemigo = enemigo     
        self.siguiente = None       


# Esto es la lista enlazada que guarda los enemigos uno atras de otro
class lista_enlazada:
    def __init__(self):
        self.cabeza = None             
        self.cola = None         
        self.tamano = 0          

    # Se va a agregar un enemigo al final de la lista
    def agregar(self, enemigo):
        nuevo = nodo(enemigo)
        if self.cabeza is None:     
            self.cabeza = nuevo     
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo  
            self.cola = nuevo           
        self.tamano += 1

    # permite que se vaya recorriendo la lista con un for 
    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.enemigo   
            actual = actual.siguiente  


ancho_pantalla = 800
alto_pantalla = 600
ancho_enemigo = 70
alto_enemigo = 70


pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
reloj = pygame.time.Clock()


enemigo1 = Sprites.Enemigo1(100, 100, 80, 80, "imagen1.jpg", pantalla, 0, 700)
personaje = Sprites.Personaje(100, 300, 80, 80, "imagen1.jpg", pantalla, 6)

# Lista enlazada con los 20 enemigos
lista_enemigos = lista_enlazada()
for i in range(20):
    x_min = (i % 5) * 50                    
    x_max = ancho_pantalla - (i % 5) * 30  
    x = x_min + i * 15                      
    y = i * 27                              
    velocidad = 2 + i // 2                  

    # Creamos el enemigo con sus datos
    enemigo = Sprites.Enemigo2(x, y, ancho_enemigo, alto_enemigo,"imagen1.jpg", pantalla,x_min, x_max, velocidad)   
                               
    lista_enemigos.agregar(enemigo)   
    
ejecutando = True
while ejecutando:
   
    ejecutando = personaje.muevete()

  
    pantalla.fill((0, 0, 0))

    
    enemigo1.muevete()
    
    if personaje.estaChocando(enemigo1.rect):
        print("El enemigo toco al jugador ")

    # Se va estar reccorriendo la lista enlazada
    for enemigo in lista_enemigos:
        enemigo.muevete()                          
        if personaje.estaChocando(enemigo.rect):    
            print("El enemigo toco al jugador ")

   
    personaje.dibujate()

    
    pygame.display.update()
   
    reloj.tick(60)


pygame.quit()
