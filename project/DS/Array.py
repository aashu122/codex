"""import numpy as np
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
"""
'''
from geo import Geopoint
tokyo = Geopoint(latitude = 35.7, longitude = 139.7)
tokyo.get_time()
'''
import numpy as np
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
"""newTwoDArray = np.insert(twoDArray, 0,[1,2,3,4], axis = 0) #0 represent position in row or column
# axis represent row or column if 0 then add value in row and if 1 add value in column
print(newTwoDArray)"""
#access Elements from the twoDArray
'''def accessElements(array,rowindex,colIndex):
    if rowindex>=len(array) or colIndex>=len(array):
        print("Incorrect index")
    else:
        print(array[rowindex][colIndex])
accessElements(twoDArray,1,3)
'''
#traversing 2D array

'''def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j])
traverseTDArray(twoDArray)
'''
# Searching Elements In 2D array
"""def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == value:
                return "The value is located at index " + str(i) +" "+ str(j)
    return "The Element is not found"
print(searchTDArray(twoDArray,19))
"""
newTDArray = np.delete(twoDArray, 0, axis = 0)
print(newTDArray)
