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

import random


inp_player = input("What do you choose? '0' for rock, '1' for paper or '2' for scissors. ")

if inp_player == "0":
  print(rock)
if inp_player == "1":
  print(paper)
if inp_player == "2":
  print(scissors)

print("Computer Choose: ")
computer = random.randint(0, 2)
if computer == 0:
  print(rock)
if computer == 1:
  print(paper)
if computer == 2:
  print(scissors)

if inp_player == "0" and computer == 1:
  print("You Lose")
elif inp_player == "0" and computer == 0:
  print("Draw")
elif inp_player == "0" and computer == 2:
  print("You Win!")

if inp_player == "1" and computer == 2:
  print("You Lose")
elif inp_player == "1" and computer == 1:
  print("Draw")
elif inp_player == "1" and computer == 0:
  print("You Win!")

if inp_player == "2" and computer == 0:
  print("You Lose")
elif inp_player == "2" and computer == 2:
  print("Draw")
elif inp_player == "2" and computer == 1:
  print("You Win!")