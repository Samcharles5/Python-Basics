str=input('enter a string :')
fre={}
for i in str:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1

for key, value in fre.items():
    print(f'{key} appear {value} times')


