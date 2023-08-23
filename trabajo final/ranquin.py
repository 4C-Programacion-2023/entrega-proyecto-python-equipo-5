import json
import  pygame
from pygame import image, transform, display

def guardar_ranquin(ranquin):
    with open("ranquin.json", "w") as file:
        json.dump(ranquin, file)
def cargar_ranquin():
    try:
        with open("ranquin.json", "r") as file:
            ranquin = json.load(file)
    except FileNotFoundError:
        ranquin = []
    return ranquin

def actualizar_ranquin(puntos):                                         ##esta parte lo que hace es comparar la puntuacion con las mejores 5, luego los ordena de mayor a menor
    ranquin = cargar_ranquin()
    ranquin.append(puntos)
    ranquin.sort(reverse=True)
    ranquin = ranquin[:5]
    guardar_ranquin(ranquin)

def mostrar_ranquin():
    ranquin = cargar_ranquin()

    font = pygame.font.Font(None, 36)
    y = 100

    while True:                                                         ##Esta zona del codigo escribe las puntuaciones en la pantalla
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
screen = display.set_mode((1380, 720))

puestos = image.load("RAANQUIN.png")                                         ##en esta parte del codigo lo que se hace es declarar variables de imagenes
puestos = transform.scale(puestos, (1380, 720))