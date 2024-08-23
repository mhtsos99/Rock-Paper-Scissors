rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random 
response = random.randint(0,2)

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) 

print("The computer chosed: ") 
if response == 0:
  print(rock) 
elif response == 1: 
  print(paper) 
else: 
  print(scissors) 
  
print("You chose: ")
if choice == 0:
  print(rock) 
elif choice == 1: 
  print(paper) 
else: 
  print(scissors) 


if choice == response: 
  print("It is a draw") 
elif choice == 0 and response == 1:
  print("Yoy lose")   
elif choice == 0 and response == 2: 
  print("You win") 
elif choice == 1 and response == 0: 
  print("You win") 
elif choice == 1 and response == 2:
  print("You lose") 
elif choice == 2 and response == 0:
  print("You lose") 
elif choice == 2 and response == 1: 
  print("you win") 
else: 
  print("Yoy typed an invalid number, try again") 
