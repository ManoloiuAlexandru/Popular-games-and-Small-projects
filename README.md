# Popular-card-games
In this repository you can find implementation of popular card games.

  First file is cards-war:
  
  The objective of the game is to win all of the cards.The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.If the two cards played are of equal value, then there is a "war".Both players place the next card of their pile face down (some variants have three face down cards) and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.
  
  The implementation is in Python. It is using basic Object Oriented concepts. The class card is used to define an object that have the 2 attributes of a normal card: number and card_type and the class player has 4 attributes: name- name of the player, nr_card- gives the number of the card, cards- gives the card that the player has in his hands and war_hand- is a list that is used when war is happening.
The player can select if he wants to play or simulate a game. While he is playing informations of who and with what card the hand was won. 

Note: Because the game is dividing the deck randomly sometimes it will enter in infinit cicle and at that point you need to stop it and run it again.

  The second file is sedma:
  
  This game is still in progress.
