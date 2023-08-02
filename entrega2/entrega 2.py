import pygame
import json
from pygame import *
import random

pygame.init()

monedas = 0

def guardar_monedas():
    global monedas
    data = {"monedas": monedas}
    with open("monedas.json", "w") as file:
        json.dump(data, file)
def guardar_ranquin(ranquin):
    with open("ranquin.json", "w") as file:
        json.dump(ranquin, file)
def cargar_monedas():
    global monedas
    try:
        with open("monedas.json", "r") as file:
            data = json.load(file)
            monedas = data.get("monedas", 0)
    except FileNotFoundError:
        monedas = 0
def cargar_ranquin():
    try:
        with open("ranquin.json", "r") as file:
            ranquin = json.load(file)
    except FileNotFoundError:
        ranquin = []
    return ranquin
def actualizar_ranquin(puntos):
    ranquin = cargar_ranquin()
    ranquin.append(puntos)
    ranquin.sort(reverse=True)
    ranquin = ranquin[:5]
    guardar_ranquin(ranquin)
def menu_principal():
    def juego_de_1_jugador():
        global monedas
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

        monedas_partida = 0

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
            screen.blit(auto, (x, y))
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

            auto_rect = Rect(x, y, 150, 80)
            objeto1_rect = Rect(w, t, 150, 80)
            objeto2_rect = Rect(w, l, 150, 80)
            objeto3_rect = Rect(w, p, 150, 80)

            if auto_rect.colliderect(objeto1_rect) or auto_rect.colliderect(objeto2_rect) or auto_rect.colliderect(
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
                    print("game over")
                    print(puntos)
                    monedas_partida = puntos / 1000
                    monedas += monedas_partida
                    guardar_monedas()
                    actualizar_ranquin(puntos)
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
            screen.blit(auto, (200, 270))
            screen.blit(objeto1, (100, 200))
            screen.blit(objeto3, (100, 200))
            screen.blit(objeto2, (100, 200))
    def mostrar_ranquin():
        ranquin = cargar_ranquin()

        font = pygame.font.Font(None, 36)
        y = 100

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.blit(puestos, (0, 0))
            top1_txt = font.render(f" {ranquin[0:1]}", True, (0, 0, 0))
            screen.blit(top1_txt, (670, 175))
            top2_txt = font.render(f" {ranquin[1:2]}", True, (0, 0, 0))
            screen.blit(top2_txt, (315, 280))
            top3_txt = font.render(f" {ranquin[2:3]}", True, (0, 0, 0))
            screen.blit(top3_txt, (1000, 380))
            top4_txt = font.render(f" {ranquin[3:4]}", True, (0, 0, 0))
            screen.blit(top4_txt, (420, 640))
            top5_txt = font.render(f" {ranquin[4:5]}", True, (0, 0, 0))
            screen.blit(top5_txt, (915, 640))

            pygame.display.flip()
            screen.blit(puestos, (0, 0))

            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_x]:
                break
    def juego_de_2_jugadores():
        font = pygame.font.Font(None, 36)

        x = 100  # cordenadas jugador1
        y = 250

        m = 100  # cordenadas jugador2
        s = 450

        w = 1200  # cordenada obstaculos

        u = 2  # velocidad de los obtaculos

        y1 = random.randint(1, 5)  # generacion de los obstaculos
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

            screen.blit(fondo, (0, 0))
            screen.blit(auto, (x, y))
            screen.blit(auto2, (m, s))
            screen.blit(objeto1, (w, t))
            screen.blit(objeto3, (w, l))
            screen.blit(objeto2, (w, p))

            vidas_txt1 = font.render(f"Vidas1: {vidas1}", True, (255, 0, 0))
            screen.blit(vidas_txt1, (100, 5))

            vidas_txt2 = font.render(f"Vidas2: {vidas2}", True, (255, 0, 0))
            screen.blit(vidas_txt2, (1200, 5))

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
                m -= 1
            if teclas[pygame.K_d]:
                m += 1
            if teclas[pygame.K_w]:
                s -= 2
            if teclas[pygame.K_s]:
                s += 2

            auto_rect = Rect(x, y, 150, 80)
            auto2_rect = Rect(m, s, 150, 80)
            objeto1_rect = Rect(w, t, 150, 80)
            objeto2_rect = Rect(w, l, 150, 80)
            objeto3_rect = Rect(w, p, 150, 80)

            if auto_rect.colliderect(objeto1_rect) or auto_rect.colliderect(objeto2_rect) or auto_rect.colliderect(
                    objeto3_rect):

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
                    print("game over jugador 1")
                    break
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
                    print("game over jugador 2")
                    break

            if teclas[pygame.K_x]:
                break

            pygame.display.flip()

            screen.blit(fondo, (0, 0))
            screen.blit(auto, (200, 270))
            screen.blit(auto2, (200, 470))
            screen.blit(objeto1, (100, 200))
            screen.blit(objeto3, (100, 200))
            screen.blit(objeto2, (100, 200))
    def garage4():
        global monedas
        font = pygame.font.Font(None, 36)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.blit(garage, (0, 0))
            monedas_txt = font.render(f"monedas totales= {monedas}", True, (255, 255, 0))
            screen.blit(monedas_txt, (1050, 5))

            pygame.display.flip()

            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_x]:
                break

    cargar_monedas()

    font = pygame.font.Font(None, 48)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(menu, (0, 0))

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_1]:
            juego_de_1_jugador()
        if teclas[pygame.K_2]:
            mostrar_ranquin()
        if teclas[pygame.K_3]:
            juego_de_2_jugadores()
        if teclas[pygame.K_4]:
            garage4()

        pygame.display.flip()

screen = display.set_mode((1380, 720))

menu = image.load("MENU HECHO.png")
menu = transform.scale(menu, (1380, 720))

garage = image.load("garage.png")
garage = transform.scale(garage, (1380, 720))

puestos = image.load("RAANQUIN.png")
puestos = transform.scale(puestos, (1380, 720))

fondo = image.load("fondo.jpeg")
fondo = transform.scale(fondo, (1380, 720))

auto = image.load("auto prinsipal.png")
auto = transform.scale(auto, (150, 100))

auto2 = image.load("auto2.png")
auto2 = transform.scale(auto2, (160, 100))

objeto1 = image.load("objeto1-removebg-preview.png")
objeto1 = transform.scale(objeto1, (200, 100))

objeto2 = image.load("obstaculo2.png")
objeto2 = transform.scale(objeto2, (200, 100))

objeto3 = image.load("objeto3.png")
objeto3 = transform.scale(objeto3, (200, 100))


cargar_monedas()
menu_principal()