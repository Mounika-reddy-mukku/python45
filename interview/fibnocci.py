N=int(input())
sum=0
L=[0,1]
for i in range(N-2):
    a=L[i]
    b=L[i+1]
    sum=a+b
    L.append(sum)
print(L)


