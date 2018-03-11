import pygame
from pygame.locals import *
from random import randint


class SheetInfos:
    def __init__(self):
        self.CAR_BLACK = (0, 0, 71, 131)
        self.CAR_BLUE = (0, 251, 71, 131)
        self.CAR_GREEN = (73, 0, 71, 131)
        self.CAR_RED = (73, 369, 71, 131)
        self.CAR_YELLOW = (146, 118, 71, 131)
        self.cars = [self.CAR_BLACK, self.CAR_BLUE, self.CAR_GREEN,
                    self.CAR_RED, self.CAR_YELLOW]

        self.MOTO_BLACK = (434, 389, 44, 100)
        self.MOTO_BLUE = (506, 133, 44, 100)
        self.MOTO_GREEN = (480, 389, 44, 100)
        self.MOTO_RED = (290, 399, 44, 100)
        self.MOTO_YELLOW = (219, 133, 44, 100)
        self.motos = [self.MOTO_BLACK, self.MOTO_BLUE, self.MOTO_GREEN,
                    self.MOTO_RED, self.MOTO_YELLOW]

    def random_car(self):
        return self.cars[randint(0, len(self.cars) - 1)]

    def random_moto(self):
        return self.motos[randint(0, len(self.motos) - 1)]

class Assets:
    def __init__(self):
        self.road1 = ""
        self.road2 = ""
        self.grass = ""
        self.water = ""
        self.water2 = ""
        self.wood200 = ""
        self.wood200_2 = ""
        self.water_sprite = ""

    def load_assets(self):
        self.road1 = pygame.image.load('road1.bmp')
        self.road2 = pygame.image.load('road2.bmp')
        self.grass = pygame.image.load('grass.bmp')
        self.water = pygame.image.load('water.bmp')
        self.water2 = pygame.image.load('water.bmp')
        self.wood200 = pygame.image.load('wood200.bmp')
        self.wood200_2 = pygame.image.load('wood200_2.bmp')
        self.water_sprite = pygame.image.load('water_sprite.bmp')

class SpriteSheet:
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image

class Player(pygame.sprite.Sprite):
    def __init__(self, speedxr=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1000 / 2
        self.rect.bottom = 700 - 20
        self.speedy = 0
        self.k = False
        self.score = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.k = False
        self.i = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.speedx = -100
                if event.key == pygame.K_RIGHT:
                    self.speedx = 100
                if event.key == pygame.K_UP:
                    self.speedy = -100
                    self.k = True
                if event.key == pygame.K_DOWN:
                    self.speedy = 100

        if self.speedy > 0:
            self.rect.y += self.speedy
            self.i = True

        if self.k and self.rect.y >= 500:
            self.rect.y += self.speedy
            self.i = False

        elif self.k and self.rect.y < 500:
            self.score += 1


        self.rect.x += self.speedx + speedxr

        if self.rect.right > 1000:
            self.rect.right = 1000 - 20
        if self.rect.left < 0:
            self.rect.left = 20
        if self.rect.bottom > 700 - 20:
            self.rect.bottom = 700 - 20


class Rondin(pygame.sprite.Sprite):
    def __init__(self, assets, x, position):

        pygame.sprite.Sprite.__init__(self)
        self.rondins = [assets.wood200, assets.wood200_2]
        self.image = self.rondins[randint(0, 1)].convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottom = 700 - x

        if position == 'right':
            self.rect.centerx = -300
            self.speedx = 5
        elif position == 'left':
            self.rect.centerx = 1300
            self.speedx = -5
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx

class Car(pygame.sprite.Sprite):
    def __init__(self, assets, x):

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('spritesheet_vehicles.png')
        sheet_infos = SheetInfos()
        self.car = sheet_infos.random_car()
        self.image = sprite_sheet.get_image(self.car[0],
                                            self.car[1],
                                            self.car[2],
                                            self.car[3])
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.centerx = -200
        self.rect.bottom = 700 - x
        self.speedx = 10
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Moto(pygame.sprite.Sprite):
    def __init__(self, assets, x):

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('spritesheet_vehicles.png')
        sheet_infos = SheetInfos()
        self.moto = sheet_infos.random_moto()
        self.image = sprite_sheet.get_image(self.moto[0],
                                            self.moto[1],
                                            self.moto[2],
                                            self.moto[3])
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.centerx = -200
        self.rect.bottom = 685 - x
        self.speedx = 10
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Water(pygame.sprite.Sprite):
    def __init__(self, assets, x):

        pygame.sprite.Sprite.__init__(self)
        self.image = assets.water_sprite.convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.bottom = 700 - x
        self.speedx = 0
        self.speedy = 0


class Background:
    def __init__(self, assets, screen, decors):

        self.update(assets, screen, decors)

    def update(self, assets, screen, decors):

        screen.fill((0,0,0))
        for i in range(7):
            screen.blit(decors[i], (0, 600 - (i * 100)))

class Decors:
    def __init__(self, assets, all_sprites, WaterS):
        self.decors = [assets.grass, assets.road1, assets.road2,  assets.road1, assets.road2, assets.water, assets.water2, assets.grass, assets.road1, assets.road2, assets.road1, assets.road2, assets.grass, assets.grass]
        self.tiles = [assets.grass, assets.road1, assets.road2, assets.water, assets.water2]
        self.water_sprites = [(Water(assets, 600)), (Water(assets, 500))]
        all_sprites.add(self.water_sprites[0])
        WaterS.add(self.water_sprites[0])

        all_sprites.add(self.water_sprites[1])
        WaterS.add(self.water_sprites[1])

        self.num = 0

    def update(self, assets, all_sprites, WaterS):

        self.num = randint(0, 4)

        if self.decors[-1] == assets.water and self.decors[-2] != assets.water2:
            self.decors.append(assets.water2)
            self.water_sprites.append(Water(assets, (len(self.decors) - 3) * 100))
            all_sprites.add(self.water_sprites[-1])
            WaterS.add(self.water_sprites[-1])

        elif self.decors[-1] == assets.water2 and self.decors[-2] != assets.water:
            self.decors.append(assets.water)
            self.water_sprites.append(Water(assets, (len(self.decors) - 3) * 100))
            all_sprites.add(self.water_sprites[-1])
            WaterS.add(self.water_sprites[-1])

        elif self.decors[-1] == assets.road1 and self.decors[-2] != assets.road2:
            self.decors.append(assets.road2)

        elif self.decors[-1] == assets.road2 and self.decors[-2] != assets.road1:
            self.decors.append(assets.road1)


        else:
            if self.tiles[self.num] == assets.road1 and self.decors[-1] == assets.road1:
                self.decors.append(assets.road2)

            elif self.tiles[self.num] == assets.road2 and self.decors[-1] == assets.road2:
                self.decors.append(assets.road1)

            elif self.tiles[self.num] == assets.water and self.decors[-1] == assets.water:
                self.decors.append(assets.water2)
                self.water_sprites.append(Water(assets, (len(self.decors) - 3) * 100))
                all_sprites.add(self.water_sprites[-1])
                WaterS.add(self.water_sprites[-1])

            elif self.tiles[self.num] == assets.water2 and self.decors[-1] == assets.water2:
                self.decors.append(assets.water)
                self.water_sprites.append(Water(assets, (len(self.decors) - 3) * 100))
                all_sprites.add(self.water_sprites[-1])
                WaterS.add(self.water_sprites[-1])

            else:
                self.decors.append(self.tiles[self.num])

        if (len(self.water_sprites)) > 7:
            print self.water_sprites
            all_sprites.remove(self.water_sprites[0])
            WaterS.remove(self.water_sprites[0])
            del self.water_sprites[0]

        del self.decors[0]

class Generate:
    def __init__(self, assets, dec, vehicles, waterobjects, WaterS):
        self.rondins = []
        self.cars = []
        self.motos = []

    def update(self, assets, dec, vehicles, all_sprites, waterobjects, WaterS):

        for self.t in range(len(dec.decors)):
            if dec.decors[self.t] == assets.road1 or dec.decors[self.t] == assets.road2:

                if randint(0, 250) == 0:
                    self.cars.append(Car(assets, self.t * 100))
                    pygame.sprite.spritecollide(self.cars[-1], all_sprites, dokill=True)
                    all_sprites.add(self.cars[-1])
                    vehicles.add(self.cars[-1])

                if randint(0, 250) == 0:
                    self.motos.append(Moto(assets, self.t * 100))
                    pygame.sprite.spritecollide(self.motos[-1], all_sprites, dokill=True)
                    all_sprites.add(self.motos[-1])
                    vehicles.add(self.motos[-1])

            elif dec.decors[self.t] == assets.water or dec.decors[self.t] == assets.water2:

                if randint(0, 100) == 0:
                    if dec.decors[self.t] == assets.water:
                        self.rondins.append(Rondin(assets, self.t * 100, 'left'))
                        pygame.sprite.spritecollide(self.rondins[-1], all_sprites, dokill=True)
                        all_sprites.add(self.rondins[-1])
                        waterobjects.add(self.rondins[-1])

                    elif dec.decors[self.t] == assets.water2:
                        self.rondins.append(Rondin(assets, self.t * 100, 'right'))
                        pygame.sprite.spritecollide(self.rondins[-1], all_sprites, dokill=True)
                        all_sprites.add(self.rondins[-1])
                        waterobjects.add(self.rondins[-1])

        if self.motos:
            for self.moto in self.motos:
                if self.moto.rect.x > 1000:
                    vehicles.remove(self.moto)
                    all_sprites.remove(self.moto)

        if self.cars:
            for self.car in self.cars:
                if self.car.rect.x > 1000:
                    vehicles.remove(self.car)
                    all_sprites.remove(self.car)

        if self.rondins:
            for self.rondin in self.rondins:
                if self.rondin.rect.x > 1800 or self.rondin.rect.x < -800:
                    waterobjects.remove(self.rondin)
                    all_sprites.remove(self.rondin)


class Move:
    def __init__(self, player, gen, dec):
        self.m = ''
        self.c = ''
        self.r = ''
        self.w = ''

    def update(self, player, gen, dec):

        if player.k and player.rect.y <= 500 and player.i:
            for self.c in gen.cars:
                self.c.rect.y += 100
            for self.m in gen.motos:
                self.m.rect.y += 100
            for self.r in gen.rondins:
                self.r.rect.y += 100
            for self.w in dec.water_sprites:
                self.w.rect.y += 100


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))

    global speedxr
    speedxr = 0

    assets = Assets()
    assets.load_assets()

    all_sprites = pygame.sprite.Group()
    WaterS = pygame.sprite.Group()
    waterobjects = pygame.sprite.Group()
    vehicles = pygame.sprite.Group()

    dec = Decors(assets, all_sprites, WaterS)

    playerG = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    playerG.add(player)


    dead = []

    gen = Generate(assets, dec, vehicles, waterobjects, WaterS)
    move = Move(player, gen, dec)
    clock = pygame.time.Clock()

    i = 0
    ti = 0

    deadW = pygame.sprite.spritecollide(player, WaterS, dokill=False)

    while True:


        bg = Background(assets, screen, dec.decors)

        move.update(player, gen, dec)

        dead = pygame.sprite.spritecollide(player, vehicles, dokill=False)
        on_rondin = pygame.sprite.spritecollide(player, waterobjects, dokill=False)

        if player.rect.y < 500 and player.k and player.i:
            dec.update(assets, all_sprites, WaterS)
            bg.update(assets, screen, dec.decors)

        if on_rondin:
            speedxr = on_rondin[0].speedx
            ti = pygame.time.get_ticks()

        else:
            speedxr = 0
            if pygame.time.get_ticks() - ti > 10:
                deadW = pygame.sprite.spritecollide(player, WaterS, dokill=False)


        if dead or deadW:
            all_sprites.remove(player)
            playerG.remove(player)



        gen.update(assets, dec, vehicles, all_sprites, waterobjects, WaterS)
        all_sprites.update()
        all_sprites.draw(screen)
        playerG.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
