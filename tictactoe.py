board=["","","",
       "","","",
       "","",""]
def game_win():
    win=[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
    for i in ('X','O'):
        for k in range(len(win)):
            xx = True
            for x in range(3):
                if board[win[k][x]] != i:xx = False
            if xx==True:return i
def game_over():
    move=[]
    for i in range(len(board)):
        if board[i] == "":move.append(i)
    if len(move) == 0:return True,move
    else:return False,move
def make_move(player,position):
    global board
    board[position]=player
def change_player(player):
    if player == 'X': return 'O'
    else: return 'X'
def minimax(player):
    if game_win() == 'X':return -100
    if game_win() == 'O':return 100
    if game_over()[0] == True:return False
    if player == 'X':
        bestValue = 0
        for i in game_over()[1]:
            make_move(player,i)
            mini=minimax(change_player(player))
            make_move("",i)
            bestValue=min(bestValue,mini)
        return bestValue
    if player == 'O':
        bestValue = 0
        for i in game_over()[1]:
            make_move(player,i)
            mini=minimax(change_player(player))
            make_move("",i)
            bestValue=max(bestValue,mini)
        return bestValue
def best_move():
    global board,now
    for i in game_over()[1]:
        make_move('O',i)
        mini = minimax('X')
        make_move('',i)
        if mini>-100:
            make_move('O',i)
            print(mini,i,'done')
            now='player'
            break
        
def check_win():
    if game_win() == 'X':
        print('Win X')
    elif game_win() == 'O':
        print('Win O')
    elif game_over()[0] == True:
        print('Draw')
    else: return True
def show():
    print('...'+board[0]+'...'+board[1]+'...'+board[2]+'...')
    print('...'+board[3]+'...'+board[4]+'...'+board[5]+'...')
    print('...'+board[6]+'...'+board[7]+'...'+board[8]+'...')
