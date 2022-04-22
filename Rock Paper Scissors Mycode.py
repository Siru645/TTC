import random
action = ["Rock", "Paper", "Scissors"]
computer_action = random.choice(action)
human_action = input("Enter your action (Rock, Paper, Scissors): ")
if human_action == computer_action:
  print("It's a tie.")
elif human_action == "Rock":
  if computer_action == "Paper":
    print("The computer plays Paper. You lose.")
elif human_action == "Rock":
  if computer_action == "Scissors":
    print("The computer plays Scissors. You win!")
elif human_action == "Paper":
  if computer_action == "Rock":
    print("The computer plays Rock. You win!")
elif human_action == "Paper":
  if computer_action == "Scissors":
    print("The computer plays Scissors. You lose.")
elif human_action == "Scissors":
  if computer_action == "Paper":
    print("The computer plays Paper. You win!")
  else: print("The computer plays Rock. You lose.")