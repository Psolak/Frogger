# coding: utf8
import pygame
import main as pg
import subprocess

pygame.init()
sound = pygame.mixer.Sound('Menu_Sound.wav')


def frogmenu(screen, menu, x_pos = 100, y_pos = 100, font = None,
            size = 100, distance = 1.4, fgcolor = (255,255,255),
            cursorcolor = (255,0,0), exitAllowed = True):
	

	sound = pygame.mixer.Sound('Menu_Sound.wav')
	pygame.font.init()
	pepcur = pygame.image.load('47.gif')
	
	# Creation de la boucle qui gere les textes du menu (Lancer, Quitter, etc ...)

	myfont = pygame.font.SysFont(font, size)
	cursorpos = 0
	renderWithCars = False
	for i in menu:
		if renderWithCars == False:
			text =  myfont.render(str(cursorpos + 1)+".  " + i,
				True, fgcolor)
		
		textrect = text.get_rect()
		textrect = textrect.move(x_pos, 
		           (size // distance * cursorpos) + y_pos) 
		screen.blit(text, textrect)
		pygame.display.update(textrect)
		cursorpos += 1
		
		

	# Trace le curseur "grenouille"
	cursorpos = 0
	cursor = pepcur
	cursorrect = cursor.get_rect()
	cursorrect = cursorrect.move(x_pos - (size // distance),
	             (size // distance * cursorpos) + y_pos)

	# Permet l'affichage du curseur, ainsi que son mouvement
	ArrowPressed = True
	exitMenu = False
	filler = pygame.Surface.copy(screen)
	fillerrect = filler.get_rect()
	while True:
		if ArrowPressed == True:
			screen.blit(filler, fillerrect)
			pygame.display.update(cursorrect)
			cursorrect = cursor.get_rect()
			cursorrect = cursorrect.move(x_pos - (size // distance),
			             (size // distance * cursorpos) + y_pos)
			screen.blit(cursor, cursorrect)
			pygame.display.update(cursorrect)
			ArrowPressed = False
		if exitMenu == True:
			break

                # Creation des evenements permettant de bouger le curseur a l'aide des touches du clavier
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					ArrowPressed = True
					sound.play()
					sound.set_volume(0.1)
					if cursorpos == 0:
						cursorpos = len(menu) - 1
					else:
						cursorpos -= 1
				elif event.key == pygame.K_DOWN:
					ArrowPressed = True
					sound.play()
					sound.set_volume(0.1)
					if cursorpos == len(menu) - 1:
						cursorpos = 0
					else:
						cursorpos += 1
				elif event.key == pygame.K_KP_ENTER or \
				     event.key == pygame.K_RETURN:
							exitMenu = True
	
	return cursorpos



red = 255,0,0
green = 0, 150, 51
gf = 0,255,0
blue  =   0,  0,255
white = 255, 255, 255
myfont2 = pygame.font.SysFont('Comic Sans MS',30)
cred = 0


size = width, height = (400,250)
screen = pygame.display.set_mode(size)
screen.fill(white)
bg = pygame.image.load("Pepe_Menu.png")
screen.blit(bg,(120,25))
title = pygame.image.load("title.png")
screen.blit(title,(30,0))
pygame.display.update()
pygame.key.set_repeat(500,70)

choose = frogmenu(screen, [                             #On appelle la fonction avec nos parametre pour creer le menu
                        'Lancer',
                        'Vos Scores',
                        'Credit','Quitter'], 64,64,None,32,1.1,gf,gf,)

myfont = pygame.font.SysFont('Comic Sans MS', 30)
scoretxt = open('score.txt','r')
scores = scoretxt.readlines()
scoretxt.close()
sound.set_volume(0.1)
if choose == 0:
    print "Lancement du jeu."
    sound.play()
    execfile('main.py')
elif choose == 1:
    sound.play()
    while True:  
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                execfile('menu.py')
        screen.fill(white)
        screen.blit(bg,(65,0))
        last = myfont.render('Last score: ' + str(int(scores[0])), False, red,)
        best = myfont.render('Best score: ' + scores[1], False, red,)
        screen.blit(last,(0,0))
        screen.blit(best,(0,25))
        pygame.display.update()
    
elif choose == 3:
    sound.play()
    print "Quitte le jeu."
    pygame.quit()
    exit()

elif choose == 2:
        sound.play()
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                execfile('menu.py')
                screen.fill(white)
                screen.blit(bg, (65,0))
                myfont = pygame.font.SysFont('Comic Sans MS', 13)
                cred = myfont.render('Realise par GHO Baptiste, CABIROU Arnaud et RACHID Kaysse'
                             , False, blue)
                
                screen.blit(cred,(0,0))
                pygame.display.update()
                



        
