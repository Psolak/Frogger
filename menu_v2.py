import pygame
import sys
from pygame.locals import *
import time


class Button(pygame.sprite.Sprite):
    def __init__(self, image, buttonX, buttonY):
        super().__init__()
        self.image = image
        self.rect = image.getRect()
        self.rect.x = buttonX
        self.rect.y = buttonY

    def wasClicked(event):
        if self.rect.collidepoint(event.pos):
             return True

def gameIntro():
    #initialize buttons
    buttons = pygame.sprite.Group() #make a group to make drawing easier
    button_start = Button(img_button_start, 27, 0)
    button_options = Button(img_button_options, 27, 500)
    #draw buttons to display
    buttons.draw(gameDisplay)
    pygame.display.update()

    #main game loop
    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #check for every button whether it was clicked
                for btn in buttons:
                    if btn.wasClicked():
                        #do something appropriate
                        if event.type == pygame.QUIT:
                            pygame.quit()
