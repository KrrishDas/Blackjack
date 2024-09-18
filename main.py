import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    os.system('clear')

def get_card():
    return random.choice(cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        game_win = 'Its a draw!'
    elif user_score == 0:
        game_win = 'You win!'
    elif dealer_score == 0:
        game_win = 'The dealer wins. You lose.'
    else:
        if user_score > dealer_score:
            game_win = 'You win!'
        else:
            game_win = 'The dealer wins. You lose.'
    return game_win


def calculate_score(list):
    if 11 in list:
        if sum(list) == 21:
            return 0
        elif sum(list) > 21:
            list.remove(11)
            list.append(1)
            return sum(list)
    if sum(list) == 21:
        return 0
    return sum(list)


print("Do you wanna play blackjack (y/n): ")
if input() == 'y':
    game1 = True
else:
    game1 = False

while game1:
    game = True
    print(logo)
    print()
    user_cards = []
    dealer_cards = []

    user_cards.append(get_card())
    user_cards.append(get_card())

    dealer_cards.append(get_card())
    dealer_cards.append(get_card())

    while game:

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards} ; current score: {user_score}")
        print(f"one of dealer's cards: {dealer_cards[0]}")

        if user_score > 21:
            game = False
            print(f"Dealers cards: {dealer_cards} ; dealers score: {dealer_score}")
            print("You went over 21. You lose!")
            print()
            break
        elif user_score == 0 or user_score == 21:
            game = False
            print(f"Dealers cards: {dealer_cards} ; dealers score: {dealer_score}")
            print("You got a perfect score. You win!")

        if game == True:
            print("Do you want to draw again? y/n :")
            continue_ = input()
            if continue_ == 'y':

                if dealer_score < 17:
                    x = get_card()
                    dealer_cards.append(x)
                    if calculate_score(dealer_cards) > 17:
                        dealer_cards.remove(x)

                user_cards.append(get_card())

            else:
                game_win = compare(user_score, dealer_score)
                print(f"Your Cards: {user_cards} ; Dealers cards: {dealer_cards}")
                print(f"Your score: {user_score} ; Dealers score: {dealer_score}")
                print(f'{game_win}')
                game = False

    if game == False:
        print()
        print("Do you wanna play blackjack (y/n): ")
        if input() == 'y':

            game1 = True
        else:
            game1 = False

print()
print("THANK YOU FOR PLAYING!")
