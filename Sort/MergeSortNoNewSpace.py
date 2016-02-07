def mergeSortInLine(inputList):
	if len(inputList) > 1:
		mid = len(inputList)/2
		leftList = inputList[:mid]
		rightList = inputList[mid:]

		mergeSortInLine(leftList)
		mergeSortInLine(rightList)

		i = j = k = 0

		while i < len(leftList) and j < len(rightList):
			if leftList[i] < rightList[j]:
				inputList[k] = leftList[i]
				i += 1
			else:
				inputList[k] = rightList[j]
				j += 1
			k += 1

		while i < len(leftList):
			inputList[k] = leftList[i]
			i += 1
			k += 1
		while j < len(rightList):
			inputList[k] = rightList[j]
			j += 1
			k += 1

a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSortInLine(a)
print a