import random

def get_user_input():
    while True:
        try:
            n = input("Please guess a letter: ").upper()
            if len(n) == 1 and ord(n) > 64 and ord(n) < 91:
                break
        except:
            print("Please type in a single alphabet!")
    return n

def check_pic(i):
    if i == 1:
        print("  _______ \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "__|__\n")
    elif i == 2:
        print("  _______ \n"
        "  |   |    \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "__|__\n")

    elif i == 3:
        print("  _______ \n"
        "  |   |    \n"
        "  |   o    \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "__|__\n")

    elif i == 4:
        print("  _______ \n"
        "  |   |    \n"
        "  |   o    \n"
        "  |   |    \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "__|__\n")

    elif i == 5:
        print("  _______ \n"
        "  |   |    \n"
        "  |   o    \n"
        "  |  \|    \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "__|__\n")

    elif i == 6:
        print("  _______ \n"
        "  |   |    \n"
        "  |   o    \n"
        "  |  \|/   \n"
        "  |        \n"
        "  |        \n"
        "  |        \n"
        "__|__\n")

    elif i == 7:
        print("  _______ \n"
        "  |   |    \n"
        "  |   o    \n"
        "  |  \|/   \n"
        "  |  /     \n"
        "  |        \n"
        "  |        \n"
        "__|__\n")

    elif i == 8:
        print("  _______ \n"
        "  |   |    \n"
        "  |   o    \n"
        "  |  \|/   \n"
        "  |   /\   \n"
        "  |        \n"
        "  |        \n"
        "__|__\n")
    return i


print("Welcome to my hangman game.")

word_choice = ["DOG", "LYNX", "GOD"]
numbers_list = [True, False, False, True]

word = random.choice(word_choice)

# for i in word:
#   print(i)

guess = []
hangman_pic = ()
guess_wrong = True
attempt = 1
wrong_attempt = 0
limit = 8

answer = []
for i in word:
    answer.append(i)
# print(answer)

blanks = []
for i in range(len(word)):
    blanks.append("_")
print(blanks)

# ['D', 'O', 'G'] not == "DOG"

while (guess_wrong == True) and (wrong_attempt < limit):
    guess_from_user = get_user_input()

    # Correct guess
    if guess_from_user in word:
        guess.append(guess_from_user)
        print("Amount of tries: " + str(attempt))
        print("Correct! One less letter to guess!")
        index_of_guess_from_user = answer.index(guess_from_user)
        blanks[index_of_guess_from_user] = guess_from_user
        print(blanks)
        attempt = attempt + 1
        
        if blanks == answer:
            print("Congrats u got the answer, the word was " + word + "!")
            print("Amount of tries: " + str(attempt))
            print("Amount of wrong tries: " + str(wrong_attempt))
            guess_wrong = False
    
    # Wrong guess
    elif guess_from_user not in word:  
        guess_wrong = True
        print("Ur WRONG BOI, try again!")
        wrong_attempt = wrong_attempt + 1
        print("Amount of wrong tries: " + str(wrong_attempt))
        print("Amount of tries: " + str(attempt))
        attempt = attempt + 1
        print(blanks)
        check_pic(wrong_attempt)


# for index in enumerate(word):
#   print(index)
#   if guessed_letter == index:
#     guessed = guessed_letter.append(guess)
#     print(guessed)
#   else:
#     wrong = input("Try again: ")
