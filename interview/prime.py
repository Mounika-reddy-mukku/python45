#Find the given number is prime num or not
N=int(input("Enter the number:"))
count=0
for i in range(2,N):
    if(N%i==0):
        count+=1
if(count>1):
    print("Not a prime number")
else:
    print("prime number")