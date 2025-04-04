import random
import string

# List of lowercase and uppercase letters
letters = list(string.ascii_letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# List of digits
numbers = list(string.digits)  # '0123456789'
# List of common symbols
symbols = list(string.punctuation)

nletter=int(input("Enter no of Letters: "))
nnumbers=int(input("Enter no of Numbers: "))
nsymblos=int(input("Enter no of Symblos: "))

password_list=[]

for i in range(nletter):
    temp=random.choice(letters)
    password_list+=temp
for i in range(nnumbers):
    temp=random.choice(numbers)
    password_list+=temp
for i in range(nsymblos):
    temp=random.choice(symbols)
    password_list+=temp

random.shuffle(password_list)

password=""

for char in password_list:
    password+=char

print(password)
