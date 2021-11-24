def LCS_lenght(x,y):
    c = [[0 for _ in range(len(y))] for _ in range(len(x))]
    m=len(x)
    n=len(y)
    # c=[[]]
    # for i in range(1,m):
    #     lista=[]
    #     c.append(lista)
    #     c[i].append(0)
    # for j in range(0,n):
    #     c[0].append(0)
    print(c)
    for i in range(1,m):
        for j in range(1,n):
            if x[i-1]==x[j-1]:
                c[i][j]=c.append(c[i-1][j-1]+1)
            else:
                if (c[i-1][j])>=(c[i][j-1]):
                    c[i][j]=c.append(c[i-1][j])
                else:
                    c[i][j]=c.append(c[i][j-1])
    return c

x=(1,0,0,1,0,1,0,1)
y=(0,1,0,1,1,0,1,1,0)

print(LCS_lenght(x,y))

