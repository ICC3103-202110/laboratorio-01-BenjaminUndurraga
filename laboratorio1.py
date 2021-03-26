from numpy import random
import numpy as np

cards_to_play = int(input('with how many pairs of cards you want to play?: '))
cards = []
player1=0
player2=0
turn = 0
total_points=0

#crearemos los pares de cartas a jugar
card_creator = 1
while card_creator <= cards_to_play:
    cards.append(card_creator)
    cards.append(card_creator)
    card_creator+=1
'''
print(cards), estan bien creadas, falta desordenarlas, para esto tendremos 
que ponerlas en otra lista
'''
messy_cards = []

while len(cards)>0:
    messing_up = cards[random.randint(len(cards))]
    messy_cards.append(messing_up)
    cards.remove(messing_up)
'''
sacamos las cartas de cards y las pusimos en messy_cards desordenadas.
ahora tenemos que pasar messy_cards a matriz para que sea un tablero con coordenadas.
'''

board = np.array(messy_cards).reshape(2,cards_to_play)
#lo hacemos de dos columnas debido a que 2 es el minimo de cartas totales a jugar
print(board)

# tenemos el tablero pero falta definir el que lo ocultara

def silenced_board(rows,amount):
    m=[]
    for i in range(rows):
        rows=[]
        for j in range(amount):
            rows.append(' *')
        m.append(rows)
    return m

'''
def move(x1,y1): 

print(move)

me falta remover, imprimir tablero
'''
print(silenced_board(2,cards_to_play))
coordx = int(input('coord x: '))
coordy = int(input('coord y: '))
print(board[coordx-1][coordy-1])

coordx2 = int(input('coord x: '))
coordy2 = int(input('coord y: '))
print(board[coordx2 - 1][coordy2 - 1])
while coordx <=2:
    if board[coordx-1][coordy-1] == board[coordx2-1][coordy2-1]:
        print('correct! u can continue')
        board.remove([coordx-1][coordy-1])
        board.remove([coordx2-1][coordy2-1])
    else:
        print('incorrect :( turn of player 2. ')
        
print(silenced_board(2,cards_to_play))