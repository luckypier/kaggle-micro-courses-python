# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:43:20 2019

@author: Pierre Recuay
"""

game = [[0,0,0],
[0,0,0],
[0,0,0],]

  
def print_game(game_map, player='X', row=0, column=0, just_display=False):
    
    
    if not (player == 'X' or player == 'O'):
        raise Exception('Player must be X or O, not {}'.format(player)) 
    
    try:         
        if not just_display:
            game_map[row][column] = player        
    except IndexError as e:
        print("Error, x and y must be less equal to 2!", e)
    else:
        print("Valid inputs")
        
    print('='*20, "\n", "  0  1  2")
    for row, value in enumerate(game_map):
        print(row, value)
    return game_map
    




game = print_game(game, just_display=True)

y = int(input('Y --> '))
x = int(input('X --> '))
game = print_game(game, 'X',y,x)

y = int(input('Y --> '))
x = int(input('X --> '))
game = print_game(game, 'E',y,x)


''' PART 8
x = 1

def mod():
    #global x
    x = 2
    

mod()
print(x)
'''

# finish 