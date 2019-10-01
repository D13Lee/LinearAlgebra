
#Derek Lee 9/30/2019
#main() prompts user input to construct a matrix. The program then detects if the constructed matrix fits the conditions of REF and RREF
#these conditions are
#1. all non zero rows are above every zero row
#2. the leading entry of every consecutive row appears farther to the right than the last leading entry
#3. every leading entry is 1
#4. all values above a leading entry is 0
#
#input is taken row by row when constructing the matrix.
#if the rows have inequal number of entries, 0's are filled to accomodate the empty spaces on the rightmost side.
#     1                1 0 0
# ex  0 1   constructs 0 1 0
#     0 0 1            0 0 1

def main():
    matrix = userConstructMatrix()
    RREF = isRREF(matrix)
    REF = False
    if not RREF:
        REF = isREF(matrix)
    compressFloats(matrix)
    printMatrix(matrix)
    if not RREF:
        print("is" + (" REF but not RREF" if REF else " not REF or RREF"))
    else:
        print("is REF and RREF")

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

def findLongestRow(matrix):
    n = 0
    for row in matrix:
        if len(row) > n:
            n = len(row)
    return n

def isRREF(matrix):
    if condition1(matrix):
        if condition2(matrix):
            if condition3(matrix):
                return condition4(matrix)
    return False

def isREF(matrix):
    if condition1(matrix):
        return condition2(matrix)

def compressFloats(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            n = matrix[i][j]
            if int(n) == n:
                matrix[i][j] = int(n)
    

def printMatrix(matrix):
    for row in matrix:
        print(row)

#check if all nonzero rows are above every zero row
def condition1(matrix):
    rows = []
    for row in matrix:
        rows.append(isZeroRow(row))

    zeroPassed = False
    for state in rows:
        if state and not zeroPassed:
            zeroPassed = True
        if state and zeroPassed:
            return False
    return True

#check that for any consecutive nonzero rows, the leading entry occurs further to the right than the one above
def condition2(matrix):
    rows = []
    for row in matrix:
        rows.append(findLeadingEntry(row))
    previous = False
    for i in range(len(rows)):
        if rows[i] == -1:
            previous = False
            #if there is a nonzero row before this one, compare positions of their leading entries
        elif previous and not rows[i] == -1:
            if rows[i-1] >= rows[i]:
                return False
        if not rows[i] == -1:
            previous = True
    return True



#check that each leading entry is 1
def condition3(matrix):
    rows = []
    for row in matrix:
        rows.append((findLeadingEntry(row),leadingEntryValue(row)))
    for data in rows:
        if data[0] == -1:
            continue
        elif not data[1] == 1:
            return False
    return True

#check that every entry above a leading entry is 0
def condition4(matrix):
    if len(matrix) < 2:
        return True
    leadingEntries = []
    #store the locations of each leading entry
    for row in matrix:
        leadingEntries.append(findLeadingEntry(row))
    #skip the first entry, which is true by default
    for i in range(1, len(leadingEntries)):
        #check all values above the position in the column given by leadingEntries[i]
        for l in range(0, i):
            if not matrix[l][leadingEntries[i]] == 0:
                return False

    return True

#returns the index of the first nonzero value
def findLeadingEntry(row):
    i = 0
    for n in row:
        if not n == 0:
            return i
        i = i + 1
    return -1

#returns the value of the first non zero value
def leadingEntryValue(row):
    for n in row:
        if not n == 0:
            return n
    return 0

#returns True if all elements are 0
def isZeroRow(row):
    for n in row:
        if not n == 0:
            return False
    return True


A = []
a1 = [1, 0, 0]
a2 = [0, 1, 0]
a3 = [0, 0, 1]
A = [a1, a2, a3]

B = []
b1 = [0, 0, 0, 0]
b2 = [0, 1, 2, 0]
b3 = [0, 1, 0, 0]
b4 = [2, 1, 0, 0]
B = [b1, b2, b3, b4]

C = []
c1 = [0, 0, 0]
c2 = [0, 0, 0]
c3 = [0, 0, 0]
C = [c1, c2, c3]

#main(A)
#main(B)
#main(C)
main()