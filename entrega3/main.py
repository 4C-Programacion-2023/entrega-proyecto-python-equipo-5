import pygame
from pygame import display
from menu import menu_principal


pygame.init()

if __name__ == "__main__":
    screen = display.set_mode((1380, 720))
    menu_principal(screen)

##debe instalar la libreria de pycharm