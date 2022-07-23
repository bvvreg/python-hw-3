def double_zero(array):
    arrayFinish = []
    for element in array:
        arrayFinish.append(element)
        if element == 0:
            arrayFinish.append(0)
      
    return arrayFinish


print (double_zero([1,0,2,3,0,4,5,0]))
print (double_zero([1,0,0,2,3,0,4,5,0]))
print (double_zero([1,2,3]))