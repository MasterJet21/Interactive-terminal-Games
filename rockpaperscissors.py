import random

Choose = "Rock, Paper, Scissors"
print(Choose)
Name = input(Choose)
print("I choose " + Name)

# ///////////////////////////////////////////////
computer_choice_index = random.randint(0,2)
computer_choices = ["Rock", "Paper", "Scissors"]
computer_choice = computer_choices[computer_choice_index]
# //////////////////////////////////////////////

if (Name == "Rock") and (computer_choice == "Paper"):
    print(computer_choice)
    print("Loser L")
elif (Name == "Rock") and (computer_choice == "Rock"):
    print("Draw")
elif (Name == "Rock") and (computer_choice == "Scissors"):
    print("U win")
elif (Name == "Paper") and (computer_choice == "Paper"):
    print(computer_choice)
    print("Draw")
elif (Name == "Paper") and (computer_choice == "Rock"):
    print(computer_choice)
    print("U win")
elif (Name == "Paper") and (computer_choice == "Scissors"):
    print(computer_choice)
    print("Loser L")
elif (Name == "Scissors") and (computer_choice == "Scissors"):
    print(computer_choice)
    print("Draw")
elif (Name == "Scissors") and (computer_choice == "Paper"):
    print(computer_choice)
    print("U win")
elif (Name == "Scissors") and (computer_choice == "Rock"):
    print(computer_choice)
    print("Loser L")