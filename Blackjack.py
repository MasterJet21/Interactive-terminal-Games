import random

user_hand = []
computer_hand = []

# Turn 1 (Draw user cards):
first_card_for_user = random.randint(1,10)
second_card_for_comp = random.randint(1,10)
fifth_card_for_user = random.randint(1,10)

# Turn 2 (Draw computer cards):
third_card_for_user = random.randint(1,10)
fourth_card_for_comp = random.randint(1,10)
sixth_card_for_comp = random.randint(1,10)

user_hand.append(first_card_for_user)
computer_hand.append(second_card_for_comp)
user_hand.append(third_card_for_user)
computer_hand.append(fourth_card_for_comp)
user_hand.append(fifth_card_for_user)
computer_hand.append(sixth_card_for_comp)

total_score_for_comp = second_card_for_comp +  fourth_card_for_comp + sixth_card_for_comp
total_score_for_user = first_card_for_user + third_card_for_user + fifth_card_for_user
yo = 0

if total_score_for_user > 21:
    yo = 1
elif total_score_for_comp > 21:
    yo = 2

if yo == 1:
    print("BOOM, exceeded 21, u lost!")
    print("Computer's score was " + str(total_score_for_comp))
    print("Your score was " + str(total_score_for_user))
elif yo == 2:
    print("Boom, the computer's score exceeded 21, U won!")
    print("Computer's score was " + str(total_score_for_comp))
    print("Your score was " + str(total_score_for_user))

elif total_score_for_user < total_score_for_comp:
    print("Loser")
    print("Computer's score was " + str(total_score_for_comp))
    print("Your score was " + str(total_score_for_user))

elif total_score_for_comp < total_score_for_user:
    print("Winner winner chicken dinner")
    print("Computer's score was " + str(total_score_for_comp))
    print("Your score was " + str(total_score_for_user))

elif total_score_for_user == total_score_for_comp:
    print("Draw!!!!!!!!!")
    print("Each of your scores were " + str(total_score_for_comp))
    
print(f"{computer_hand} is the computer hand")
print(f"{user_hand} is the user hand")




