import pygame as pg 
from pygame.locals import *
from pygame.draw import *
import sys, requests
from functions import *
from classes import Line,Coordinate, WidthLimits,HeightLimits,DimensionLimits

colors = {"Orange":(229,198,84), "Black":(0,0,0), "Red":(255,0,0) }
dimension_list = []
used_syllables = []


def startGame(lista):
    pg.init()
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
                            hangman_rec = hangman_rec.upper()
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
                    lista_crta = crtaj(hangman_rec, screen)
                    message_to_screen('Player 2 pick a letter:',colors['Black'], screen, font, (50, 400) )
                    displayButtons(screen, dimension_list)
                    broj_gresaka=0
                    displayed = True

                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                if event.type == pg.MOUSEMOTION:
                    x,y = pg.mouse.get_pos()
                    usao = False
                    for i in dimension_list:
                        if i.width.lower<x and i.width.upper>x and i.height.lower<y and i.height.upper>y:
                            pg.mouse.set_cursor(*pg.cursors.tri_left)
                            usao = True
                    if not usao:
                        pg.mouse.set_cursor(*pg.cursors.arrow)

                if event.type == pg.MOUSEBUTTONDOWN:
                    kraj = False
                    x,y = pg.mouse.get_pos()
                    for i in dimension_list:
                        if i.width.lower<x and i.width.upper>x and i.height.lower<y and i.height.upper>y:
                            index = hangman_rec.find(i.syllable)
                            if index>-1:
                                used_syllables.append(i.syllable)
                                
                                if hangman_rec.count(i.syllable)==1:
                                    crta = lista_crta[index]
                                    displaySyllable(i.syllable, crta, screen, hangman_rec,colors['Black'])
                                else:
                                    moreThanTwoSylabbles(hangman_rec,lista_crta, i.syllable,screen)
                            else:
                                broj_gresaka+=1
                                kraj = drawHangman(screen, broj_gresaka)
                                if kraj:
                                    dimension_list.clear()
                                    drawRest(used_syllables,hangman_rec, lista_crta, screen)
                            drawAnX(i, screen)
                            if not kraj:
                                dimension_list.remove(i)
                                if isItDone(used_syllables, hangman_rec):
                                    dimension_list.clear()
                                    drawWin(screen)
                
        
        
        clock.tick(30)            
        


lista = []
lista = fetchWords(lista)




longest_word = findLongest(lista)


startGame(lista)




