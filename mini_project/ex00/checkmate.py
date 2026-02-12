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

    def Pawn(my_row, my_col) :
        if [my_row - 1, my_col - 1] == king or [my_row - 1, my_col + 1] == king :
            print("Success")
            return True
        return False  
    
    def move_Bishop_Rook(my_row, my_col, move) :
        for i in move :
            my_position = [my_row, my_col]
            while (0 <= my_position[0] < size) and (0 <= my_position[1] < size):
                my_position[0] += i[0]
                my_position[1] += i[1]
                if my_position == king :
                    print("Success")
                    return True
        return False

    def Bishop(my_row, my_col) :
        move = [[-1,-1], [-1,1], [1, -1], [1, 1]]
        return move_Bishop_Rook(my_row, my_col, move)
    
    def Rook(my_row, my_col) :
        move = [[-1,0], [1,0], [0, -1], [0, 1]]
        return move_Bishop_Rook(my_row, my_col, move)

    def Queen(my_row, my_col) :
        if Bishop(my_row, my_col) :
            return True
        elif Rook(my_row, my_col) :
            return True
        return False
    
    for i in range(size) :
        for j in range(size) :
            if list_board[i][j] == "P" :
                if Pawn(i, j) :
                    return
            if list_board[i][j] == "B" :
                if Bishop(i, j) :
                    return
            if list_board[i][j] == "R" :
                if Rook(i, j) :
                    return
            if list_board[i][j] == "Q" :
                if Queen(i, j) :
                    return
    print("Fail")