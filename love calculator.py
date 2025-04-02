name1=input("Enter your Name :")
name2=input("Enter your Love's Name :")
name1=name1.lower()
name2=name2.lower()
name3= name1+name2
total=0
total +=name3.count('t')
total +=name3.count('r')
total +=name3.count('u')
total +=name3.count('e')
total1=0
total1 +=name3.count('l')
total1 +=name3.count('o')
total1 +=name3.count('v')
total1 +=name3.count('e')

final= str(total)+str(total1)

print(f"Your Love score is {final}")
