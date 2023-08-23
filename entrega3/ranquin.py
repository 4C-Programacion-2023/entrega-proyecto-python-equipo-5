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

def actualizar_ranquin(puntos):
    ranquin = cargar_ranquin()
    ranquin.append(puntos)
    ranquin.sort(reverse=True)
    ranquin = ranquin[:5]
    guardar_ranquin(ranquin)

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
screen = display.set_mode((1380, 720))

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



