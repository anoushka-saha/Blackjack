# Anoushka Saha
# Blackjack
# May 9th, 2024
# Day 11 Capstone Project

# Importing random module
import random

# Import module for clearing terminal
import os

# Card dealing function
def deal_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Score calculating function, using 0 to represent a blackjack
def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    return sum(cards)

#Function that compares user's and computer's score to determine win/loss
def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You both went over. You lose 😤"
    elif user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal the user and computer 2 cards each using deal_card()
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        print("Your cards: " + str(user_cards) + " current score: " + str(user_score))
        print("Computer's first card: " + str(computer_cards[0]))

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # If game hasn't ended, user can ask for another card, or the game ends
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    print("Your Final hand: " + str(user_cards) + " Final score: " + str(user_score))
    print("Computer's Final hand: " + str(computer_cards) + " Final score: " + str(computer_score))
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()
