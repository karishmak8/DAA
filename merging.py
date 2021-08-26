a=list()
n1=int(input("enter number of elements in the list1: "))
n2=int(input("enter number of elements in the list2: "))
print("enter two sorted lists")
b=[int(input()) for i in range(n1)]
c=[int(input()) for i in range(n2)]
i = j = k = 0
while i < n1 and j < n2:
    if b[i] < c[j]:
        a.insert(k ,b[i])
        i= i+ 1
    else:
        a.insert(k,c[j])
        j += 1
    k += 1
while i < n1:
	a.insert(k ,b[i])
	i += 1
	k += 1
while j < n2:
	a.insert(k,c[j])
	j += 1
	k += 1
print(a)
