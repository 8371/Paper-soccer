import pygame
import time
from pprint import pprint
zapis=''
def start():
    global srodek,table,ekran,boisko,lenx,leny,o,draw,color,out,table,zapis,zmianax,x
    srodek=[7,5]
    table = [['0'] * 11 for i in range(15)]
    ekran = pygame.display.set_mode((382,565))
    boisko = pygame.image.load('boisko.png')
    ekran.blit(boisko,(0,0))
    lenx,leny,o,draw,color,out=[191],[282],46,3,(0,0,0),8
    pygame.init()
    for i in range(15):                      
        table[i][0]='471'
    for i in range(15):                      
        table[i][1]='28'
    for i in range(15):
        table[i][9]='28'                        
    for i in range(15):
        table[i][10]='693'
    for i in range(2):
        table[2][2+i]='46'
    for i in range(2):
        table[2][7+i]='46'
    table[2][1]='2846'
    table[2][4]='6'
    table[2][6]='4'
    table[1][6]='8'
    table[1][4]='8'
    table[2][9]='468'
    table[1][7]='9'
    table[1][3]='7'
    for i in range(2):
        table[1][2+i]='798'
    table[1][4]='9'
    table[1][1]='728'
    for i in range(2):
        table[1][7+i]='789'
    table[1][6]='7'
    table[1][9]='98'
    table[13][2]='123'
    table[13][1]='123'
    table[13][3]='123'
    table[12][2]='46'
    table[12][3]='46'
    table[12][1]='4'
    table[13][4]='3'
    table[12][4]='6'
    table[13][4]='23'
    table[13][6]='2'
    table[13][7]='123'
    table[13][8]='123'
    table[12][7]='46'
    table[12][8]='46'
    table[13][6]='12'
    table[13][9]='3'
    table[13][9]='23'
    x=-1
    zmianax=-1
def cofka():
    e=2
def przycisk(x,x1):
    font = pygame.font.SysFont("comicsansms",25)
    text = font.render("X: "+str(x), True,(0,0,0))
    ekran.blit(text, (0,0))
    font = pygame.font.SysFont("comicsansms",15)
    gracz = font.render("Move : "+str(x1), True,(0,0,0))
    ekran.blit(gracz, (15,530))

    
def zmianakkk(x1,x2,x3,x4,x5,x6):
    global out,color,zmianax,zapis
    zapis=zapis+str(x1)
    if table[srodek[0]+x5][srodek[1]+x6]=='0':
        zmianax=zmianax*-1
        #zapis+='.'
    if str(x1) not in table[srodek[0]+x5][srodek[1]+x6]:
        table[srodek[0]][srodek[1]]+=str(x2)
        srodek[0]+=x5
        srodek[1]+=x6
        table[srodek[0]][srodek[1]]+=str(x1)
        pygame.draw.line(ekran,color,(lenx[0],leny[0]),(lenx[0]+x3,leny[0]+x4),draw)
        lenx[0] += x3
        leny[0] += x4
        checkx()
        pygame.draw.rect(ekran, (255,255,255),(0,0,80,30))
        pygame.draw.rect(ekran, (255,255,255),(0,520,130,530))
        if zmianax==1:            
            color=(255,0,0)
            graczx='Player'
        if zmianax==-1:
            graczx='Pc'
            color=(0,0,0)
        przycisk(out,graczx)
def zmiana(x):
    if x==1:
        zmianakkk(1,9,-o,+o,+1,-1)
    if x==3:
        zmianakkk(3,7,+o,+o,+1,+1)
    if x==7:
        zmianakkk(7,3,-o,-o,-1,-1)
    if x==9:
        zmianakkk(9,1,+o,-o,-1,+1)
    if x==4:
        zmianakkk(4,6,-o,+0,+0,-1)
    if x==8:
        zmianakkk(8,2,+0,-o,-1,+0)
    if x==2:
        zmianakkk(2,8,+0,+o,+1,+0)
    if x==6:
        zmianakkk(6,4,+o,+0,+0,+1)
def checkx():
    global srodek,out
    out=8
    try:
        if '6' in table[srodek[0]][srodek[1]+1]:
            out-=1
        if '4' in table[srodek[0]][srodek[1]-1]:
            out-=1
        if '8' in table[srodek[0]-1][srodek[1]]:
            out-=1
        if '2' in table[srodek[0]+1][srodek[1]]:
            out-=1
        if '7' in table[srodek[0]-1][srodek[1]-1]:
            out-=1
        if '3' in table[srodek[0]+1][srodek[1]+1]:
            out-=1
        if '9' in table[srodek[0]-1][srodek[1]+1]:
            out-=1
        if '1' in table[srodek[0]+1][srodek[1]-1]:
            out-=1
    except:
        print('error')
        print(srodek)
def koniec():
    zapis=''
    if input('ok')=='1':
        start()

def check():
    if out==0:
        print('end')
        koniec()
    if srodek==[13,4] or srodek==[13,5] or srodek ==[13,6]:
        print('win')
        koniec()
    if srodek==[1,4] or srodek==[1,5] or srodek ==[1,6]:
        print('win')
        koniec()    
        
def pilka():
    global srodek,zapis
    while True:
        check()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP6:                    
                    zmiana(6)
                if event.key == pygame.K_KP2:                    
                    zmiana(2)
                if event.key == pygame.K_KP8:
                    zmiana(8)                                       
                if event.key == pygame.K_KP4:                    
                    zmiana(4)
                if event.key == pygame.K_KP9:                   
                    zmiana(9)
                if event.key == pygame.K_KP7:                    
                    zmiana(7)
                if event.key == pygame.K_KP1:                    
                    zmiana(1)
                if event.key == pygame.K_KP3:                    
                    zmiana(3)
                if event.key == pygame.K_y:
                    test=0
                if event.key == pygame.K_d:
                    print(zapis)
                if event.key == pygame.K_f: # odpala poczatek, wypisuje zapis, usuwa os ruch
                    start()                    
                    print(zapis)
                    l1=zapis
                    l1=l1[:-1]
                    l=len(l1)
                    zapis=''
                    for i in range(l):
                        zmiana(int(l1[i]))           
                if event.key == pygame.K_u:
                    test=0
                if event.key == pygame.K_r:
                    start() #odpala poczatkowe ustawienie
                if event.key == pygame.K_p: # wyswietla srodek + tabele ustawiona
                    print(srodek)
                    for row in table:            
                        print(' '.join([str(elem) for elem in row]))
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
start()
pilka()
