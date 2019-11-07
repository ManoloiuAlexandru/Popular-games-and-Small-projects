A widely used way to run Python code is through an interactive session. To start a Python interactive session, just open a command-line or terminal and then type in python and the name of the script and then hit Enter.For you to run these programs you need to have Python 3.7  on your PC and you don't need to have any extra packages installed or imported.

# Popular-games
In this repository you can find implementation of popular games.

----------------------------------------------------------------------------------------------------------------------------------------
  Cards-war:
  
  The objective of the game is to win all of the cards.The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored. If the two cards played are of equal value, then there is a "war". Both players place the next card of their pile face down (some variants have three face down cards) and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's. '''Source:(https://en.wikipedia.org/wiki/War_(card_game))'''
  
  The implementation is in Python and it is using basic Object Oriented concepts. The class card is used to define an object that have the 2 attributes of a normal card:number and card_type.
  '''The class player has 4 attributes: name- name of the player'''
      '''nr_card- gives the number of the card'''
      cards- gives the card that the player has in his hands
      war_hand- is a list that is used when war is happening.
  
The player can select if he wants to play or simulate a game. While he is playing informations of who and with what card the hand was won. In this game it does not matter who starts but who has the bigger card at the end of the hand, in this game there can't be a draw.

Note: In the war game the deck is build so it can split the cards easy.

----------------------------------------------------------------------------------------------------------------------------------------
  Sedma:
  
  Sedma is a Czech 4-card trick-and-draw game played by four players in fixed partnerships with a 32-card Bohemian-pattern pack. Card suits do not play a role in this game, and there is no ranking order. A trick is won by the last player to play a card of the same rank as the card led.
  
  Source:(https://en.wikipedia.org/wiki/Sedma)
  
  The implementation is in Python. It is using the same OOP principles as the cards-war game. The class card is used to define an object that have the 2 attributes of a normal card: number and card_type and the class player has 4 attributes: name- name of the player, nr_card- gives the number of the cards, cards- gives the card that the player has in his hands and points- that increase with one everytime you get an A(15) or a 10. While the game is going messages about what card you should play and who won the current hand and how many cards are left in the deck. Also the card class has overloaded the equal operator because you need to remove cards from hand and also keep a track of them. The idea of the game is that player 1 starts with the card that appears most often in his hand. If the opposing player does not have a card with the same number the first player takes the cards and process repeats. Otherwise, if his opponent has the card with the same number then player 1 must give a card of the same number or let player 2 take the cards, in this way player 2 starting the next hand. When switching to the oppsoite player the variable "switched" changes it's value from 1 to 0 or from 0 to 1.

----------------------------------------------------------------------------------------------------------------------------------------
  Hungman:
  
  Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters, within a certain number of guesses.
  
  Source:(https://en.wikipedia.org/wiki/Hangman_(game))

  The implementation is in Python. It is using the same OOP principles as the cards-war game. The class hungman is used to define the word that the player has to guess. In order to get the word that the player has to guess the program uses the Python library "random" and takes a word from the list_of_words, which is a list. The hungman class has another static variabile and that is "full_word" which is used to see if the player has found the word or not, the initial value of this variable is 0, the chances to 1 when to player finds the word. The second class is player which has 4 filds: the life, which means the number of tryes that the player has, if this value gets to 0 and the player dosen't guess the word until then the game is over. The name which is used to get the name of the player, the list_of_used_letters which is used to store all the letters that the player has tryed until now, this is used so that the player will not lose lives if he uses more then once a letter. And the good_letters that is used when a letter that the player has introduce is in the word that he is looking for. The games start after the player introduces his/her name and choices what type of game he/she wants: 1 if the player wants to see the first and the last letter of the word or 2 if the player dosen't want to see any of the letters, then presses a random letter on the keyboard. The game ends when the player is out of lifes or if he finds the word.  
  
 ---------------------------------------------------------------------------------------------------------------------------------------
  BlackJack:
  
  Blackjack is the American variant of a globally popular banking game known as Twenty-One. It is a comparing card game between one or more players and a dealer, where each player in turn competes against the dealer. Players do not compete against each other. It is played with one or more decks of 52 cards, and is the most widely played casino banking game in the world. The objective of the game is to beat the dealer in one of the following ways:

  Get 21 points on the player's first two cards (called a "blackjack" or "natural"), without a dealer blackjack;
  Reach a final score higher than the dealer without exceeding 21; 
  or
  Let the dealer draw additional cards until their hand exceeds 21 ("busted").
  
  Source:(https://en.wikipedia.org/wiki/Blackjack)
  
  The implementation is in Python. It is using the same OOP principles as the cards-war game. The class card is used to define an object that has the 2 attributes of a normal card: number, card_type and a special attribute: hidden-this attribute is for the dealer part, BlackJack has a rule: the dealer will have 2 cards in the start as the player but only one is shown. The class player has 4 attributes: name- name of the player, cards- gives the cards that the player has in his hands and hand_value- that increase with the number on the card, and money - this is the money that the player has at the start. The game begins with the player geting 2 cards and the dealer get 2 cards. The player will see his cards and the dealer's unhidden card. Then the player will be asked to bet a number, if he bets a number bigger then he's money he will be asked to bet less money. The game then is simple after the bet he will be asked if he wants to "stand" or if he wants to "hit". The "stand" option means that the if the dealer will have the hand_value<17 the dealer will draw cards until it gets over or equal to 17, then he's hand value will be calculated, with the player's class methos "calculate_hand", then using the function "win_or_lose", which will check who won and return 1 if the player won,2 if it is a draw or 0 if the dealer won. After we see who won the player will recive his bet * 2 back. If the player selects "hit" this will give him a new card if with the new card he goes over 21 he lost, if the hand_value <21 he will have to choice again if he wants to "hit" or "stand" the game will end when he is out of money.
