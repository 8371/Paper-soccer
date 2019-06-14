import pygame
import time
from pprint import pprint
#stores information about movements
made_movements=''
def start():
    global center,table,board,court,position_x,position_y,o,draw,color,possible_line_directions,table,made_movements,change_color,x
    #Center where we start game
    center=[7,5]
    table = [['0'] * 11 for i in range(15)]
    #Creating table for game, board in pygame
    board = pygame.display.set_mode((382,565))
    court = pygame.image.load('court.png')
    board.blit(court,(0,0))
    #coordinates in pygame board
    position_x,position_y=[191],[282]
    #line length pixels
    o=46
    #size draw line
    draw=3
    #color first draw line
    color=(0,0,0)
    #possible line directions
    possible_line_directions=8
    pygame.init()
    #change color players
    change_color=-1
    #This table... include in foto Image_1.png.............
    #so that the player does not go beyond the map
    for i in range(2):
        table[1][2+i]='798'
    for i in range(2):
        table[1][7+i]='789'
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
    table[1][1]='728'
    table[1][3]='789'
    table[1][4]='98'
    table[1][6]='78'
    table[1][7]='789'
    table[1][9]='98'
    table[2][1]='2846'
    table[2][4]='6'
    table[2][6]='4'
    table[2][7]='46'
    table[2][9]='468'
    table[12][1]='42'
    table[12][2]='46'
    table[12][3]='46'    
    table[12][4]='6'
    table[12][6]='4'
    table[12][7]='46'
    table[12][8]='46'
    table[12][9]='62'
    table[13][1]='123'    
    table[13][2]='123'
    table[13][3]='123'
    table[13][4]='23'
    table[13][6]='12'
    table[13][7]='123'
    table[13][8]='123'
    table[13][9]='23'
def Result(x,x1):
    #display information about possible line directions and who is making move
    font = pygame.font.SysFont("comicsansms",25)
    text = font.render("X: "+str(x), True,(0,0,0))
    board.blit(text, (0,0))
    font = pygame.font.SysFont("comicsansms",15)
    Player = font.render("Move : "+str(x1), True,(0,0,0))
    board.blit(Player, (15,530))
def make_move(x):
    if x==1:
        check_move(1,9,-o,+o,+1,-1)
    if x==3:
        check_move(3,7,+o,+o,+1,+1)
    if x==7:
        check_move(7,3,-o,-o,-1,-1)
    if x==9:
        check_move(9,1,+o,-o,-1,+1)
    if x==4:
        check_move(4,6,-o,+0,+0,-1)
    if x==8:
        check_move(8,2,+0,-o,-1,+0)
    if x==2:
        check_move(2,8,+0,+o,+1,+0)
    if x==6:
        check_move(6,4,+o,+0,+0,+1)
def check_move(x1,x2,x3,x4,x5,x6):
    global change_color
    #If new move change color next player
    if table[center[0]+x5][center[1]+x6]=='0':
        change_color=change_color*-1
    #check possible to make move
    if str(x1) not in table[center[0]+x5][center[1]+x6]:
        do_move(x1,x2,x3,x4,x5,x6)
def do_move(x1,x2,x3,x4,x5,x6):
    global possible_line_directions,color,change_color,made_movements
    made_movements=made_movements+str(x1)
    #adding number to table
    table[center[0]][center[1]]+=str(x2)
    center[0]+=x5
    center[1]+=x6
    table[center[0]][center[1]]+=str(x1)
    #draw line
    pygame.draw.line(board,color,(position_x[0],position_y[0]),(position_x[0]+x3,position_y[0]+x4),draw)
    position_x[0] += x3
    position_y[0] += x4
    #check number possible line directions for display
    check_possible_line_directions()
    pygame.draw.rect(board, (255,255,255),(0,0,80,30))
    pygame.draw.rect(board, (255,255,255),(0,520,130,530))
    if change_color==1:            
        color=(255,0,0)
        Playerx='Player 2'
    if change_color==-1:
        Playerx='Player 1'
        color=(0,0,0)
    Result(possible_line_directions,Playerx)
def check_possible_line_directions():
    global center,possible_line_directions
    possible_line_directions=8
    try:
        if '6' in table[center[0]][center[1]+1]:
            possible_line_directions-=1
        if '4' in table[center[0]][center[1]-1]:
            possible_line_directions-=1
        if '8' in table[center[0]-1][center[1]]:
            possible_line_directions-=1
        if '2' in table[center[0]+1][center[1]]:
            possible_line_directions-=1
        if '7' in table[center[0]-1][center[1]-1]:
            possible_line_directions-=1
        if '3' in table[center[0]+1][center[1]+1]:
            possible_line_directions-=1
        if '9' in table[center[0]-1][center[1]+1]:
            possible_line_directions-=1
        if '1' in table[center[0]+1][center[1]-1]:
            possible_line_directions-=1
    except:
        print('error')
        print(center)
def end():
    global made_movements
    made_movements=''
    start()
def check_win():
    #if possible line directions is 0 so game over and win opponent
    if possible_line_directions==0:
        if change_color == -1:
            print('Win Player 2')
        else:
            print('Win Player 1')  
        end()
    #when someone shoots a goal
    if center==[13,4] or center==[13,5] or center ==[13,6]:
        print('Win Player 2')
        end()
    if center==[1,4] or center==[1,5] or center ==[1,6]:
        print('Win Player 1')
        end()

def possible_movees():
    global center
    moves=[]
    try:
        if not'6' in table[center[0]][center[1]+1]:
            moves.append('6')
        if not '4' in table[center[0]][center[1]-1]:
            moves.append('4')
        if not '8' in table[center[0]-1][center[1]]:
            moves.append('8')
        if not '2' in table[center[0]+1][center[1]]:
            moves.append('2')
        if not '7' in table[center[0]-1][center[1]-1]:
            moves.append('7')
        if not '3' in table[center[0]+1][center[1]+1]:
            moves.append('3')
        if not '9' in table[center[0]-1][center[1]+1]:
            moves.append('0')
        if not '1' in table[center[0]+1][center[1]-1]:
            moves.append('1')
        print(moves)
    except:
        print('error')
        print(center)

def possible_moves():
    global center,made_movements
    
    moves=[]
    try:
        if not'6' in table[center[0]][center[1]+1]:
            moves.append('6')
        
        print(moves)
    except:
        print('error')
        print(center)
def make_movse():
    movek=[1,2,3,6]
    for i in movek:
        print(i)
        make_move(i)
#def answer():
    
    #Czy można wykonać X ruch.
    #Jeśli wykonam ten ruch czy moge zrobić następny?

    
def game():
    global center,made_movements
    while True:
        #check for somebody win 
        check_win()
        for event in pygame.event.get():
            #if player press key make move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP6:                    
                    make_move(6)
                if event.key == pygame.K_KP2:                    
                    make_move(2)
                if event.key == pygame.K_KP8:
                    make_move(8)                                       
                if event.key == pygame.K_KP4:                    
                    make_move(4)
                if event.key == pygame.K_KP9:                   
                    make_move(9)
                if event.key == pygame.K_KP7:                    
                    make_move(7)
                if event.key == pygame.K_KP1:                    
                    make_move(1)
                if event.key == pygame.K_KP3:                    
                    make_move(3)
                if event.key == pygame.K_w:
                    make_movse()
                if event.key == pygame.K_d:
                    print(made_movements)
                    print(center)
                    print(table)
                    possible_moves()
                if event.key == pygame.K_f or event.key == pygame.K_KP5 :
                    #When press key F clean board and restores the current state without last move
                    start()                    
                    l1=made_movements
                    l1=l1[:-1]
                    l=len(l1)
                    made_movements=''
                    for i in range(l):
                        make_move(int(l1[i]))           
                if event.key == pygame.K_r:
                    #When press key r reset game
                    made_movements=''
                    start() 
                if event.key == pygame.K_p: # display center + tabele 
                    print(center)
                    for row in table:            
                        print(' '.join([str(elem) for elem in row]))
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
start()
game()
