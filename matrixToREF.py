#Derek Lee 
#
#converts a matrix to REF form
#1. check to see if matrix is REF
#2. rearrange columns so that they are placed in order of leading entry appearance
#3. determine first column with more than 1 leading entry
#4. collect rows that have a leading entry in that column
#5. multiply first row by leading entry of second row and vice versa so that the leading entries have the same value
#6. add the first row to the second row so that the second row no longer has a leading entry in that column
#7. repeat 5-6 until the first row collected is the only row with a leading entry in that column
#8. repeat from 1 until matrix achieves REF


from matrixRREFcheck import isREF, findLeadingEntry, leadingEntryValue, isZeroRow
from rowoperations import rowAddition, swapRows, rowMultiplication

operationHistory = []

def main():
    pass

def convertToREF(matrix):
    while not isREF(matrix):
        rearrangeRows(matrix)
        column = findFirstConflict(matrix)
        if column == -1:
            pass

        rows = collectWithLeadingEntry(matrix, column)
        while len(rows) > 1:
            eliminateLeading(matrix, rows[0], rows[len(rows) - 1])
            rows.pop()
    return operationHistory




def rearrangeRows(matrix):
    while not isOrdered(matrix):
        for i in range(len(matrix) - 1):
            if isZeroRow(matrix[i]) and isZeroRow(matrix[i+1]):
                pass
            elif (isZeroRow(matrix[i]) and not isZeroRow(matrix[i+1])) or (findLeadingEntry(matrix[i]) > findLeadingEntry(matrix[i + 1])):
                swapRows(matrix, i, i+1)
                operationHistory.append("R" + str(i+1) + ", " + str(i+2))

def isOrdered(matrix):
    zeroPassed = False
    last = 0
    for row in matrix:
        if isZeroRow(row):
            zeroPassed = True
        else:
            if zeroPassed:
                return False
            i = findLeadingEntry(row)
            if i < last:
                return False
            last = i
    return True


def findFirstConflict(matrix):
    leadingPositions = dict()
    for i in range(len(matrix[0])):
        leadingPositions[i] = 0
    for row in matrix:
        if not isZeroRow(row):
            position = findLeadingEntry(row)
            if leadingPositions[position] > 0:
                return position
            leadingPositions[position] = leadingPositions[position] + 1
    return -1

def collectWithLeadingEntry(matrix, column):
    rows = []
    for i in range(len(matrix)):
        if findLeadingEntry(matrix[i]) == column:
            rows.append(i)
    return rows

def eliminateLeading(matrix, i, j):
    iFactor = leadingEntryValue(matrix[i])
    jFactor = leadingEntryValue(matrix[j])

    rowMultiplication(matrix, i, jFactor)
    rowMultiplication(matrix, j, iFactor)
    operationHistory.append("R"+str(i+1)+" (" + str(jFactor) + ")")
    operationHistory.append("R"+str(j+1)+" (" + str(iFactor) + ")")
    mult = 1
    if leadingEntryValue(matrix[i]) == leadingEntryValue(matrix[j]):
        mult = -1
    else:
        mult = 1
    rowAddition(matrix, i, mult, j)
    operationHistory.append("R"+str(i+1)+" (" + str(mult) + ") + R" + str(j+1))


