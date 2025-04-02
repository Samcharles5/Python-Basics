import random

print("LET'S PLAY ROCK PAPER SCISSOR\n")

user_choice=int(input("Enter Your choice 0-Rock 1-Paper 2-Scissor : "))
com_choice=random.randint(0,2)

if user_choice>2:
    print("Invalid Input")
    exit()

if user_choice==2 and com_choice==0:
    print(f"computer chooce '{com_choice}' You LOSS")
elif user_choice==0 and com_choice==2:
    print(f"computer chooce '{com_choice}' You WIN")
elif user_choice>com_choice:
    print(f"computer chooce '{com_choice}' You WIN")
elif user_choice<com_choice:
    print(f"computer chooce '{com_choice}' You LOSS")
elif user_choice==com_choice:
    print(f"computer chooce '{com_choice}' DRAW")
else:
    print("Invalid Input")
