A widely used way to run Python code is through an interactive session. To start a Python interactive session, just open a command-line or terminal and then type in python and the name of the script and then hit Enter.For you to run these programs you need to have Python 3.7  on your PC and you don't need to have any extra packages installed or imported.

# Popular-card-games
In this repository you can find implementation of popular card games.

  The second file is sedma:
  
  Sedma is a Czech 4-card trick-and-draw game played by four players in fixed partnerships with a 32-card Bohemian-pattern pack. Card suits do not play a role in this game, and there is no ranking order. A trick is won by the last player to play a card of the same rank as the card led.
  
  The implementation is in Python. It is using the same OOP principles as the cards-war game. The class card is used to define an object that have the 2 attributes of a normal card: number and card_type and the class player has 4 attributes: name- name of the player, nr_card- gives the number of the card, cards- gives the card that the player has in his hands and points- that increase with one everytime you get an A(15) or a 10. While the game is going messages about what card you should play and who won the current hand and how many cards ar left in the deck. Also the card class has overloads the equal operator because you need to remove cards from hand and also keep a track of them. The idea of the game is that player 1 starts with the card that appears most often in his hand. If the opposing player does not have a card with the same number the first player takes the cards and process repeats. Otherwise, if his opponent has the card with the same number then player 1 must give a card of the same number or let player 2 take the cards, in this way player 2 starting the next hand. When switching to the oppsoite player the variable switched changes it value from 1 to 0 or from 0 to 1.
