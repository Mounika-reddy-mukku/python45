#print first n prime numbers
N=int(input("Enter N:"))
L=[]
i=2
while(len(L)<N):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count+=1
    if(count==0):
        L.append(i)
    i=i+1
print(L)

