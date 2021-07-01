# %%
import random 
def drowboard (bourd):
    print('' + bourd[0] +' | '+bourd[1] + ' | ' + bourd[2])
    print('---+---+---')
    print('' + bourd[3] +' | '+bourd[4] + ' | ' + bourd[5])
    print('---+---+---')
    print('' + bourd[6] +' | '+bourd[7] + ' | ' + bourd[8])
    
def inputplayerletter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('do you want X or O ?')
        letter = input().upper()
    if letter == 'X':
        return ['X','O']
    return ['O','X']

def howplayfirst():
    if random.randint(0,1)==0:
        return 'player2'
    return 'player1'
def playagin():
    print('do you want to play agin? (yes or not)')
    return input().upper().startswith('y')
    
def makemove(bourd,letter,move):
    bourd[move-1]=letter
    
def iswinner(bo,le):
    return ((bo[0]==le and bo[1]==le and bo[2]==le) or
        (bo[0]==le and bo[3]==le and bo[6]==le)or
        (bo[1]==le and bo[4]==le and bo[7]==le)or
        (bo[2]==le and bo[5]==le and bo[8]==le)or
        (bo[0]==le and bo[4]==le and bo[8]==le)or
        (bo[2]==le and bo[4]==le and bo[6]==le))
def spacefree(bourd,move):
    return bourd[move-1] == ' '

def getplayermove(bourd,player):
    move=0
    while move not in range(1,9):
        print(f'what is the next move {player}?(1,9)')
        move =int(input())
    return move
def bourdfull(bourd):
    return not any([x == ' ' for x in bourd])

print('welcome to "X" and "O" game')

while True:
    thebourd = [' '] * 9
    player1letter,player2letter = inputplayerletter()
    turn = howplayfirst()
    print('the '+turn+'will go first')
    gameisplaying = True

    while gameisplaying:
        if turn =='player1':
            letter = player1letter
        else:
            letter = player2letter
        drowboard(thebourd)
        move = getplayermove(thebourd,turn)
        makemove(thebourd,letter,move)
        if iswinner(thebourd,letter):
            drowboard(thebourd)
            print("you win the game")
            gameisplaying = False
        elif bourdfull(thebourd):
            drowboard(thebourd)
            print("the game is tie")
            gameisplaying = False
        if turn =='player1':
            turn ='player2'
        else:
            turn = 'player1'
    if not playagin():
        print("goodbye")
        break
         
        
        

# %%
