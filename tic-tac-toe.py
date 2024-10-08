# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:52:40 2024

@author: IITM
"""

# import tkinter as tk
# from tkinter import font

import numpy as np
import random

def create_board():
    board = np.full(shape = (3,3), fill_value = '-')
    return (board)

def pos_dict(board):
    n = 0
    pos_lib = {}
    for i in range(len(board)):
        for j in range(len(board)):
            pos_lib[n]=(i,j)
            n+=1
    return pos_lib
    
    
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                l.append((i,j))
    return l

def get_place(board, pos_lib):
    print ("Current board:")
    print (board)
    print ("=" * len(board) * len(board) * 2)
    print ('Select a Position to place:') # for now
    x = random.choice(possibilities(board)) # for now
    # x = input('Select a Position to place:')
    return x # for now
    # return pos_lib[x]

def place_piece(board, pos, c_player, i):
    print ("Current board:")
    print (board)
    print ("=" * len(board) * len(board) * 2)
    print ('Board after the '+ c_player + "'s move:")
    board[pos] = i
    print(board)
    print ("=" * len(board) * len(board) * 2)
    return board

def column_check(board, i): 
    for j in range(len(board)):
        l = []
        for k in range(len(board)):
            l.append(board[j][k])

        if l.count(l[0]) == len(l) and l[0] == i:
            return True
        else:
            continue
    return False


def row_check(board, i): 
    for j in range(len(board)):
        l = []
        for k in range(len(board)):
            l.append(board[k][j])

        if l.count(l[0]) == len(l) and l[0] == i:
            return True
        else:
            continue
    return False
    
def diag_check(board, i): 
    for j in range(len(board)):
        l = []
        for k in range(len(board)):
            l.append(board[k][j])
        return np.allclose(l, l[0])
        
def check_win(board, c_player, i):
    if column_check(board, i) or row_check(board, i):
        print (c_player + ' wins!!!')
        return 1
    else:
        return 0
            
            
def play_game():
    board, winner, state = create_board(), 0, 'draw'
    print(board)

    print ("Choose your symbol[X/O]:")
    player = 'X' # for now
    # player = input ("Choose your symbol[X/O]:")
    player = player.upper()
    pos_lib = pos_dict(board)
    
    
    while winner == 0:
        for i in ['X', 'O']:
            if len(possibilities(board))!=0:
                if i == player:
                    pos = get_place(board, pos_lib)
                    c_player = 'Human'
                else:
                    pos = random.choice(possibilities(board))
                    c_player = 'Computer'
                while pos not in possibilities(board):
                    print ('Position already occupied!!')
                    pos = get_place(board, pos_lib)
                board = place_piece(board, pos, c_player, i)
                winner = check_win(board, c_player, i)
                if winner == 1:
                    state = 'win'
                    break
            else:
                winner = -1
    if state == 'draw':
        print ('The match is a draw!')
        
#%%
play_game()