def binaryToDecimal(binaryNumber) :
    binaryAsString = str(binaryNumber)

    result = 0
    power = 0
    for i in range(len(binaryAsString)-1, -1, -1):
        digit = int(binaryAsString[i])
        result += digit* 2**power
        power+=1

    return result
binary = int(input())
decimal = binaryToDecimal(binary)
print(decimal)