import time
import random
arr=[]
i=0
while i<10000:
    n=random.randint(1,100)
    arr.append(n)
    i+=1

def max_heapify(arr, i, lenght):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left <= lenght and arr[largest] < arr[left]:
        largest = left

    if right <= lenght and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, lenght)


def build_max_hep(arr):
    lenght = len(arr)
    for i in range(((lenght - 1) // 2), -1, -1):
        max_heapify(arr, i, lenght - 1)


def heapsort(arr):
    build_max_hep(arr)
    lenght = len(arr)
    for i in range(lenght - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        lenght = lenght - 1
        max_heapify(arr, 0, lenght - 1)
    end=time.time()-start




# print("heap ")
# for v in range(len(arr)):
#     print(arr[v], end=' ')
start=time.time().real
heapsort(arr)


arr.reverse()
end=time.time().real-start
print(end)
# print("Sorted heap ")
# for v in range(len(arr)):
#     print(arr[v], end=' ')
