import random


class card():
    def __init__(self, number, card_type):
        self.number = number
        self.card_type = card_type


class jucator():
    def __init__(self, name, nr_cards):
        self.name = name
        self.nr_cards = nr_cards
        self.cards = []
        self.mana_razboi=[]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]
type_cards = ['romb', 'trifoi', 'inima', 'pica']
jucator1 = jucator("Mircea", 0)
card_picked = card(random.choice(numbers), random.choice(type_cards))
jucator1.cards.append(card_picked)
while (jucator1.nr_cards < 25):
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in jucator1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    if card_is_in_hand == 0:
        jucator1.cards.append(card_picked)
        jucator1.nr_cards += 1

jucator2 = jucator("Alex", 0)
card_is_in_hand = 1
while card_is_in_hand == 1:
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in jucator1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
                break

jucator2.cards.append(card_picked)
card_picked = card(random.choice(numbers), random.choice(type_cards))
jucator2.cards.append(card_picked)
while (jucator2.nr_cards < 25):
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in jucator1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    for card_in_hand in jucator2.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    if card_is_in_hand == 0:
        jucator2.cards.append(card_picked)
        jucator2.nr_cards += 1

print("Cartile au fost impartite")
while(jucator1.nr_cards>0 and jucator2.nr_cards>0):
    card_on_filed1 = random.choice(jucator1.cards)
    card_on_filed2 = random.choice(jucator2.cards)
    jucator1.cards.remove(card_on_filed1)
    jucator2.cards.remove(card_on_filed2)
    jucator1.mana_razboi.append(card_on_filed1)
    jucator2.mana_razboi.append(card_on_filed2)

    if card_on_filed1.number > card_on_filed2.number:
        print(card_on_filed1.number, " este mai mare", card_on_filed2.number)
        print("Carti luate de jucatorul ",jucator1.name)
        jucator1.cards.extend(jucator2.mana_razboi)
        jucator1.cards.extend(jucator1.mana_razboi)
        jucator2.nr_cards=jucator2.nr_cards-len(jucator2.mana_razboi)
        jucator1.nr_cards=jucator1.nr_cards+len(jucator1.mana_razboi)
        jucator2.mana_razboi=[]
        jucator1.mana_razboi=[]
    elif (card_on_filed1.number<card_on_filed2.number):
        print(card_on_filed2.number, " este mai mare", card_on_filed1.number)
        print("Carti luate de jucatorul ",jucator2.name)
        jucator2.cards.extend(jucator2.mana_razboi)
        jucator1.cards.extend(jucator1.mana_razboi)
        jucator2.nr_cards=jucator2.nr_cards+len(jucator2.mana_razboi)
        jucator1.nr_cards=jucator1.nr_cards-len(jucator1.mana_razboi)
        jucator2.mana_razboi=[]
        jucator1.mana_razboi=[]
    else:
        for i in range(0,card_on_filed2.number-1):
            card_on_filed1 = random.choice(jucator1.cards)
            card_on_filed2 = random.choice(jucator2.cards)
            jucator1.mana_razboi.append(card_on_filed1)
            jucator1.cards.remove(card_on_filed1)
            jucator2.mana_razboi.append(card_on_filed2)
            jucator2.cards.remove(card_on_filed2)

    for card_in_hand in jucator1.cards:
        print(card_in_hand.number," ",card_in_hand.card_type,end=';')
    print()
    for card_in_hand in jucator2.cards:
        print(card_in_hand.number," ",card_in_hand.card_type,end=';')
    print()
print()
if jucator2.nr_cards<0:
    print(jucator1.name," a castigat")
else:
    print(jucator2.name," a castigat")