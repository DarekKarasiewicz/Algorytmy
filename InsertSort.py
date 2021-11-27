import time
import random


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


print(" ")
print("Insertion-Sort")
A=[]
i=0;
while i<10000:
    n=random.randint(1,100)
    A.append(n)
    i+=1
Insert_Sort(A)
A.reverse()
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
A.reverse()

