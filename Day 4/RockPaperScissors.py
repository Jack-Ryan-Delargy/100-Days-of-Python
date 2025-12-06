import random

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

gameImages = [rock,  paper, scissors]

userChoice = int(input("Please choose 0(rock), 1(paper), or 2(scissors)"))
if userChoice >= 0 and userChoice <=  2:
    print(gameImages[userChoice])

computerChoice = random.randint(0,2)
print(f"Computer chose:")
print(gameImages[computerChoice])

if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number. Game Over")
elif userChoice == 0 and computerChoice == 2:
    print("You win!")
elif userChoice == 2 and computerChoice == 0:
    print("You loose!")
elif userChoice < computerChoice:
    print("You loose!")
elif userChoice > computerChoice:
    print("You win!")
elif userChoice == computerChoice:
    print("Its a tie.")
