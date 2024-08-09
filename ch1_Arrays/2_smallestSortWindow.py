#given an array of integers, determine the bounds of the smallest window
#that must be sorted for the entire array to be sorted

unsortedArray2 = [3, 7, 5, 6, 9]
unsortedArray = [1, 9, 6, 8, 2]

#use pop() and insert()
currentLowestIndex = 0
currentHighestIndex = 0

for currentValue in unsortedArray:
    numToBeSorted = currentValue
    indexOfNumToBeSorted = unsortedArray.index(currentValue)

    for currentIndex in range(len(unsortedArray)):
        if numToBeSorted > unsortedArray[currentIndex] and indexOfNumToBeSorted < currentIndex:
            unsortedArray.pop(indexOfNumToBeSorted)
            unsortedArray.append(numToBeSorted)
            
for value in unsortedArray:
    print(value)