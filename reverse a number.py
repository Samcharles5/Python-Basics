num=int(input('Enter a number to reverse:' ))
temp = num
rev=0
while num>0:
    remainder=num%10
    rev=rev*10+remainder
    num =num//10
print(f'given no: {temp} reversed no: {rev}')

# num = 56
# reversed_num = 0
#
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
#
# print("Reversed Number: " + str(reversed_num))