def hasSignOnRow(grid, rowIndex, sign):
    row = grid[rowIndex]
    return row[0] == sign and row[1] == sign and row[2] == sign
def hasSignOnColumn(grid, columnIndex, sign):
    signRow0 = grid[0][columnIndex]
    signRow1 = grid[1][columnIndex]
    signRow2 = grid[2][columnIndex]
    return signRow0 == sign and signRow0 == signRow1 and signRow1 == signRow2
def hasSignOnDiagonal(grid, sign):
    sign00 = grid[0][0]
    sign11 = grid[1][1]
    sign22 = grid[2][2]
    onDiagonal1 = sign00 == sign and sign00 == sign11 and sign11 == sign22
    sign02 = grid[0][2]
    sign11 = grid[1][1]
    sign20 = grid[2][0]
    onDiagonal2 = sign02 == sign and sign02 == sign11 and sign11 == sign20
    return onDiagonal1 or onDiagonal2
def hasSignWon(grid, sign):
    hasWon = False
 # 1- Check on the 3 olumns and 3 rows :
    for i in range(3):
        hasWon = hasWon or hasSignOnRow(grid, i, sign) or hasSignOnColumn(grid, i, sign)
 # 2- Check on the 2 diagonals :
    hasWon = hasWon or hasSignOnDiagonal(grid, sign)
    return hasWon
grid = eval(input())
if hasSignWon(grid, "A"):
    print("A WON")
elif hasSignWon(grid, "B"):
    print("B WON")
else:
    print("NO WINNER")