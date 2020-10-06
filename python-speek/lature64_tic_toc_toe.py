#!/usr/bin/python3

from IPython.display import clear_output

def display_board(board): 
    clear_output()   
    print(board[7]+'|'+board[8]+'|'+board[9])    
    print(board[4]+'|'+board[5]+'|'+board[6])    
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('----------------------')    

def player_input():
    '''
    OUTPUT = (player1,player2)
    '''
    marker = ""
    
    while marker !='X' and marker !='O':
        marker = input("Player 1 choose (X,O): ").upper()
        print(marker)
    
    player1 = marker

    if player1 =='X':
        player2 = 'O'
    else:
        player2 = 'X'

    return  (player1,player2)

def palce_marker(board,marker,position):
    board[position] = marker
    display_board(list_a)

list_a = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#display_board(list_a) 
palce_marker(list_a,'$',8)

#player1 , player2 = player_input()
#print(player1 + player2)