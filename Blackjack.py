#Anoushka Saha
#Blackjack
#May 9th, 2024
#Day 11 Capstone Project

#Importing random module
import random

#Card dealing function
def deal_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)



#Score calculating function
def calc_score(cards):
    return sum(cards)

#Dealing the user and computer cards
user_cards = []
comp_cards = []

user_cards.extend([deal_card(), deal_card()])
comp_cards.append([deal_card(), deal_card()])
