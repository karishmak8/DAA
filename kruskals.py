import collections


result=[]
sets=[]
edges=[]
v=int(input("enter no.of vertices "))
e=int(input("enter no.of edges "))
edges=dict()
for k in range(e):
    edges[tuple(int(input('enter vertex ')) for i in range(2))]=int(input("enter the weight of the edges "))
for i in range(v):
    sets.append([i])
edges=dict(sorted(edges.items(),key=lambda item:item[1]))

def find_set(x):
    for i in range(len(sets)):
            if x in sets[i]:
                return i
for u,v in edges.keys():
    x=find_set(u)
    y=find_set(v)
    if(x!=y):
        result.append((u,v))
        sets[x]+=sets[y] 
        sets.pop(y) 
cost=0
print("edge : weight")
for i in result:
    print(i,edges[i])
    cost+=edges[i]
print("total cost of minimum spanning tree : ",cost )
