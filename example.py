import pygame
import dumbmenu as dm
import main as pg
pygame.init()

# Just a few static variables
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

size = width, height = (500,500)
screen = pygame.display.set_mode(size)
screen.fill(green)
pygame.display.update()
pygame.key.set_repeat(500,30)

choose = dm.dumbmenu(screen, [
                        'Lancer',
                        'Manual',
                        'Vos Scores',
                        'Quitter'], 64,64,None,32,1.4,red,red)

if choose == 0:
    print "You choose 'Start Game'."
elif choose == 1:
    print "You choose 'Manual'."
elif choose == 2:
    print "You choose 'Show Highscore'."
elif choose == 3:
    print "You choose 'Quit Game'."
pygame.quit()
exit()

