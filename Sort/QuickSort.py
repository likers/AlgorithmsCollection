def quickSort(inputList):
	quickSortHelper(inputList, 0, len(inputList)-1)

def quickSortHelper(inputList, first, last):
	if first < last:
		splitPoint = partition(inputList, first, last)

		quickSortHelper(inputList, first, splitPoint-1)
		quickSortHelper(inputList, splitPoint+1, last)

def partition(inputList, first, last):
	pivotValue = inputList[first]

	leftMark = first + 1
	rightMark = last

	done = False
	while not done:
		while leftMark <= rightMark and inputList[leftMark] <= pivotValue:
			leftMark = leftMark + 1

		while inputList[rightMark] >= pivotValue and rightMark >= leftMark:
			rightMark = rightMark - 1

		if rightMark < leftMark:
			done = True
		else:
			temp = inputList[leftMark]
			inputList[leftMark] = inputList[rightMark]
			inputList[rightMark] = temp

	temp = inputList[first]
	inputList[first] = inputList[rightMark]
	inputList[rightMark] = temp

	return rightMark

inputList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(inputList)
print inputList