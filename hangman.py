import pygame as pg 
from pygame.locals import *
import sys, requests, json
import pygame_textinput as pgti

# fetching list of words 
def fetchWords(lista):
    f = open("words.txt", "r");
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

def message_to_screen(msg,color,screen, font, dimensions):
    screen_text = font.render(msg,True,color)
    screen.blit(screen_text,dimensions)
    pg.display.update()

def startGame():
    pg.init()
    background = 229,198,84
    black = 0,0,0
    screen_size = screen_width, screen_height = 800,600


    
    screen = pg.display.set_mode(screen_size)
    font = pg.font.Font(None,45)
    fontP1 = pg.font.Font(None,25)


    screen.fill(background)



    pg.display.flip() 
    text_input = pgti.TextInput()
    # message_to_screen("Welcome to Hangman", black,screen,font,[230,100])
    # message_to_screen("Player 1 enter word: ", black,screen,fontP1,[300,180])
    # message_to_screen(player1_text, black,screen,fontP1,[0,0]) 
    clock = pg.time.Clock()
    player1_text =''

    while True:
        screen.fill(background)
        message_to_screen("Welcome to Hangman", black,screen,font,[230,100])
        message_to_screen("Welcome to Hangman", black,screen,font,[330,100])
        # message_to_screen("Player 1 enter word: ", black,screen,font,[300,180])
        message_to_screen(player1_text, black,screen,font,[0,0])
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        
        # text_input.update(events)   
        # screen.blit(text_input.get_surface(), (10, 10))
        # pg.display.update()
        
            if event.type==pg.KEYDOWN:
                
                
                if event.key ==pg.K_BACKSPACE:
                    player1_text = player1_text[:-1]
                    
                    pg.display.update()
                else:
                    player1_text += event.unicode   
        clock.tick(30)
        


lista = []
lista = fetchWords(lista)




longest_word = findLongest(lista)


startGame()




