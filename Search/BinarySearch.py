def binarySearch(inputList, target):
	low = 0
	high = len(inputList)-1
	while low <= high:
		mid = (high-low)/2
		if inputList[mid] > target:
			high = mid - 1
		elif inputList[mid] < target:
			low = mid + 1
		else:
			return mid

	return -1
	 