def binarySearch(list, int):
	for i in range( 0, len(list), 1) :
		if list[i] == int:
			return i
	return -1

print(binarySearch([4,8,15,16,23,42], 15))

