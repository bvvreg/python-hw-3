def spiral(matrix):

    endRow = len(matrix)
    startRow = 0

    endColumn = len(matrix[0])
    startColumn = 0
    arrayFinish = []
  
    while (startRow < endRow and startColumn < endColumn):
  
        # додаєм перший рядок 
        for i in range(startColumn, endColumn):
            arrayFinish.append(matrix[startRow][i])
  
        startRow += 1
  
        # додаєм останній стовпець
        for i in range(startRow, endRow ):
            arrayFinish.append(matrix[i][endColumn - 1])
  
        endColumn -= 1
  
        # додаємо останній рядок у зворотньому напрямку
        if (startRow < endRow ):
  
            for i in range(endColumn - 1, (startColumn - 1), -1):
                arrayFinish.append(matrix[endRow - 1][i])
  
            endRow -= 1
  
        # додаємо перший стовпець  у зворотньому напрямку
        if (startColumn < endColumn):
            for i in range(endRow - 1, startRow - 1, -1):
                arrayFinish.append(matrix[i][startColumn])
  
            startColumn += 1

    return arrayFinish
  
print (spiral([[1,2,3],
               [4,5,6],
               [7,8,9]]))

print (spiral([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9,10,11,12]]))

print (spiral([[1,  2, 3, 4, 5, 6],
               [7,  8, 9,10,11,12],
               [13,14,15,16,17,18],
               [19,20,21,22,23,24],
               [25,26,27,28,29,30]]))