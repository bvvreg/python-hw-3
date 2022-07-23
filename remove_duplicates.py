def remove_duplicates(array):
    arrayFinish = []
    prevElement = array[0]
    arrayFinish.append(array[0])

    for element in array:
        if element != prevElement:
            arrayFinish.append(element)
        prevElement = element
      
    return(arrayFinish)


print (remove_duplicates([1,1,2]))
print (remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
print (remove_duplicates([1,1,1,1,1,1,1,1]))