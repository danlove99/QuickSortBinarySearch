def partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] <= pivot:
		    i = i + 1
		    arr[j], arr[i] = arr[i], arr[j]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return(i+1)

def quicksort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		quicksort(arr,low, pi-1)
		quicksort(arr,pi+1,high)
	return arr
	

def binsearch(arr, target):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = (low + high) // 2
		if target == arr[mid]:
			return True
		elif target > arr[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return False
	
	
arr = [2,4,65,7,33,21,45,6]
quicksort(arr, 0, len(arr) - 1)
binsearch(arr, 4)
                