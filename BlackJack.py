import random


class Card:
    def __init__(self, number, card_type):
        self.number = number
        self.card_type = card_type
        self.hidden = False


class Player:
    def __init__(self, name, money):
        self.name = name
        self.cards = []
        self.hand_value = 0
        self.money = money

    def show_hand(self):
        for card in self.cards:
            if card.hidden is False:
                print(card.number, " ", card.card_type)
            else:
                print("Hidden card")

    def calculate_hand(self):
        self.hand_value = 0
        for card in self.cards:
            if card.number > 11 and card.hidden is False:
                self.hand_value += 10
            elif card.hidden is False:
                self.hand_value += card.number


def win_or_lose(player, dealer):
    show_hands(player, dealer)
    if player.hand_value > dealer.hand_value and player.hand_value > 21:
        print("You lose")
        return 0
    elif dealer.hand_value < player.hand_value <= 21:
        print("You won")
        return 1
    elif 21 >= dealer.hand_value > player.hand_value:
        print("You lose")
        return 0
    elif dealer.hand_value > 21 >= player.hand_value:
        print("You won")
        return 1


def show_hands(player, dealer):
    print("Your hand")
    player.show_hand()
    print("Your hand value:", player.hand_value)
    print("Dealer hand")
    dealer.show_hand()
    print("Dealer hand value:", dealer.hand_value)


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
type_cards = ['diamond', 'clover', 'hearts', 'spades']
deck = []
for number in numbers:
    for type_card in type_cards:
        deck.append(Card(number, type_card))

player1 = Player("Player 1", 100)
dealer = Player("Dealer", 0)

while player1.money > 0:
    for i in range(0, 2):
        card_picked = random.choice(deck)
        player1.cards.append(card_picked)
        deck.remove(card_picked)
    card_picked = random.choice(deck)
    dealer.cards.append(card_picked)
    deck.remove(card_picked)
    card_picked = random.choice(deck)
    card_picked.hidden = True
    dealer.cards.append(card_picked)
    deck.remove(card_picked)
    player1.calculate_hand()
    dealer.calculate_hand()
    show_hands(player1, dealer)
    choice = ""
    print("Your money:", player1.money)
    money_in_game = int(input("How much money you want to bet?"))
    while money_in_game > player1.money:
        print("You don't have enough money!")
        money_in_game = int(input("How much money you want to bet?"))
            
    player1.money -= money_in_game
    while player1.hand_value <= 21 and dealer.hand_value <= 21 and choice != "stand":
        choice = input("Hit or stand?")
        if choice == "stand":
            card_picked = random.choice(deck)
            dealer.cards.append(card_picked)
            deck.remove(card_picked)
            for card in dealer.cards:
                card.hidden = False
            dealer.calculate_hand()
            result = win_or_lose(player1, dealer)
        elif choice == "hit":
            card_picked = random.choice(deck)
            player1.cards.append(card_picked)
            deck.remove(card_picked)
            player1.calculate_hand()
            show_hands(player1, dealer)

    if choice != "stand":
        for card in dealer.cards:
            card.hidden = False
        result = win_or_lose(player1, dealer)

    if result == 1:
        player1.money += money_in_game * 2
        dealer.cards.clear()
        player1.cards.clear()
    else:
        dealer.cards.clear()
        player1.cards.clear()
