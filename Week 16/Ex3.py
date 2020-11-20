def getMinimumIndex (list):
    minIndex = 0
    for i in range (len(list)):
        if list [i] < list [minIndex]:
            minIndex = i
    return minIndex
initialList = eval(input())
sortedList = []
for i in range (len(initialList)):
    minIndex = getMinimumIndex(initialList)
    sortedList.append(initialList[minIndex])
    initialList.pop(minIndex)
print(sortedList)