N=int(input())
Fib=[0,1]
while(Fib[-1]+Fib[-2]<=N):
    sum=Fib[-1]+Fib[-2]
    Fib.append(sum)
print(Fib)
    