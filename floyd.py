INF=999
graph=[]
v=int(input("enter no.of vertices "))
graph=[[0 for i in range(v)]for i in range(v)]
e=int(input("enter no.of edges "))
for k in range(e):
  v1,v2=int(input("enter vertex1:")),int(input("enter vertex2:"))
  graph[v1][v2]=int(input("enter the weight of the edges "))
for i in range(v):
    for j in range(e):
        if(i==j or graph[i][j]!=0):
            continue;
        else:
            graph[i][j]=INF
print("graph =",graph)
v=len(graph)
dist=graph.copy()
for k in range(v):
    for i in range(v):
        for j in range(v):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
for i in range(v):
    for j in range(v):
        if(dist[i][j]==INF):
            print("%7s"%("INF"),end=" ")
        else:
            print("%7d"%(dist[i][j]),end=" ")
    print("")
