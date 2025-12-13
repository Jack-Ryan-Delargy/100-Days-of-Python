import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []
user_total = 0
computer_total = 0


def deal_card(cards, user_cards, computer_cards):
    while len(user_cards) < 2:
        user_cards.append(random.choice(cards))
    while len(computer_cards) < 2:
        computer_cards.append(random.choice(cards))

def calculate_score(user_cards, computer_cards):
    def calculate_user_score(user_total):
        user_total = sum(user_cards)
        return
    def calculate_computer_score(computer_total):
        computer_total = sum(computer_cards)
        return


deal_card(cards, user_cards, computer_cards)

#print(f"User cards: {user_cards}\nComputer Cards: {computer_cards}")
