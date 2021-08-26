def heapify(arr,n,i):
	max=i
	l=2*i+1
	r=2*i+2
	if(l<n and arr[max]<arr[l]):
		max=l
	if(r<n and arr[max]<arr[r]):
		max=r
	if max!=i:
		arr[i],arr[max]=arr[max],arr[i]
		heapify(arr,n,max)
def heap(array):
	n=len(array)
	for i in range(n//2-1,-1,-1):
		heapify(array,n,i)
	for i in range(n-1,0,-1):
		array[i],array[0]=array[0],array[i]
		heapify(array,i,0)


n=int(input("enter no:of elements:"))
array=[]
print("enter elements")
for i in range(0,n):
	ele=int(input())
	array.append(ele)
print("original array:",array)
heap(array)
print("sorted array:",array)	
	
