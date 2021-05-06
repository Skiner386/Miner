import pygame
from pygame.locals import *
import threading
from Game.eq import *
from datetime import datetime
pygame.init()
class HW:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.root = pygame.display.set_mode((x,y))

class Info:
    def __init__(self):
        self.PlayerTexture = pygame.image.load('Images/character.png')
        self.dirt = pygame.image.load('Images/dirt.png')
        self.grass = pygame.image.load('Images/grass.png')
        self.silver = pygame.image.load('Images/silver.png')
        self.stone = pygame.image.load('Images/stone.png')
        self.diamond = pygame.image.load('Images/diamond.png')
        self.iron = pygame.image.load('Images/iron.png')
        self.gold = pygame.image.load('Images/gold.png')
        self.sky = pygame.image.load('Images/sky.png')
        self.BackGround = pygame.image.load('Images/bg.png')
        self.ladder = pygame.image.load('Images/ladder.png')
        self.shop = pygame.image.load('Images/shop.png')
        self.Shop_BG = pygame.image.load('Images/ShopBG.png')
        self.StonePick = pygame.image.load('Images/StonePick.png')
        self.IronPick = pygame.image.load('Images/IronPick.png')

Img = Info()
disp = HW(1000, 900)


class Blad(Exception):
    def __init__(self,blok,wiadomosc):
        Exception.__init__(self,wiadomosc)
        self.blok = blok

class Map1:
    def __init__(self):
        self.Start = True
        self.Loc = []
        self.blocks_rect = []
        self.a = 0
        self.MapLenght = 3000
        self.MapHeight = 7200
        self.scroll = [0,0]
        self.Con1 = True
        self.Map = [
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 'S', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    7, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1,
                    3, 3, 1, 1, 1, 3, 1, 1, 3, 3, 3, 3, 1, 3, 3, 1, 1, 1, 3, 1,
                    3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 5, 3, 3, 3, 4, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3,
                    3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 6, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 7, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 4, 3, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 6, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 7, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 3, 3, 6, 7, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3,
                    3, 3, 6, 3, 3, 7, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        ] #xd
    def BlockLoc(self):
        for i in range(0,self.MapHeight,150):
            for z in range(0,self.MapLenght,150):
                self.Loc.append([z,i])

    def Camera(self):
        for i in self.Loc:
            i[0] -= Play.dx
            i[1] -= Play.dy

    def MovingBackground(self):
        rel_x = self.a % Img.BackGround.get_rect().width
        disp.root.blit(Img.BackGround, (rel_x - Img.BackGround.get_width()+ M1.scroll[0],0))
        self.a += 3
        if rel_x < 6000:
            disp.root.blit(Img.BackGround, (rel_x + M1.scroll[0], 0))

    def DisplayMap(self):
        self.blocks_rect = []
        M1.MovingBackground()
        M1.Camera()
        a = 0
        for i in self.Map:
            if i == 'S':
                self.blocks_rect.append([Img.shop,(pygame.Rect(self.Loc[a][0],self.Loc[a][1],470,300)),'Shop'])
            if i == 0:
                self.blocks_rect.append(['None',(pygame.Rect(self.Loc[a][0],self.Loc[a][1],150,150)),'None'])
            if i == 1:
                self.blocks_rect.append([Img.dirt,(pygame.Rect(self.Loc[a][0],self.Loc[a][1],150,150)),'Dirt'])
            if i == 2:
                self.blocks_rect.append([Img.grass,(pygame.Rect(self.Loc[a][0],self.Loc[a][1],150,150)),'Grass'])
            if i == 3:
                self.blocks_rect.append([Img.stone,(pygame.Rect(self.Loc[a][0],self.Loc[a][1],150,150)),'Stone'])
            if i == 4:
                self.blocks_rect.append((Img.silver,(pygame.Rect(self.Loc[a][0], self.Loc[a][1], 150, 150)),'Silver'))
            if i == 5:
                self.blocks_rect.append((Img.iron,(pygame.Rect(self.Loc[a][0], self.Loc[a][1], 150, 150)),'Iron'))
            if i == 6:
                self.blocks_rect.append((Img.gold,(pygame.Rect(self.Loc[a][0], self.Loc[a][1], 150, 150)),'Gold'))
            if i == 7:
                self.blocks_rect.append((Img.diamond,(pygame.Rect(self.Loc[a][0], self.Loc[a][1], 150, 150)),'Diamond'))

    #def BlocksHP:
        #for i in self.Map:
            #if i == 0:


            a += 1
    def Camera2(self):
        for i in self.blocks_rect:
            i[1][0] -= Play.dx
            i[1][1] -= Play.dy

M1 = Map1()




class Player:
    def __init__(self):
        self.pickaxe = ['wood_pickaxe',1]
        self.name = ''
        self.Player_rect = pygame.Rect(disp.x/2,355,65,100)
        self.button_rect = pygame.Rect(disp.x-60,10,50,50)
        self.vel = 0
        self.jump = True
        self.dy = 0
        self.dx = 0
        self.Con1 = False
        self.Con2 = False
        self.but = 2
        self.counter = 0
        self.counter2 = 0
        self.time = 0
        self.text = pygame.font.Font('Fonts/PIXEAB__.TTF',30)
        self.mame = self.text.render(str(self.time),True,(100,100,100))
        self.Money = 0
        self.MoneyText = self.text.render(('Money:' + str(self.Money)),True,(100,100,100))
        self.TextRect = self.mame.get_rect()
        self.MoneyRect = self.MoneyText.get_rect()
        self.HPleft = 0
        self.Mineral = None


    def Movement(self):
        self.dx = 0

        if pygame.key.get_pressed()[K_a]:
            self.Con1 = True
            self.dx = -5
        else:
            self.Con1 = False
        if pygame.key.get_pressed()[K_d]:
            self.Con2 = True
            self.dx = 5
        else:
            self.Con2 = False
    def Collision(self):
        for block in M1.blocks_rect:
            if block[1].colliderect(self.Player_rect) and block[2] != 'None' and block[2] != 'Shop':
                if block[1].top + self.dy== self.Player_rect.bottom:
                    self.dy = 0
                    break

                if self.Con1 == True:
                    if block[1].right + self.dx == self.Player_rect.left:
                        self.dx = 0
                if self.Con2 == True:
                    if block[1].left + self.dx == self.Player_rect.right:
                        self.dx = 0

            else:
                self.dy = 5
                    #self.Player_rect.y -= self.dy

    def Mining(self):
        a = 0
        a += self.counter
        #and block[1][1] < self.Player_rect[1]
#
        # and block[1][0] > self.Player_rect[0]
        for block in M1.blocks_rect:
            if block[1].collidepoint(pygame.mouse.get_pos()):
                if  (block[1][1] < self.Player_rect[1] and block[1][1] < self.Player_rect[1]) or \
                        (block[1][0] < self.Player_rect[0] and block[1][0] + 250 > self.Player_rect[0]) or \
                        (block[1][0] > self.Player_rect[0] and block[1][0] < self.Player_rect[0] + 150):
                    b = [block[1],block[2]]
                    self.mame = self.text.render(str(self.HPleft-(self.time)), True, (100, 100, 100))

                    if b[1] == 'Grass':
                        self.HPleft = 25
                        if pygame.mouse.get_pressed()[0]:
                            self.time += self.pickaxe[1]
                            if self.time >= 25:
                                M1.Map[a] = 0
                                self.time = 0

                    if b[1] == 'Stone':
                        self.HPleft = 100
                        if pygame.mouse.get_pressed()[0]:
                            self.time += self.pickaxe[1]
                            if self.time >= 100:
                                M1.Map[a] = 0
                                self.time = 0
                                Op.Minerals["Stone"] += 1

                    if b[1] == 'Silver':
                        self.HPleft = 250
                        if pygame.mouse.get_pressed()[0]:
                            self.time += self.pickaxe[1]
                            if self.time >= 250:
                                M1.Map[a] = 0
                                Op.Minerals["Silver"] += 1
                                self.time = 0

                    if b[1] == 'Dirt':
                        self.HPleft = 40
                        if pygame.mouse.get_pressed()[0]:
                            self.time += self.pickaxe[1]
                            if self.time >= 40:
                                M1.Map[a] = 0
                                self.time = 0

                    if b[1] == 'Gold':
                        self.HPleft = 200
                        if pygame.mouse.get_pressed()[0]:
                            self.time += self.pickaxe[1]
                            if self.time >= 200:
                                M1.Map[a] = 0
                                Op.Minerals["Gold"] += 1
                                self.time = 0

                    if b[1] == 'Iron':
                        self.HPleft = 150
                        if pygame.mouse.get_pressed()[0]:
                            self.time += self.pickaxe[1]
                            if self.time >= 150:
                                M1.Map[a] = 0
                                Op.Minerals["Iron"] += 1
                                self.time = 0

                    if b[1] == 'Diamond':
                        self.HPleft = 500
                        if pygame.mouse.get_pressed()[0]:
                            self.time += self.pickaxe[1]
                            if self.time >= 500:
                                M1.Map[a] = 0
                                Op.Minerals["Diamond"] += 1
                                self.time = 0


            a+= 1
    def DispPlayer(self,HW):
        self.Movement()
        self.Collision()
        self.Mining()
        self.Shop()

        self.TextRect.update(self.Player_rect[0]+8/2,self.Player_rect[1]-100/2,100,100)
        self.MoneyRect.update(10,10,100,100)

        for block in M1.blocks_rect:
            try:
                HW.blit(block[0],[block[1][0],block[1][1]])
            except:
                pass
            #pygame.draw.rect(disp.root,(255,255,255),pygame.Rect([block[1][0],block[1][1]],(150,150)),2)
        HW.blit(Img.PlayerTexture, (self.Player_rect.x,self.Player_rect.y))
        if self.time != 0:
            HW.blit(self.mame,self.TextRect)
        HW.blit(self.MoneyText,self.MoneyRect)
        #pygame.draw.rect(disp.root, (255, 255, 255), (self.Player_rect.x,self.Player_rect.y,self.Player_rect[2],self.Player_rect[3]), 2)
        self.Button()

    def Button(self):
        bambo = threading.Thread(target=lambda: masno(bambo))

        pygame.draw.rect(disp.root,(100,100,100),self.button_rect)
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                bambo.start()
                if self.but%2 == 0:
                    Op.a = True
                    print('tak')
                else:
                    Op.a = False
                    print('nie')
                self.but += 1
                #print(self.but)

    def ShopDisp(self,):


        disp.root.blit(Img.Shop_BG,(0,0))
        StoneRect = pygame.Rect(75,75,75,75)
        IronRect = pygame.Rect(75,200,75,75)
        SilverRect = pygame.Rect(75,325,75,75)
        GoldRect = pygame.Rect(75,450,75,75)
        DiamondRect = pygame.Rect(75,575,75,75)


        stone = pygame.transform.scale(Img.stone, (75, 75))
        disp.root.blit(stone,StoneRect)
        text1 = self.text.render(str(Op.Minerals['Stone']), True, (100, 100, 100))
        disp.root.blit(text1,(200,90))

        iron = pygame.transform.scale(Img.iron, (75, 75))
        disp.root.blit(iron,IronRect)
        text2 = self.text.render(str(Op.Minerals['Iron']), True, (100, 100, 100))
        disp.root.blit(text2,(200,215))

        silver = pygame.transform.scale(Img.silver, (75, 75))
        disp.root.blit(silver,SilverRect)
        text3 = self.text.render(str(Op.Minerals['Silver']), True, (100, 100, 100))
        disp.root.blit(text3,(200,340))

        gold = pygame.transform.scale(Img.gold, (75, 75))
        disp.root.blit(gold,GoldRect)
        text4 = self.text.render(str(Op.Minerals['Gold']), True, (100, 100, 100))
        disp.root.blit(text4,(200,465))

        diamond = pygame.transform.scale(Img.diamond, (75, 75))
        disp.root.blit(diamond,DiamondRect)
        text5 = self.text.render(str(Op.Minerals['Diamond']), True, (100, 100, 100))
        disp.root.blit(text5,(200,590))

        ButtText = self.text.render('Sell', True, (100, 100, 100))
        ButtRect = pygame.Rect(350,344,100,70)
        pygame.draw.rect(disp.root,(150,150,100),(ButtRect[0]-10,ButtRect[1]-15,ButtRect[2],ButtRect[3]))
        disp.root.blit(ButtText,ButtRect)

        ExitText = self.text.render('Exit', True, (100, 100, 100))
        ExitRect = pygame.Rect(875, 825, 100, 70)
        pygame.draw.rect(disp.root,(150,150,100),(ExitRect[0]-10,ExitRect[1]-15,ExitRect[2],ExitRect[3]))
        disp.root.blit(ExitText,ExitRect)

        BuyText_1 = self.text.render('Buy', True, (100, 100, 100))
        BuyRect_1 = pygame.Rect(250, 800, 100, 70)
        pygame.draw.rect(disp.root, (150, 150, 100), (BuyRect_1[0] - 10, BuyRect_1[1] - 15, BuyRect_1[2], BuyRect_1[3]))
        disp.root.blit(BuyText_1, BuyRect_1)

        BuyText_2 = self.text.render('Buy', True, (100, 100, 100))
        BuyRect_2 = pygame.Rect(600, 800, 100, 70)
        pygame.draw.rect(disp.root, (150, 150, 100), (BuyRect_2[0] - 10, BuyRect_2[1] - 15, BuyRect_2[2], BuyRect_2[3]))
        disp.root.blit(BuyText_2, BuyRect_2)

        disp.root.blit(Img.StonePick,(100,775))
        disp.root.blit(Img.IronPick,(450,775))

        disp.root.blit(self.MoneyText,(self.MoneyRect[0]+550,self.MoneyRect[1],self.MoneyRect[2],self.MoneyRect[3]))
        self.MoneyText = self.text.render(('Money:' + str(self.Money)),True,(100,100,100))

        if ExitRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                M1.Start = True
                print('ddd')

        if BuyRect_1.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                if self.Money >= 100:
                    self.Money -= 100
                    self.pickaxe = ['stone_pickaxe',2]

        if BuyRect_2.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                if self.Money >= 500:
                    self.Money -= 500
                    self.pickaxe = ['iron_pickaxe',3]

        if StoneRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.Mineral = 'Stone'

        if IronRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.Mineral = 'Iron'

        if SilverRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.Mineral = 'Silver'

        if GoldRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.Mineral = 'Gold'

        if DiamondRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.Mineral = 'Diamond'

        if ButtRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                #if Op.Minerals[self.Mineral] != 'None':

                        try:
                            if self.Mineral == None:
                                raise Blad(self,'Wybierz blok')
                            else:
                                if Op.Minerals[self.Mineral] > 0:
                                    if self.Mineral == 'Stone':
                                        self.Money += 1
                                        Op.Minerals[self.Mineral] -= 1

                                    if self.Mineral == 'Iron':
                                        self.Money += 20
                                        Op.Minerals[self.Mineral] -= 1

                                    if self.Mineral == 'Silver':
                                        self.Money += 50
                                        Op.Minerals[self.Mineral] -= 1

                                    if self.Mineral == 'Gold':
                                        self.Money += 150
                                        Op.Minerals[self.Mineral] -= 1

                                    if self.Mineral == 'Diamond':
                                        self.Money += 300
                                        Op.Minerals[self.Mineral] -= 1
                        except Blad as pe:
                            print(pe,pe.blok)

        #print(self.Mineral)


    def Shop(self):
        for block in M1.blocks_rect:
            if self.Player_rect.colliderect(block[1]) and block[2] == 'Shop' and pygame.key.get_pressed()[pygame.K_e]:
                M1.Start = False
                while True:
                    if M1.Start == False:
                        disp.root.fill((0, 0, 0))
                        self.ShopDisp()
                        pygame.display.update()
                    else:
                        break
                    for i in pygame.event.get():
                        if (i.type == pygame.QUIT):
                            quit()

    def Records(self):
        a = self.Money
        b = datetime.now()
        c = b.strftime("%H:%M:%S")
        today = datetime.today()
        date = today.strftime("%B %d, %Y")
        g = "Money: " + str(a) + " Time: " + str(c) + " " + str(date)
        f = open("Record.txt", "w+")
        f.write(g)
        f.close()

Play = Player()


M1.BlockLoc()

while True:
    #M1.scroll[0] -= (Play.Player_rect[0]+M1.scroll[0]-750)/20
    if M1.Start == True:
        pygame.time.Clock().tick(60)
        disp.root.fill((0,0,0))

        M1.DisplayMap()
        Play.DispPlayer(disp.root)

        #print(M1.blocks_rect)

    for i in pygame.event.get():
        if (i.type == pygame.QUIT):
            Play.Records()
            quit()
    pygame.display.update()
    #pygame.display.flip()