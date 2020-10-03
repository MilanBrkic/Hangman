import pygame as pg 
from pygame.locals import *
from pygame.draw import *
import sys, requests, json

colors = {"Orange":(229,198,84), "Black":(0,0,0), "Red":(255,0,0) }


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
                    pg.display.update()
                    displayed = True
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                
        
        
        clock.tick(30)            
        


lista = []
lista = fetchWords(lista)




longest_word = findLongest(lista)


startGame(lista)




