import time
import random
start=time.time().real
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,(r-1)+1):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1


def QucikSort(A,p,r):
    if p<r:
        q=partition(A, p, r)
        QucikSort(A,p,q-1)
        QucikSort(A,q+1,r)



A=[]
i=0;
while i<10000:
    n=random.randint(1,100)
    A.append(n)
    i+=1


print(" ")
print("QuickSorted")

QucikSort(A,0,A[-1])
A.reverse()
end=time.time()-start
print(end.real)