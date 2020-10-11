import pygame as pg 
from pygame.locals import *
from pygame.draw import *
import sys, requests, json,math
from classes import Line,Coordinate, WidthLimits,HeightLimits,DimensionLimits

colors = {"Orange":(229,198,84), "Black":(0,0,0), "Red":(255,0,0) }

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
    return lista


def message_to_screen(msg,color,screen, font, dimensions):
        screen_text = font.render(msg,True,color)
        screen.blit(screen_text,dimensions)
        pg.display.update()

def getAlphabet():
    alphabet = []
    for x in range(26):
        alphabet.append(chr(ord('A')+x))
    return alphabet

def displayButtons(screen, dimension_list):
    alphabet = getAlphabet()
    font = pg.font.Font(None,35)
    for i in range(3):
        width = 50
        height = 400+i*50
        for j in range(9):
            if i==2 and j==8:
                break
            inner_width = width+65*j
            word = alphabet[i*9+j]
            
            dimension_list.append(DimensionLimits(word,WidthLimits(inner_width,40), HeightLimits(height,40)))
            pg.draw.rect(screen, colors['Black'], (inner_width, height, 40, 40), 2)
            
            message_to_screen(word, colors['Black'], screen, font, (inner_width+10, height+10))

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

def drawAnX(s, screen):
    pg.draw.line(screen,colors['Red'],(s.width.lower,s.height.lower), (s.width.upper,s.height.upper), 3)
    pg.draw.line(screen,colors['Red'],(s.width.lower,s.height.upper), (s.width.upper,s.height.lower), 3)
    pg.display.update()

def checkWord(lista, word):
    if word in lista:
        return True

def displaySyllable(syllable, crta, screen):
    font_slovo =  pg.font.Font(None,100)
    message_to_screen(syllable,colors['Black'], screen,font_slovo, (crta.coord1.x+10,crta.coord1.y-60))

def moreThanTwoSylabbles(hangman_rec,lista_crta, syllable,screen):
    index = 0
    for x in hangman_rec:
        if x==syllable:
            crta = lista_crta[index]
            displaySyllable(syllable, crta, screen)
        index+=1
            