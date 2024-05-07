#This is  test text for readability

#Given an array of integers, return an array that contains the product
#of all ints except for the value of i

initialArray1 = [1,2,3,4,5]
initialArray2 = [3,2,1]

solutionArray = [0]*10

for currentIndex in range(len(initialArray2)):
    indexProduct = 1
    for value in initialArray2:
        indexProduct*=value

    solutionArray[currentIndex] = indexProduct/initialArray2[currentIndex]
    print(solutionArray[currentIndex])

