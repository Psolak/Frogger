import pygame
import dumbmenu as dm
import main as pg
import subprocess
pygame.init()



red = 255,0,0
green = 0, 150, 51
gf = 0,255,0
blue  =   0,  0,255
white = 255, 255, 255

size = width, height = (400,250)
screen = pygame.display.set_mode(size)
screen.fill(white)
bg = pygame.image.load("Pepe_Menu.png")
screen.blit(bg,(65,0))
pygame.display.update()
pygame.key.set_repeat(500,30)

choose = dm.dumbmenu(screen, [
                        'Lancer',
                        'Vos Scores',
                        'Quitter'], 64,64,None,32,1.4,gf,gf)

myfont = pygame.font.SysFont('Comic Sans MS', 30)
scoretxt = open('score.txt','r')
scores = scoretxt.readlines()
scoretxt.close()

if choose == 0:
    print "Lancement du jeu."
    execfile('main.py')
elif choose == 1:
    while True:  
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                execfile('menu.py')
        screen.fill(white)
        screen.blit(bg,(65,0))
        last = myfont.render('Last score: ' + str(int(scores[0])), False, red)
        best = myfont.render('Best score: ' + scores[1], False, red)
        screen.blit(last,(0,0))
        screen.blit(best,(0,25))
        pygame.display.update()
    
elif choose == 2:
    print "Quitte le jeu."
    
    
pygame.quit()
exit()

