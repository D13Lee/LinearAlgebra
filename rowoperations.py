#Derek Lee  10/1/2019
#functions that allow row operations on a matrix.
#product of row and nonzero scalar plus another row
#row multiplication
#row swapping


#replaces row with new row that has been multiplied by factor
#accepts matrix, index of row, and scalar factor
def rowMultiplication(matrix, row, factor):
    newRow = []
    for n in matrix[row]:
        newRow.append(n*factor)
    matrix[row] = newRow

#swaps the place of two rows in matrix
#accepts matrix and two indexes as parameters
def swapRows(matrix, row1, row2):
    intermediate = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = intermediate

#multiplies a row by a factor (does not replace old values) and adds it to the second row (replaces old values)
#accepts matrix, the index to be added, the factor, and the index to be added to
def rowAddition(matrix, row1, factor, row2):
    newRow = []
    for i in range(len(matrix[row1])):
        newRow.append((matrix[row1][i]*factor) + matrix[row2][i])
    matrix[row2] = newRow

