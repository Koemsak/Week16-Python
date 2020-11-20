array2D = eval(input())
nbRows = len(array2D)
nbColumns = len(array2D[0])
sevenRow = -1
sevenColumn = -1
for row in range(nbRows):
    for column in range(nbColumns):
        number = array2D[row][column]
        if number == 7 :
            sevenRow = row
            sevenColumn = column
sevenPosition = [sevenRow, sevenColumn]
print(sevenPosition)