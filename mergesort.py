def mergeSort(A):
	if len(A)>1:
		mid=int(len(A)/2)
		L=A[:mid] #dividing array into two halves
		R=A[mid:]
		#print(L)
		#print(R)
		mergeSort(L)
		mergeSort(R)
		mergePro(A,L,R)
def mergePro(A,L,R):
	i = j = k = 0
	
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		k += 1
		# Checking if any element was left
	while i < len(L):
		A[k] = L[i]
		i += 1
		k += 1
	while j < len(R):
		A[k] = R[j]
		j += 1
		k += 1	
