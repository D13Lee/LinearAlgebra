#Run this file to
#construct a matrix from user input
#convert matrix to REF form
#print result and sequential steps taken
from matrixToREF import convertToREF

def main():
    matrix = userConstructMatrix()
    
    compressFloats(matrix)
    printMatrix(matrix)
    
    operationHistory = convertToREF(matrix)
    compressFloats(matrix)
    
    printHistory(operationHistory)
    printMatrix(matrix)
    
def printHistory(operationHistory):
    for line in operationHistory:
        print(line)

def userConstructMatrix():
    rows = int(input("Enter number of rows: "))
    matrix = []
    for i in range(rows):
        userInput = input("Enter row " + str(i + 1) + ": ").split()
        
        row = []
        for entry in userInput:
            row.append(float(entry))
        matrix.append(row)

    fillZeroes(matrix)
    return matrix

def fillZeroes(matrix):
    length = findLongestRow(matrix)
    for row in matrix:
        for i in range(length - len(row)):
            row.append(0.0)


def compressFloats(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            n = matrix[i][j]
            if int(n) == n:
                matrix[i][j] = int(n)

def findLongestRow(matrix):
    n = 0
    for row in matrix:
        if len(row) > n:
            n = len(row)
    return n

def printMatrix(matrix):
    for row in matrix:
        print(row)

main()