# no divisible by 3 replaced by Fizz
# no divisible by 5 replaced by Buzz
# no divisible by 3 and 5 replaced by FizzBuzz

n=int(input("enter the sequence END number: "))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
else:
    print("Loop completed")