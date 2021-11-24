def h1(k,m):
    index=k % m
    return index

def h2(k,m):
    index=1+(k%(m-1))
    return index

def h(k,m,A):
    for n in k:
        i=0
        while(n not in A):
            index=(h1(n,m)+i) % m
            if A[index] is None:
                A[index]=n
            else:
                i+=1
    return A





k=[10,22,31,4,15,28,17,88,59]
m=11
A=[]
for i in range(m):
    A.append(None)

h(k,m,A)
print(A)
