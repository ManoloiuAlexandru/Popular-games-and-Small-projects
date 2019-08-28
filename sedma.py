import random


class card:
    def __init__(self, number, card_type):
        self.number = number
        self.card_type = card_type

    def __eq__(self, other):
        if not isinstance(other, card):
            return NotImplemented

        return self.number == other.number and self.card_type == other.card_type


class player:
    def __init__(self, name, nr_cards):
        self.name = name
        self.nr_cards = nr_cards
        self.cards = []
        self.points = 0


numbers = [7, 8, 9, 10, 12, 13, 14, 15]
type_cards = ['diamond', 'clover', 'hearts', 'spades']
out_cards = []
deck_size = 32
player1 = player("player 1", 0)
card_picked = card(random.choice(numbers), random.choice(type_cards))
player1.cards.append(card_picked)
while (player1.nr_cards < 3):
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    if card_is_in_hand == 0:
        player1.cards.append(card_picked)
        player1.nr_cards += 1

player2 = player("player 2", 0)
card_is_in_hand = 1
while card_is_in_hand == 1:
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
                break

player2.cards.append(card_picked)
card_picked = card(random.choice(numbers), random.choice(type_cards))
player2.cards.append(card_picked)
while (player2.nr_cards < 2):
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    for card_in_hand in player2.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    if card_is_in_hand == 0:
        player2.cards.append(card_picked)
        player2.nr_cards += 1

deck_size -= 8
for card_in_hand in player1.cards:
    print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
print()
player1.nr_cards = 4
for card_in_hand in player2.cards:
    print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
print()
player2.nr_cards = 4
card_down2 = None
card_down1 = None
in_progress = 0
switched = 0
while deck_size > 0 and player1.nr_cards > 0 and player2.nr_cards > 0:
    max_nr_of_card = 0
    if (in_progress == 0):
        card_to_play = card(None, None)
        for card_in_hand in player1.cards:
            nr_of_card = player1.cards.count(card_in_hand)
            if nr_of_card == 4 and card_in_hand.number == 7:
                print("Player 1 won because he has only 7's in his hand")
                deck_size = 0
            elif (card_in_hand.number == 7 and nr_of_card > 1) or (card_in_hand.number == 7 and player1.nr_cards == 1):
                max_nr_of_card = nr_of_card
                card_to_play = card_in_hand
            elif max_nr_of_card < nr_of_card and card_in_hand.number != 7 and player1.nr_cards > 1:
                max_nr_of_card = nr_of_card
                card_to_play = card_in_hand
        print("Player 1 should play this card", card_to_play.card_type, card_to_play.number)
        card_down1 = card_to_play
        player1.nr_cards -= 1
        player1.cards.remove(card_down1)
        out_cards.append(card_down1)
    else:
        card_to_play = card_down1
        print("Player 1 should play this card", card_to_play.card_type, card_to_play.number)
    for card_in_hand in player1.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print()
    for card_in_hand in player2.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print("There are ", deck_size, " cards left")
    print()

    max_nr_of_card = 0
    if (in_progress == 0):
        card_to_play = card(None, None)
        for card_in_hand in player2.cards:
            nr_of_card = player2.cards.count(card_in_hand)
            if nr_of_card == 4 and card_in_hand.number == 7:
                print("Player 2 won because he has only 7's in his hand")
                deck_size = 0
            elif (card_in_hand.number == 7 and nr_of_card > 1) or (card_in_hand.number == 7 and player2.nr_cards == 1):
                max_nr_of_card = nr_of_card
                card_to_play = card_in_hand
            elif max_nr_of_card < nr_of_card and card_in_hand.number != 7 and player2.nr_cards > 1:
                max_nr_of_card = nr_of_card
                card_to_play = card_in_hand
        print("Player 2 should play this card", card_to_play.card_type, card_to_play.number)
        card_down2 = card_to_play
        player2.nr_cards -= 1
        player2.cards.remove(card_down2)
        out_cards.append(card_down2)
    else:
        card_to_play = card_down2
        print("Player 2 should play this card", card_to_play.card_type, card_to_play.number)
    for card_in_hand in player1.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print()
    for card_in_hand in player2.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print("There are ", deck_size, " cards left")
    print()

    if card_down1.number != card_down2.number and card_down2.number != 7 and switched == 1:
        in_progress = 0
        print("Player 1 gets the cards")
        if card_down1.number == 10 or card_down1.number == 15:
            player1.points += 1
        for card_in_hand in player1.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()
        for card_in_hand in player2.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print("There are ", deck_size, " cards left")
        print()

        while player1.nr_cards < 4 and deck_size > 0:
            card_picked = card(random.choice(numbers), random.choice(type_cards))
            card_is_in_hand = 0
            for card_in_hand in player1.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in out_cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in player2.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1

            if card_is_in_hand == 0:
                player1.cards.append(card_picked)
                player1.nr_cards += 1
                deck_size -= 1
        while player2.nr_cards < 4 and deck_size > 0:
            card_picked = card(random.choice(numbers), random.choice(type_cards))
            card_is_in_hand = 0
            for card_in_hand in player1.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in player2.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in out_cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            if card_is_in_hand == 0:
                player2.cards.append(card_picked)
                player2.nr_cards += 1
                deck_size -= 1
        for card_in_hand in player1.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()
        for card_in_hand in player2.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()

    elif card_down1.number == card_down2.number:
        in_progress = 1
        can_continue = 0
        for card_in_hand in player1.cards:
            if card_down1.number == card_in_hand.number:
                card_down1 = card_in_hand
                player1.nr_cards -= 1
                player1.cards.remove(card_down1)
                out_cards.append(card_down1)
                can_continue = 1
                break
        if can_continue == 0:
            for card_in_hand in player1.cards:
                if card_in_hand.number != 10 or card_in_hand.number != 15 or card_in_hand.number != 7:
                    card_down1 = card_in_hand
                    player1.nr_cards -= 1
                    player1.cards.remove(card_down1)
                    out_cards.append(card_down1)
                    switched = 1
                    break
        can_continue = 0
        for card_in_hand in player2.cards:
            if card_down2.number == card_in_hand.number:
                card_down2 = card_in_hand
                player2.nr_cards -= 1
                player2.cards.remove(card_down2)
                out_cards.append(card_down2)
                can_continue = 1
                switched = 0
                break
        if can_continue == 0:
            for card_in_hand in player2.cards:
                if card_in_hand.number != 10 or card_in_hand.number != 15 or card_in_hand.number != 7:
                    card_down2 = card_in_hand
                    player2.nr_cards -= 1
                    player2.cards.remove(card_down2)
                    out_cards.append(card_down2)
                    break
    else:
        in_progress = 0
        print("Player 2 gets the cards")
        if card_down1.number == 10 or card_down1.number == 15:
            player2.points += 1
        for card_in_hand in player1.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()
        for card_in_hand in player2.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print("There are ", deck_size, " cards left")
        print()

        while player1.nr_cards < 4 and deck_size > 0:
            deck_size -= 1
            card_picked = card(random.choice(numbers), random.choice(type_cards))
            card_is_in_hand = 0
            for card_in_hand in player1.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in out_cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            if card_is_in_hand == 0:
                player1.cards.append(card_picked)
                player1.nr_cards += 1
        while player2.nr_cards < 4 and deck_size > 0:
            deck_size -= 1
            card_picked = card(random.choice(numbers), random.choice(type_cards))
            card_is_in_hand = 0
            for card_in_hand in player1.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in player2.cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            for card_in_hand in out_cards:
                if card_picked.card_type == card_in_hand.card_type:
                    if card_picked.number == card_in_hand.number:
                        card_is_in_hand = 1
            if card_is_in_hand == 0:
                player2.cards.append(card_picked)
                player2.nr_cards += 1
        for card_in_hand in player1.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print()
        for card_in_hand in player2.cards:
            print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
        print("There are ", deck_size, " cards left")
        print()

if player2.points > player1.points:
    print("Player 2 wins")
elif player1.points > player2.points:
    print("Player 1 wins")
else:
    print("Draw")
