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
---'   ____)____
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

#Write your code below this line 👇
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
print("You chose:")
if choice == "0":
  print(rock)
elif choice == "1":
  print(paper)
else:
  print(scissors)
import random
aichoice = random.randint(0,2)
if aichoice == 0:
  if choice == "0":
    print("Computer chose:")
    print(rock)
    print("It's a draw.")
  elif choice == "1":
    print("Computer chose:")
    print(rock)
    print("You Win.")
  else:
    print("Computer chose:")
    print(rock)
    print("You Lose.")
elif aichoice == 1:
  if choice == "0":
    print("Computer chose:")
    print(paper)
    print("You lose.")
  elif choice == "1":
    print("Computer chose:")
    print(paper)
    print("It's a draw.")
  else:
    print("Computer chose:")
    print(paper)
    print("You Win.")
else:
  if choice == "0":
    print("Computer chose:")
    print(scissors)
    print("You win.")
  elif choice == "1":
    print("Computer chose:")
    print(scissors)
    print("You lose.")
  else:
    print("Computer chose:")
    print(scissors)
    print("It's a draw.")