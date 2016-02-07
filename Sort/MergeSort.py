def mergeSort(inputList):
	
	if len(inputList) > 1:
		result = []
		mid = len(inputList)/2
		leftList = inputList[:mid]
		rightList = inputList[mid:]

		leftResult = mergeSort(leftList)
		rightResult = mergeSort(rightList)

		i = j = k = 0

		while i < len(leftResult) and j < len(rightResult):
			if leftResult[i] < rightResult[j]:
				result.append(leftResult[i])
				i = i + 1
			else:
				result.append(rightResult[j])
				j = j + 1
			k = k + 1

		if i < len(leftResult):
			result = result + leftResult[i:]
		if j < len(rightResult):
			result = result + rightResult[j:]
		print result
		return result
	else:
		return inputList


a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(a)


