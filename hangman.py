import pygame as pg 
from pygame.locals import *
from pygame.draw import *
import sys, requests, json,math

colors = {"Orange":(229,198,84), "Black":(0,0,0), "Red":(255,0,0) }

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printSelf(self):
        print(self.x, self.y)

class Line:
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

def ponder(n):
    if n<2:
        return 350
    elif n<3:
        return 300
    elif n<5:
        return 250
    elif n<10:
        return 70
    elif n<15:
        return 20
    else: return 10

def crtaj(rec, screen):
    screen_width =800
    n = len(rec)
    pocetni = ponder(n)
    razmak = math.ceil((screen_width-pocetni*2)/n)
    lista = []

    
    for x in range(len(rec)):
        c1 = Coordinate(math.ceil(pocetni+x*razmak), 150)
        c2 = Coordinate(math.ceil(pocetni+x*razmak+razmak*0.8), 150)
        linija = Line(c1,c2)
        lista.append(linija)
    for x in lista:
        pg.draw.line(screen, colors['Black'], (x.coord1.x,x.coord1.y), (x.coord2.x,x.coord2.y),3)
        pg.display.update()


# fetching list of words 
def fetchWords(lista):
    f = open("words.txt", "r")
    words  = f.read()
    lista = words.split()
    return lista

def findLongest(lista):
    maxRec = lista[0]
    max = len(lista[0])
    for x in lista:
        if len(x)>max:
            max = len(x)
            maxRec = x
    return maxRec, max


def checkWord(lista, word):
    if word in lista:
        return True



def startGame(lista):

    def message_to_screen(msg,color,screen, font, dimensions):
        screen_text = font.render(msg,True,color)
        screen.blit(screen_text,dimensions)
        pg.display.update()

    pg.init()
    background = 229,198,84
    black = 0,0,0
    red = 255,0,0

    screen_size = screen_width, screen_height = 800,600


    
    screen = pg.display.set_mode(screen_size)
    font = pg.font.Font(None,45)
    fontP1 = pg.font.Font(None,25)
    fontInput = pg.font.Font(None,35)
    fontWarning = pg.font.Font(None, 20)
    screen.fill(colors["Orange"])
    hangman_rec = ''


    pg.display.flip() 
    player1_text =''
    warning = ''
    def putObjectsMenu():
        screen.fill(colors["Orange"])
        message_to_screen("Welcome to Hangman", colors["Black"],screen,font,[230,150])
        message_to_screen("Player 1 enter word: ", colors["Black"],screen,fontP1,[315,220]) 
        pg.draw.rect(screen, colors["Black"], (150,270,500,50), 2)
        message_to_screen(player1_text, colors["Black"],screen,fontInput,[152,285])
        message_to_screen(warning, colors["Red"],screen,fontWarning,[152,250])
    
    
    
    putObjectsMenu()
    
    
    clock = pg.time.Clock()
    startMenu = True
    displayed = False
    while True:
        
        
        events = pg.event.get()
        
            
        for event in events:
            if startMenu:    
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type==pg.KEYDOWN:
                    warning = ""
                    if event.key ==pg.K_BACKSPACE:
                        player1_text = player1_text[:-1]
                        pg.display.update()
                    elif event.key == pg.K_SPACE:
                        warning = "Words do not have space in them"
                    elif event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                        if checkWord(lista, player1_text):
                            hangman_rec = player1_text
                            startMenu = False
                        else:
                            warning = "ne postoji rec"
                    else:
                        if len(player1_text)>22:
                            warning= "Cannot be longer than 22 characters"
                        else:
                            player1_text += event.unicode
                    putObjectsMenu()
            else:
                if not displayed:
                    screen.fill(colors['Orange'])
                    crtaj(hangman_rec, screen)
                    message_to_screen('Player 2 guess pick a letter:',colors['Black'], screen, font, (180, 200) )
                    displayed = True
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                
        
        
        clock.tick(30)            
        


lista = []
lista = fetchWords(lista)




longest_word = findLongest(lista)


startGame(lista)




