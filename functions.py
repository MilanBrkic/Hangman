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
        height = 450+i*50
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


def ponderFonta(n):
    if n<2:
        return 120
    elif n<9:
        return 100
    elif n<15:
        return 60
    else: return 50

def displaySyllable(syllable, crta, screen, hangman_rec):
    p = ponderFonta(len(hangman_rec))
    font_slovo =  pg.font.Font(None,p)
    up = 60
    if len(hangman_rec)>9:
        up = 35
    message_to_screen(syllable,colors['Black'], screen,font_slovo, (crta.coord1.x+10,crta.coord1.y-up))

def moreThanTwoSylabbles(hangman_rec,lista_crta, syllable,screen):
    index = 0
    for x in hangman_rec:
        if x==syllable:
            crta = lista_crta[index]
            displaySyllable(syllable, crta, screen, hangman_rec)
        index+=1


def horizontalLine(screen):
    pg.draw.line(screen, colors['Black'], (510, 400), (590, 400), 3)

def verticalLine(screen):
    pg.draw.line(screen, colors['Black'], (550, 400), (550, 230), 3)

def horiAndVerLine(screen):
    pg.draw.line(screen, colors['Black'], (550, 230), (620, 230), 3)
    pg.draw.line(screen, colors['Black'], (620, 230), (620, 250), 3)

def drawHead(screen):
    pg.draw.circle(screen, colors['Black'], (620,270), 20, 3)

def drawBody(screen):
    pg.draw.line(screen, colors['Black'], (620, 290), (620, 350), 3)

def drawRightArm(screen):
    pg.draw.line(screen, colors['Black'], (620, 300), (650, 320), 4)

def drawLeftArm(screen):
    pg.draw.line(screen, colors['Black'], (620, 300), (590, 320), 4)

def drawRightLeg(screen):
    pg.draw.line(screen, colors['Black'], (620, 350), (650, 380), 4)

def drawLeftLeg(screen):
    pg.draw.line(screen, colors['Black'], (620, 350), (590, 380), 4)
    

def drawHangman(screen,broj_gresaka):
    kraj=False
    if broj_gresaka==1:
        horizontalLine(screen)
    elif broj_gresaka==2:
        verticalLine(screen)
    elif broj_gresaka==3:
        horiAndVerLine(screen)
    elif broj_gresaka==4:
        drawHead(screen)
    elif broj_gresaka==5:
        drawBody(screen)
    elif broj_gresaka==6:
        drawRightArm(screen)
    elif broj_gresaka==7:
        drawLeftArm(screen)
    elif broj_gresaka==8:
        drawRightLeg(screen)
    elif broj_gresaka==9:
        drawLeftLeg(screen)
        message_to_screen("You LOSE!!!", colors['Red'], screen,pg.font.Font(None,65) , (50, 300))
        kraj=True

    pg.display.update()
    return kraj