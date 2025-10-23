import random
# card_list = [1,2,3,4,5,6,7,8,9,10,10,10]
# my_hand = []
# computer_list = []
# rc1 = random.choice(card_list)
# rc2 = random.choice(card_list)
# my_hand.append(rc1)
# my_hand.append(rc2)

#
# computer_card = random.choice(card_list)
# computer_list.append(computer_card)
# new_user_card = random.choice(card_list)
#                 my_hand.append(new_user_card)
#                 player_score = sum(my_hand)
#                 print(f"Your cards: {my_hand}, current player_score: {player_score}")
#                 print(f"Computer's first card: {computer_card}")
#                 if player_score > 21:
#                     print(f"You went over 21. You lost! Final hand: {my_hand}, player_score: {player_score}")
#                     should_play = False
#                 elif player_score == 21:
#                     print(f"You scored {player_score}, it's a Blackjack")
#                     restart = input("Would you like to play again? Type 'y' or 'n': ")
#                     if restart == 'y':
#                         blackjack()
#                     else:
#                         should_play = False
#                 else:
#                     continue
#             else:
#                 computer_score = sum(computer_list)
#
#                 computers_new_card = random.choice(card_list)
#                 computer_list.append(computers_new_card)
#                 computer_new_score = sum(computer_list)
#                 while computer_new_score <=20 and computer_new_score<=21:
#                     computer_list.append(computers_new_card)
#                     computer_new_score = sum(computer_list)
#                     if computer_new_score >21:
#                         should_play = False
#                         print(f"Your final hand: {my_hand}, final player_score: {player_score}")
#                         print(f"Computer's final hand: {computer_list}, final player_score: {computer_new_score}")
#                         print("Opponent went over. You win")
#                     elif computer_score == 21:
#                         should_play = False
#                         print(f"Your final hand: {my_hand}, final player_score: {player_score}")
#                         print(f"Computer's final hand: {computer_list}, final player_score: {computer_new_score}")
#                         print(f"Computer hit a blackjack. You lose")
#                     else:
#                         print("You win")
#     else:
#         print("GoodBye")