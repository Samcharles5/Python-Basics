n=int(input('enter a number: '))
n1,n2=0,1
print(f'Fibonacci series: {n1}{n2}', end="")
for i in range(2,n):
    n3=n2+n1
    n1,n2=n2,n3
    print(n3,end="")