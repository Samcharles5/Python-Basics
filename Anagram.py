str1=input('Enter first string: ')
str2=input('Enter second string: ')

if sorted(str1)==sorted(str2):
    print('\nit is anagram')
else:
    print('\nnot anagram')