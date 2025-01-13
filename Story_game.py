import time
import random

def get_user_input():
  while True:
      try:
          n = input("Please put your choice: ")
          if n == "Rock" or n == "Paper" or n == "Scissors":
              break
      except:
          print("Invalid imput")
  return n

def gamecheck(Name, computer_choice):
  if (Name == "Rock") and (computer_choice == "Paper"):
    print("U lose!")
    print("A ghost appear behind U as U get slashed from the back and die from bleeding. The End.")
    return False
  elif (Name == "Rock") and (computer_choice == "Rock"):
    print("Try again.")
    return True
  elif (Name == "Rock") and (computer_choice == "Scissors"):
    print("U win.")
    print("The door to the outside world opens as you are released from the grasps of the monsters in this house. You take your leave as the story comes to an abrupt end.")
    return False
  elif (Name == "Paper") and (computer_choice == "Paper"):
    print("Try again.")
    return True
  elif (Name == "Paper") and (computer_choice == "Rock"):
    print("U win.")
    print("The door to the outside world opens as you are released from the grasps of the monsters in this house. You take your leave as the story comes to an abrupt end.")
    return False
  elif (Name == "Paper") and (computer_choice == "Scissors"):
    print("U lose!")
    print("A ghost appear behind U as U get slashed from the back and die from bleeding. The End.")
    return False
  elif (Name == "Scissors") and (computer_choice == "Scissors"):
    print("Try again.")
    return True
  elif (Name == "Scissors") and (computer_choice == "Paper"):
    print("U win.")
    print("The door to the outside world opens as you are released from the grasps of the monsters in this house. You take your leave as the story comes to an abrupt end.")
    return False
  elif (Name == "Scissors") and (computer_choice == "Rock"):
    print("U lose!")
    print("A ghost appear behind U as U get slashed from the back and die from bleeding. The End.")
    return False

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentplayer = "X"
winner = None
gamerunning = True

# Printing the gameboard
def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

#  Take player input
def playerinput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("Oops this spot is already taken.")

# Check for win or tie
def checkhorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True #Return gives the output of the function(Something like a result)
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
# Check row for win or tie
def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True #Return gives the output of the function(Something like a result)
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# Check for diagonal for win or tie
def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True #Return gives the output of the function(Something like a result)
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# Check if tie
def checktie(board):
    global gamerunning
    if "-"not in board:
        printboard(board)
        print("Its a tie! YOU DIE!")
        gamerunning = False

# Check for win
def checkwin():
    global gamerunning
    if checkdiagonal(board) or checkhorizontle(board) or checkrow(board):
        print(f"The winner is {winner}. Your free to go home. The End.")
        gamerunning = False

# Switch player
def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

time.sleep(1)
print("Welcome to my Ninja Game!")
time.sleep(1)
print("U are summoned into the Ninja World where u find urself alone in front of a door to a Mansion.")
time.sleep(1)
Choose = input("Enter or don't enter? ")
Room = {

  'L':"Living room",
  'B':"Bedroom",
  'K':"Kitchen",
  'T':"Toilet"

}

hi = True

time.sleep(1)
#() ==> set
#[] ==> Lists
#{} ==> Dictionary
while hi == True:
  if Choose == "Enter":
    time.sleep(1)
    print("You find yourself in an empty and dusty " + Room['L'] + "...")
    hi = False

  elif Choose == "Dont enter":
    time.sleep(1)
    print("You return to the world of mortals and never to return, saving u ample time and trauma. Good choice!")
    hi = False

  else:
    print("Invalid input, try again.")
    Choose = input()

time.sleep(1)
print("You see a big touch screen tv on a wall that says 'Press the screen to play Rock paper scissors, you will be allowed to escape if you win'")
time.sleep(1)
print("Do you play the game? Yes or No?")

decide = input(">")
trf = True

# ///////////////////////////////////////////////
computer_choice_index = random.randint(0,2)
computer_choices = ["Rock", "Paper", "Scissors"]
computer_choice = computer_choices[computer_choice_index]
# //////////////////////////////////////////////

while trf:
  if decide == "Yes":
    time.sleep(1)
    print("'Rock, paper, scissors, winner starts first'")
    Name = get_user_input()
    print("I choose " + Name + ".")
    print("The tv chose " + computer_choice + ".")
    trf = gamecheck(Name, computer_choice)

  elif decide == "No":
    trf = False
    time.sleep(1)
    print("You refuse and decide to enter the " + Room["K"])
    time.sleep(1)
    print("U see a tictactoe game drawn on a whiteboard, above the diagram it says 'Do you want to play with me? You can start first...'")
    time.sleep(1)
    print("You realised u are forced to play as ur legs are suddenly tied to the ground.")
    time.sleep(1)
    # While game is running
    while gamerunning:
        printboard(board)
        playerinput(board)
        checkwin()
        checktie(board)
        switchplayer()

  else:
    time.sleep(1)
    print("Invalid input, try again")
    decide = input()

# elif decide == "No":
#   print("You decide to decline and you enter the "+ Room["B"] +"...")
# else:
#   while decide != "Yes" or "No":
#     print("Invalid input.")
#     decide = input(">")
    



