board1 = [[5,3,4,6,7,8,9,1,2],
				  [6,7,2,1,9,5,3,4,8],
				  [1,9,8,3,4,2,5,6,7],
				  [8,5,9,7,6,1,4,2,3],
				  [4,2,6,8,5,3,7,9,1],
				  [7,1,3,9,2,4,8,5,6],
				  [9,6,1,5,3,7,2,8,4],
				  [2,8,7,4,1,9,6,3,5],
				  [3,4,5,2,8,6,1,7,9]]
          
board2 = [[1,1,1,1,1,1,1,1,1],
				  [2,2,2,2,2,2,2,2,2],
				  [3,3,3,3,3,3,3,3,3],
				  [4,4,4,4,4,4,4,4,4],
				  [5,5,5,5,5,5,5,5,5],
				  [6,6,6,6,6,6,6,6,6],
				  [7,7,7,7,7,7,7,7,7],
				  [8,8,8,8,8,8,8,8,8],
				  [9,9,9,9,9,9,9,9,9]]

def getRow(board, rowNumber): #gets row of sudoku board
    return board[rowNumber-1]

def getColumn(board, columnNumber):#gets column of sudoku board4
    column = []
    for i in board:
        column.append(i[columnNumber-1])
    return column

def getSubsquare(board, sectRow, sectColumn):#gets subsquare of sudoku board
    subsquare = []
    if sectRow == 1:
        rows = [1, 2, 3]
    if sectRow == 2:
        rows = [4, 5, 6]
    if sectRow == 3:
        rows = [7, 8, 9]
    if sectColumn == 1:
        columns = [1, 2, 3]
    if sectColumn == 2:
        columns = [4, 5, 6]
    if sectColumn == 3:
        columns = [7, 8, 9]

    subsquare.append(getRow(board, rows[0])[columns[0]-1])
    subsquare.append(getRow(board, rows[0])[columns[1]-1])
    subsquare.append(getRow(board, rows[0])[columns[2]-1])
    subsquare.append(getRow(board, rows[1])[columns[0]-1])
    subsquare.append(getRow(board, rows[1])[columns[1]-1])
    subsquare.append(getRow(board, rows[1])[columns[2]-1])
    subsquare.append(getRow(board, rows[2])[columns[0]-1])
    subsquare.append(getRow(board, rows[2])[columns[1]-1])
    subsquare.append(getRow(board, rows[2])[columns[2]-1])
    return subsquare



def validateSudoku(board): #solution = true, else false
    idealList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in range(9):
        if sorted(getRow(board, i+1)) != idealList:
            return False
    for i in range(9):
        if sorted(getColumn(board, i+1)) != idealList:
            return False
    for i in range(3):
        for n in range(3):
             if sorted(getSubsquare(board, i+1, n+1)) != idealList:
                 return False
    return True
        

print(validateSudoku(board1))
