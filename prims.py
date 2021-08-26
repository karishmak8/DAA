n=int(input("enter no:of items:"))
lst=[]
for i in range(0,n):
    A=[]
    value=int(input("enter the value:"))
    A.append(value)
    weight=int(input("enter the weight:"))
    A.append(weight)
    lst.append(A)
kc=int(input("enter knapsack capacity:"))
r=[]
for i in range(0,n):
    A=[]
    ratio=lst[i][0]/lst[i][1]
    A.append(ratio)
    r.append(A)
lst1=[x for _, x in sorted(zip(r,lst),reverse=True)]
tw=0
tv=0
for i in range(0,n):
    tw=tw+lst1[i][1]
    if(tw<=kc):
        tv=tv+lst1[i][0]
        tw1=tw
    else:
        break
if(tw1!=kc):
    tv=tv+((kc-tw1)*lst1[i][0]/lst1[i][1])
print("maximum total value in knapsack:",tv)
