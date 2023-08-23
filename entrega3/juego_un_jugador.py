import pygame
from pygame import image, transform, Rect, display
from ranquin import actualizar_ranquin
import random

def juego_de_1_jugador(screen):                          ##Aca se empieza a configurar el modo de 2 jugadores
    font = pygame.font.Font(None, 36)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(garage, (0, 0))

        pygame.display.flip()

        teclas = pygame.key.get_pressed()                       ##las opciones a b y c son para elejir el auto los trs tienen el mismo codigo la opcion a esta detallado el funcionamiento del juego
        if teclas[pygame.K_x]:
            break
        if teclas[pygame.K_a]:
            x = 100                                           ##Aca se empieza a configurar el juego
            y = 250
            w = 1200
            u = 2

            y1 = random.randint(1, 5)
            y2 = random.randint(1, 5)
            y3 = random.randint(1, 5)
            t = y1 * 100
            l = y2 * 100
            p = y3 * 100

            vidas = 3

            font = pygame.font.Font(None, 36)
            puntos = 0
            tiempo_transcurrido = 0

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                screen.blit(fondo, (0, 0))                                                               ##declara las variables x e y de los objetos, autos y el fondo
                screen.blit(auto, (x, y))
                screen.blit(objeto1, (w, t))
                screen.blit(objeto3, (w, l))
                screen.blit(objeto2, (w, p))

                vidas_txt = font.render(f"Vidas: {vidas}", True, (255, 0, 0))                           ##Aca se posiciona el contador de vidas en pantalla
                screen.blit(vidas_txt, (100, 5))
                puntos_txt = font.render(f"Puntos: {puntos}", True, (0, 0, 0))
                screen.blit(puntos_txt, (100, 40))

                w = w - u

                if w < -10:                                                           ##Establece el movimiento constante de los objetos
                    w = 1200
                    y1 = random.randint(1, 5)
                    y2 = random.randint(1, 5)
                    y3 = random.randint(1, 5)
                    t = y1 * 100
                    l = y2 * 100
                    p = y3 * 100
                    if u < 8:
                        u += 0.5
                        y += 0.2

                teclas = pygame.key.get_pressed()                               ##define las teclas para el movimiento del jugador
                if teclas[pygame.K_LEFT]:
                    x -= 1
                if teclas[pygame.K_RIGHT]:
                    x += 1
                if teclas[pygame.K_UP]:
                    y -= 2
                if teclas[pygame.K_DOWN]:
                    y += 2
                if teclas[pygame.K_a]:
                    x -= 1
                if teclas[pygame.K_d]:
                    x += 1
                if teclas[pygame.K_w]:
                    y -= 2
                if teclas[pygame.K_s]:
                    y += 2

                auto_rect = Rect(x, y, 150, 80)                                       ##esto establece las hitboxs de los objetos
                objeto1_rect = Rect(w, t, 150, 80)
                objeto2_rect = Rect(w, l, 150, 80)
                objeto3_rect = Rect(w, p, 150, 80)

                if x < -30:
                    vidas -= 1
                    x = 100
                    y = 250

                if auto_rect.colliderect(objeto1_rect) or auto_rect.colliderect(
                        objeto2_rect) or auto_rect.colliderect(
                    objeto3_rect):                                                      ##esto detecta las colisiones entre los objetos y los autos para descontar vidas
                    vidas -= 1
                    print("Colisión detectada. Vidas restantes:", vidas)
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

                    if vidas == 0:
                        print(puntos)
                        actualizar_ranquin(puntos)
                        font = pygame.font.Font(None, 48)
                        while True:                                                       ##esto cambia del fondo a la pantalla final donde te muestra la puntuacion y te da opcion de jugar de vuelta
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()
                            teclas = pygame.key.get_pressed()

                            if teclas[pygame.K_n]:
                                break
                            if teclas[pygame.K_y]:
                                juego_de_1_jugador(screen)

                            screen.blit(final1, (0, 0))
                            puntos_txt = font.render(f"{puntos}", True, (255, 255, 255))
                            screen.blit(puntos_txt, (650, 340))
                            pygame.display.flip()
                if teclas[pygame.K_n]:
                    break
                if teclas[pygame.K_x]:
                    break
                tiempo_transcurrido += pygame.time.get_ticks()
                if tiempo_transcurrido >= 10:
                    puntos += 1
                    tiempo_transcurrido = 0
                if y < 80:
                    puntos -= 10
                if y > 580:
                    puntos -= 10

                pygame.display.flip()                     ##Esto lo que hace es borrar todos los objetos de la pantalla y dibujarlos de vuelta en su nueva ubicacion con sus respectivos tamaños


                screen.blit(fondo, (0, 0))
                screen.blit(auto, (200, 270))
                screen.blit(objeto1, (100, 200))
                screen.blit(objeto3, (100, 200))
                screen.blit(objeto2, (100, 200))
        if teclas[pygame.K_b]:
            x = 100
            y = 250
            w = 1200
            u = 2

            y1 = random.randint(1, 5)
            y2 = random.randint(1, 5)
            y3 = random.randint(1, 5)
            t = y1 * 100
            l = y2 * 100
            p = y3 * 100

            vidas = 3

            font = pygame.font.Font(None, 36)
            puntos = 0
            tiempo_transcurrido = 0

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                screen.blit(fondo, (0, 0))
                screen.blit(auto2, (x, y))
                screen.blit(objeto1, (w, t))
                screen.blit(objeto3, (w, l))
                screen.blit(objeto2, (w, p))

                vidas_txt = font.render(f"Vidas: {vidas}", True, (255, 0, 0))
                screen.blit(vidas_txt, (100, 5))
                puntos_txt = font.render(f"Puntos: {puntos}", True, (0, 0, 0))
                screen.blit(puntos_txt, (100, 40))

                w = w - u

                if w < -10:                                                              ##Establece el movimiento constante de los objetos
                    w = 1200
                    y1 = random.randint(1, 5)
                    y2 = random.randint(1, 5)
                    y3 = random.randint(1, 5)
                    t = y1 * 100
                    l = y2 * 100
                    p = y3 * 100
                    u += 0.5

                teclas = pygame.key.get_pressed()                                         ##define las teclas para el movimiento del jugador
                if teclas[pygame.K_LEFT]:
                    x -= 1
                if teclas[pygame.K_RIGHT]:
                    x += 1
                if teclas[pygame.K_UP]:
                    y -= 2
                if teclas[pygame.K_DOWN]:
                    y += 2
                if teclas[pygame.K_a]:
                    x -= 1
                if teclas[pygame.K_d]:
                    x += 1
                if teclas[pygame.K_w]:
                    y -= 2
                if teclas[pygame.K_s]:
                    y += 2

                auto2_rect = Rect(x, y, 150, 80)                                     ##esto establece las hitboxs de los objetos
                objeto1_rect = Rect(w, t, 150, 80)
                objeto2_rect = Rect(w, l, 150, 80)
                objeto3_rect = Rect(w, p, 150, 80)

                if x < -30:
                    vidas -= 1
                    x = 100
                    y = 250

                if auto2_rect.colliderect(objeto1_rect) or auto2_rect.colliderect(objeto2_rect) or auto2_rect.colliderect(objeto3_rect):                 ##esto detecta las colisiones entre los objetos y los autos para descontar vidas
                    vidas -= 1
                    print("Colisión detectada. Vidas restantes:", vidas)
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

                    if vidas == 0:
                        print(puntos)
                        actualizar_ranquin(puntos)
                        font = pygame.font.Font(None, 48)
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()
                            teclas = pygame.key.get_pressed()

                            if teclas[pygame.K_n]:
                                if teclas[pygame.K_n]:
                                    break
                            if teclas[pygame.K_y]:
                                juego_de_1_jugador(screen)

                            screen.blit(final1, (0, 0))
                            puntos_txt = font.render(f"{puntos}", True, (255, 255, 255))
                            screen.blit(puntos_txt, (650, 340))
                            pygame.display.flip()
                if teclas[pygame.K_n]:
                    break
                if teclas[pygame.K_x]:
                    break
                tiempo_transcurrido += pygame.time.get_ticks()                                      ##sistema de puntuacion
                if tiempo_transcurrido >= 10:
                    puntos += 1
                    tiempo_transcurrido = 0
                if y < 80:
                    puntos -= 10
                if y > 580:
                    puntos -= 10

                pygame.display.flip()                                                            ##Esto lo que hace es borrar todos los objetos de la pantalla y dibujarlos de vuelta en su nueva ubicacion con sus respectivos tamaños

                screen.blit(fondo, (0, 0))
                screen.blit(auto2, (200, 270))
                screen.blit(objeto1, (100, 200))
                screen.blit(objeto3, (100, 200))
                screen.blit(objeto2, (100, 200))
        if teclas[pygame.K_c]:
            x = 100
            y = 250
            w = 1200
            u = 2

            y1 = random.randint(1, 5)
            y2 = random.randint(1, 5)
            y3 = random.randint(1, 5)
            t = y1 * 100
            l = y2 * 100
            p = y3 * 100

            vidas = 3

            font = pygame.font.Font(None, 36)
            puntos = 0
            tiempo_transcurrido = 0

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                screen.blit(fondo, (0, 0))
                screen.blit(auto3, (x, y))
                screen.blit(objeto1, (w, t))
                screen.blit(objeto3, (w, l))
                screen.blit(objeto2, (w, p))

                vidas_txt = font.render(f"Vidas: {vidas}", True, (255, 0, 0))
                screen.blit(vidas_txt, (100, 5))
                puntos_txt = font.render(f"Puntos: {puntos}", True, (0, 0, 0))
                screen.blit(puntos_txt, (100, 40))

                w = w - u

                if w < -10:
                    w = 1200
                    y1 = random.randint(1, 5)
                    y2 = random.randint(1, 5)
                    y3 = random.randint(1, 5)
                    t = y1 * 100
                    l = y2 * 100
                    p = y3 * 100
                    u += 0.5

                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_LEFT]:
                    x -= 1
                if teclas[pygame.K_RIGHT]:
                    x += 1
                if teclas[pygame.K_UP]:
                    y -= 2
                if teclas[pygame.K_DOWN]:
                    y += 2
                if teclas[pygame.K_a]:
                    x -= 1
                if teclas[pygame.K_d]:
                    x += 1
                if teclas[pygame.K_w]:
                    y -= 2
                if teclas[pygame.K_s]:
                    y += 2

                auto3_rect = Rect(x, y, 150, 80)
                objeto1_rect = Rect(w, t, 150, 80)
                objeto2_rect = Rect(w, l, 150, 80)
                objeto3_rect = Rect(w, p, 150, 80)

                if x < -30:
                    vidas -= 1
                    x = 100
                    y = 250

                    if vidas == 0:
                        print(puntos)
                        actualizar_ranquin(puntos)
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
                                juego_de_1_jugador(screen)

                            screen.blit(final1, (0, 0))
                            puntos_txt = font.render(f"{puntos}", True, (255, 255, 255))
                            screen.blit(puntos_txt, (650, 340))
                            pygame.display.flip()

                if auto3_rect.colliderect(objeto1_rect) or auto3_rect.colliderect(
                        objeto2_rect) or auto3_rect.colliderect(
                    objeto3_rect):
                    vidas -= 1
                    print("Colisión detectada. Vidas restantes:", vidas)
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

                    if vidas == 0:
                        print(puntos)
                        actualizar_ranquin(puntos)
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
                                juego_de_1_jugador(screen)

                            screen.blit(final1, (0, 0))
                            puntos_txt = font.render(f"{puntos}", True, (255, 255, 255))
                            screen.blit(puntos_txt, (650, 340))
                            pygame.display.flip()
                if teclas[pygame.K_n]:
                    break
                if teclas[pygame.K_x]:
                    break
                tiempo_transcurrido += pygame.time.get_ticks()
                if tiempo_transcurrido >= 10:
                    puntos += 1
                    tiempo_transcurrido = 0
                if y < 80:
                    puntos -= 10
                if y > 580:
                    puntos -= 10

                pygame.display.flip()

                screen.blit(fondo, (0, 0))
                screen.blit(auto3, (200, 270))
                screen.blit(objeto1, (100, 200))
                screen.blit(objeto3, (100, 200))
                screen.blit(objeto2, (100, 200))
        if teclas[pygame.K_n]:
          break

screen = display.set_mode((1380, 720))                                            ##en esta parte del codigo lo que se hace es declarar variables de imagenes

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



