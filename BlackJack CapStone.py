import random

def calculate_score(hand):
    score = sum(hand)
    if 1 in hand and score +10 <=21:
        score+=10
    return score

def compare(u_score,c_score):
    if c_score> 21:
        print("Opponent went over 21. You win 😎")
    elif c_score == u_score:
        print("It's a draw 🤝")
    elif c_score > u_score:
        print("Computer wins 😤")
    else:
        print("You win 🎉")

def blackjack():
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]  # 10 για J, Q, K

    while True:
        my_hand = [random.choice(card_list), random.choice(card_list)]
        computer_list = [random.choice(card_list)]

        should_play = True

        while should_play:
            player_score = calculate_score(my_hand)

            print(f"\nYour cards: {my_hand}, current score: {player_score}")
            print(f"Computer's first card: {computer_list[0]}")

            # Έλεγχος για blackjack ή bust
            if player_score == 21:
                print("BlackJack! 🎉 You win!")
                should_play = False
                break
            elif player_score > 21:
                print("You went over 21. You lose 😭")
                should_play = False
                break

            # Απόφαση παίκτη
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == 'y':
                my_hand.append(random.choice(card_list))
            else:
                should_play = False  # σταματά να τραβάει

        # Αν δεν έχασε ο παίκτης, παίζει ο υπολογιστής
        if calculate_score(my_hand) <= 21:
            while calculate_score(computer_list) < 17:
                computer_list.append(random.choice(card_list))

            computer_score = calculate_score(computer_list)
            player_score = calculate_score(my_hand)

            print(f"\nYour final hand: {my_hand}, final score: {player_score}")
            print(f"Computer's final hand: {computer_list}, final score: {computer_score}")

            # Σύγκριση σκορ
            compare(player_score,computer_score)

        # Νέα παρτίδα
        restart = input("\nWould you like to play again? Type 'y' or 'n': ")
        if restart != 'y':
            print("Thanks for playing BlackJack!")
            break

play = input("Would you like to play a game of BlackJack? Type 'y' or 'n': ")
if play != 'y':
    print("Goodbye!")
else:
    blackjack()