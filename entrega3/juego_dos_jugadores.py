import pygame
from pygame import image, transform, display, Rect
import random

def juego_de_2_jugadores(screen):                               ##Aca se empieza a configurar el modo de 2 jugadores
    font = pygame.font.Font(None, 36)

    x = 100
    y = 250

    m = 100
    s = 450

    w = 1200

    u = 2

    y1 = random.randint(1, 5)
    y2 = random.randint(1, 5)
    y3 = random.randint(1, 5)
    t = y1 * 100
    l = y2 * 100
    p = y3 * 100

    vidas1 = 3
    vidas2 = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(fondo, (0, 0))                                                                           ##declara las variables x e y de los objetos, autos y el fondo
        screen.blit(auto, (x, y))
        screen.blit(auto2, (m, s))
        screen.blit(objeto1, (w, t))
        screen.blit(objeto3, (w, l))
        screen.blit(objeto2, (w, p))

        vidas_txt1 = font.render(f"Vidas1: {vidas1}", True, (255, 0, 0))                                    ##Aca se posiciona el contador de vidas en pantalla
        screen.blit(vidas_txt1, (100, 5))

        vidas_txt2 = font.render(f"Vidas2: {vidas2}", True, (255, 0, 0))
        screen.blit(vidas_txt2, (1200, 5))

        w = w - u
        if w < -10:                                     ##Establece el movimiento constante de los objetos
            w = 1200
            y1 = random.randint(1, 5)
            y2 = random.randint(1, 5)
            y3 = random.randint(1, 5)
            t = y1 * 100
            l = y2 * 100
            p = y3 * 100
            u += 0.5

        teclas = pygame.key.get_pressed()               ##define las teclas para el movimiento de los jugadores
        if teclas[pygame.K_LEFT]:
            x -= 1
        if teclas[pygame.K_RIGHT]:
            x += 1
        if teclas[pygame.K_UP]:
            y -= 2
        if teclas[pygame.K_DOWN]:
            y += 2

        if teclas[pygame.K_a]:
            m -= 1
        if teclas[pygame.K_d]:
            m += 1
        if teclas[pygame.K_w]:
            s -= 2
        if teclas[pygame.K_s]:
            s += 2

        auto_rect = Rect(x, y, 150, 80)                     ##esto establece las hitboxs de los objetos
        auto2_rect = Rect(m, s, 150, 80)
        objeto1_rect = Rect(w, t, 150, 80)
        objeto2_rect = Rect(w, l, 150, 80)
        objeto3_rect = Rect(w, p, 150, 80)

        if auto_rect.colliderect(objeto1_rect) or auto_rect.colliderect(objeto2_rect) or auto_rect.colliderect(
                objeto3_rect):                              ##esto detecta las colisiones entre los objetos y los autos para descontar vidas

            vidas1 -= 1

            x = 100
            y = 250

            w = 1200
            y1 = random.randint(1, 5)
            y2 = random.randint(1, 5)
            y3 = random.randint(1, 5)
            t = y1 * 100
            l = y2 * 100
            p = y3 * 100

            pygame.time.delay(100)

            if vidas1 == 0:
                font = pygame.font.Font(None, 48)
                while True:                                         ##esto cambia del fondo a la pantalla final donde te muestra la puntuacion y te da opcion de jugar de vuelta
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                    teclas = pygame.key.get_pressed()
                    if teclas[pygame.K_n]:
                        break
                    if teclas[pygame.K_y]:
                        juego_de_2_jugadores(screen)

                    screen.blit(final1, (0, 0))
                    ganador2 = font.render(" jugador 1 a perdido", True, (255, 255, 255))
                    screen.blit(ganador2, (550, 340))
                    pygame.display.flip()
        if auto2_rect.colliderect(objeto1_rect) or auto2_rect.colliderect(objeto2_rect) or auto2_rect.colliderect(
                objeto3_rect):

            vidas2 -= 1

            m = 100
            s = 450

            w = 1200
            y1 = random.randint(1, 5)
            y2 = random.randint(1, 5)
            y3 = random.randint(1, 5)
            t = y1 * 100
            l = y2 * 100
            p = y3 * 100

            pygame.time.delay(100)

            if vidas2 == 0:
                font = pygame.font.Font(None, 48)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                    teclas = pygame.key.get_pressed()

                    if teclas[pygame.K_n]:
                        break
                    if teclas[pygame.K_y]:
                        juego_de_2_jugadores(screen)

                    screen.blit(final1, (0, 0))
                    ganador1 = font.render(" jugador 2 a perdido", True, (255, 255, 255))
                    screen.blit(ganador1, (550, 340))
                    pygame.display.flip()
        if teclas[pygame.K_n]:
            break
        if teclas[pygame.K_x]:
            break

        pygame.display.flip()                       ##Esto lo que hace es borrar todos los objetos de la pantalla y dibujarlos de vuelta en su nueva ubicacion con sus respectivos tamaños

        screen.blit(fondo, (0, 0))
        screen.blit(auto, (200, 270))
        screen.blit(auto2, (200, 470))
        screen.blit(objeto1, (100, 200))
        screen.blit(objeto3, (100, 200))
        screen.blit(objeto2, (100, 200))

screen = display.set_mode((1380, 720))                     ##en esta parte del codigo lo que se hace es declarar variables de imagenes

menu = image.load("MENU HECHO.png")
menu = transform.scale(menu, (1380, 720))

garage = image.load("garage.png")
garage = transform.scale(garage, (1380, 720))

puestos = image.load("RAANQUIN.png")
puestos = transform.scale(puestos, (1380, 720))

fondo = image.load("fondo.jpeg")
fondo = transform.scale(fondo, (1380, 720))

final1 = image.load("pantalla final 1.png")
final1 = transform.scale(final1, (1380, 720))

auto = image.load("auto prinsipal.png")
auto = transform.scale(auto, (150, 100))

auto2 = image.load("auto2.png")
auto2 = transform.scale(auto2, (160, 100))

auto3 = image.load("auto3.png")
auto3 = transform.scale(auto3, (160, 100))

objeto1 = image.load("objeto1-removebg-preview.png")
objeto1 = transform.scale(objeto1, (200, 100))

objeto2 = image.load("obstaculo2.png")
objeto2 = transform.scale(objeto2, (200, 100))

objeto3 = image.load("objeto3.png")
objeto3 = transform.scale(objeto3, (200, 100))


