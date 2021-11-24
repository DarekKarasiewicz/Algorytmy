import time
import random

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
        QucikSort(A,p,q-1,)
        QucikSort(A,q+1,r)





def Insert_Sort(A):
    start=time.time()
    for j in range(1,(len(A))):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    end = time.time() - start
    print(str(end.real) + "s")


def find_min_index(lst, start):
    i = start
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[i]:
            i = j
    return i


def selection_sort(lst):
    start_time = time.time()
    for i in range(len(lst)):
        min_idx = find_min_index(lst, i)
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    end = time.time() - start_time
    print(str(end.real) + "s")
    return lst

A=[]
i=0;
while i<10000:
    n=random.randint(1,100)
    A.append(n)
    i+=1

# for v in A:
#     print(v,end=" ")

# print(" ")
# print("Partition")
# partition(A,0,10)
# # for v in A:
# #     print(v,end=" ")
print(" ")
print("QuickSorted")

QucikSort(A,0,A[-1])
# for v in A:
#     print(v,end=" ")

print(" ")
print("Insertion-Sort")
A=[]
i=0;
while i<10000:
    n=random.randint(1,100)
    A.append(n)
    i+=1
Insert_Sort(A)
# for v in A:
#     print(v,end=" ")

print(" ")
print("Sort by choice")
A=[]
i=0;
while i<10000:
    n=random.randint(1,100)
    A.append(n)
    i+=1
selection_sort(A)

