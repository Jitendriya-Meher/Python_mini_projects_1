# 0 for rock
# 1 for paper
# 2 for scissor

# rock wins against scissor
# scissor wins against paper
# paper wins against rock

import random

def rps(inp):
    if(inp==0):
        return "( Rock )"
    elif(inp==1):
        return "( Paper )"
    elif(inp==2):
        return "( Scissor )"
    else:
        return "Enter a valid number? It will be modified? "

print('''
0 for rock
1 for paper
2 for scissor
''')

user_choice = int(input("Your Choice : "))
if( user_choice > 2):
    print("Enter a valid number ? It will be modified ?")
user_choice = user_choice % 3

print("\nYour Choice : ",user_choice,rps(user_choice))

computer_choice = random.randint(0,2)
print("Computer choice :", computer_choice, end=" ")
print(rps(computer_choice))

print()
if( computer_choice == user_choice):
    print("It's a Draw.")
elif( computer_choice == 0 and user_choice == 2):
    print("You Lose.")
elif( computer_choice == 2 and user_choice == 0):
    print("You Win.")
elif( computer_choice > user_choice):
    print("You Lose.")
elif( computer_choice < user_choice):
    print("You Win.")
print()