num1=int(input('enter first number'))
num2=int(input('enter Second number'))

def gcd(num1,num2):
    if num1>num2:
        small=num2
    else:
        small=num1
    for i in range(1,small+1):
        if num1%i==0 and num2%i==0:
            gcd=i
    return gcd
print(gcd(num1,num2))