A=[123,432,543,654,765,756,323,523,423]
B=[0,0,0,0,0,0,0,0,0,0]
C=[0,0,0,0,0,0,0,0,0,0]
def Counting_Sort(A,B,k):
    lenght_A=len(A)-1
    for i in range(0,k):
        C[i]=0
    for j in range(0,lenght_A):
        number_to_string=str(A[j])
        number=int(number_to_string[2])
        C[number] = C[number]+1
    for i in range(1,k):
        C[i]=C[i]+C[i-1]
    for j in range(0,lenght_A):
        number_to_string = str(A[j])
        number = int(number_to_string[2])
        B[C[number]+1]=A[j]
        C[number]=C[number]-1

def Radix_Sort(A,d):
    for i in range(1,d):
        A.sort()



def sortuj_wstaw(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b

def Bucket_Sort(A):
    B=[]
    slot_num = 10

    for i in range(slot_num):
        B.append([])
    for j in A:
        index_b=int(slot_num * j)
        B[index_b].append(j)
    for i in range(slot_num):
        B[i]=sortuj_wstaw(B[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    return B

#26<-ilość literek w alfabecie
Counting_Sort(A,B,10)
#3 <-ilość pozycji do przesortowania
Radix_Sort(A,3)
print(A)
A= [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print(Bucket_Sort(A))
