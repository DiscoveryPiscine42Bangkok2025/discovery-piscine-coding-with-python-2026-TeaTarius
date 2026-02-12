#!/usr/bin/env python3
def checkmate(board):
    
    if board.count("K") == 0:
        print("Error")
        return

    list_board = board.split()

    size = len(list_board) 
    for row in list_board:
        if len(row) != size :
            print("Error")
            return
        
    king = []
    for i in range(size): 
        for j in range(size):
            if list_board[i][j] == "K" :
                king = [i, j]
                break
        if king :
            break