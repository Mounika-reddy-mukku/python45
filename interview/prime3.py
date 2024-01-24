N=int(input("Enter the number:"))
primeNumbers=[]
for i in range(2,N):
    count=0
    if(i==2):
        primeNumbers.append(i)
        continue
    for j in range(2,i):
        if(i%j==0):
            count+=1
    if(count==0):
        primeNumbers.append(i)
print(primeNumbers)