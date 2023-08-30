import pygame
from pygame import image, display, transform
from juego_un_jugador import juego_de_1_jugador
from ranquin import mostrar_ranquin
from juego_dos_jugadores import juego_de_2_jugadores

def menu_principal(screen):
    # ... (menu setup code)
    pygame.mixer.music.load("miusiq.mp3")
    pygame.mixer.music.play(-1)  # esto hace q se repita siempre la musica

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(menu, (0, 0))

        teclas = pygame.key.get_pressed()                                   ##llama a las funciones definidas en los otros archivos para hacer el menu del juego
        if teclas[pygame.K_1]:
            juego_de_1_jugador(screen)
        if teclas[pygame.K_2]:
            mostrar_ranquin()
        if teclas[pygame.K_3]:
            juego_de_2_jugadores(screen)

        pygame.display.flip()

screen = display.set_mode((1380, 720))

menu = image.load("MENU HECHO.png")                                           ##en esta parte del codigo lo que se hace es declarar variables de imagenes
menu = transform.scale(menu, (1380, 720))