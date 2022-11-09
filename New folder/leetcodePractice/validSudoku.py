# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according 
# to the following rules:

#boolean = false
#1. Each row must contain the digits 1-9 without repetition.
# this can be done with a loop to compare all numbers with each other
#board[0][0-9] #gets the 1st row
# return = false #if there is repetition

#2. Each column must contain the digits 1-9 without repetition.
#board[0-9][0] #gets the 1st row
# return = false #if there is repetition

#3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#board[0-3][0-3] #goes through columns and rows of 3x3 dimensions
# return = false #if there is repetition

#4. once all is checked return true

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

#Each row must contain the digits 1-9 without repetition.
# for x in len(board):
#     for j in len(board[x]):
#          board[x][j] != 

#square 
# for x in range(3):
#     for i in range(3):
#         print(board[x][i])

