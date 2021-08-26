def min_matrix():
    global mat,split
    l=len(mat)
    for i in range(1,l):
        split[i][i] = i
    for d in range(1,l-1):
        for i in range(1,l-d):
            j=i+d 
            min=999999999
            for k in range(i,j):
                val=mat[i][k]+mat[k+1][j]+arr_d[i-1]*arr_d[k]*arr_d[j]
                if(val<min):
                    min=val
                    split[i][j]=k
            
            mat[i][j]=min
    return mat[1][l-1]

def order_mat(split,i,j):
    if(i==j):
        print(chr(64+split[i][j]),end="")
    else:
        print('(',end="")
        order_mat(split,i,split[i][j])
        order_mat(split,split[i][j]+1,j)
        print(')',end="")

n=int(input())
arr_d=list(map(int,input().split()))
print('Given matrices ',end="")
for i in range(len(arr_d)-1):
    print('   ',arr_d[i],'x',arr_d[i+1],end=" ")
mat=[[0 for j in range(n)] for i in range(n)]
split=[[0 for j in range(n)] for i in range(n)]
print('\n_________\nMinimum number of operations(multiplications) required',min_matrix())
print('order of matrices chosen is ',end=" ")
order_mat(split,1,n-1)	
