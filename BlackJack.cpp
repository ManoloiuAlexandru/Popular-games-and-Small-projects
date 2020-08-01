#include<iostream>
#include<vector>
#include<random>
#include <time.h>
#include <stdlib.h>
#include<algorithm>
using namespace std;
class Card
{
public:
	int number;
	string card_type;
	bool hidden;
	Card(int nr, string ct)
	{
		number = nr;
		card_type = ct;
		hidden = 0;
	}
	bool operator ==(const Card& card_to_comp) {
		if (number == card_to_comp.number && card_type==card_to_comp.card_type) {
			return true;
		}

		return false;
	}
};
class Player
{
public:
	int hand_value;
	vector<Card> cards;
	string name;
	int money;
	Player(string nm,int mon)
	{
		name = nm;
		money = mon;
	}
	void show_hand()
	{
		for (auto& card : cards)
		{
			if (card.hidden == 1)
			{
				cout << "Hidden card" << endl;
			}
			else
			{
				cout << card.number << " " << card.card_type << endl;
			}
		}
	}
	void calculate_hand()
	{
		hand_value = 0;
		for (auto& card : cards)
		{
			if (card.number > 11 && card.hidden == 0)
			{
				hand_value += 10;
			}
			else if (card.hidden == 0)
			{
				hand_value += card.number;
			}
		}
	}
};
void show_hands(Player player, Player dealer)
{
	cout << "Your hand:" << endl;
	player.show_hand();
	cout << "Your hand value:" << player.hand_value << endl;
	cout << "Dealer hand" << endl;
	dealer.show_hand();
	cout << "Dealer hand value:" << dealer.hand_value << endl;
}
int win_or_lose(Player player, Player dealer)
{
	show_hands(player, dealer);
	if (player.hand_value > dealer.hand_value && player.hand_value > 21)
	{
		cout << "You lose" << endl;
		return 0;
	}
	else if (dealer.hand_value < player.hand_value && player.hand_value <= 21)
	{
		cout << "You won" << endl;
		return 1;
	}
	else if (21 >= dealer.hand_value && dealer.hand_value > player.hand_value)
	{
		cout << "You lose" << endl;
		return 0;
	}
	else if (dealer.hand_value > 21 && 21 >= player.hand_value)
	{
		cout << "You won" << endl;
		return 1;
	}
	else if (dealer.hand_value == player.hand_value)
	{
		cout << "Push" << endl;
		return 2;
	}
}
void clear_hands(Player player1, Player dealer)
{
	player1.cards.clear();
	dealer.cards.clear();
}
int main()
{
	vector<int> numbers = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 };
	vector<string> type_cards = { "diamond", "clover", "hearts", "spades" };
	vector<Card> deck;
	int result;
	for (auto& number : numbers)
	{
		for (auto& type_card : type_cards)
		{
			deck.push_back(Card(number, type_card));
		}
	}
	Player player1("Player1",100);
	Player dealer("Dealer", 0);
	string play;
	Card card_picked(0,"");
	cout << "Want to play ?";
	cin >> play;
	while (play == "yes" && player1.money > 0)
	{
		for (int i = 0; i < 2; i++)
		{
			srand(time(NULL));
			card_picked = deck[rand() % deck.size()];
			while (find(player1.cards.begin(), player1.cards.end(), card_picked) != player1.cards.end())
			{
				card_picked = deck[rand() % deck.size()];
			}
			player1.cards.push_back(card_picked);
		}
		card_picked = deck[rand() % deck.size()];
		while (find(dealer.cards.begin(), dealer.cards.end(), card_picked) != dealer.cards.end())
		{
			card_picked = deck[rand() % deck.size()];
		}
		dealer.cards.push_back(card_picked);
		card_picked = deck[rand() % deck.size()];
		while (find(dealer.cards.begin(), dealer.cards.end(), card_picked) != dealer.cards.end())
		{
			card_picked = deck[rand() % deck.size()];
		}
		card_picked.hidden = 1;
		dealer.cards.push_back(card_picked);
		player1.calculate_hand();
		dealer.calculate_hand();
		show_hands(player1, dealer);
		string choice = "";
		cout << "Your money:" << player1.money << endl;
		int money_in_game;
		cout << "How much money you want to bet?" << endl;
		cin >> money_in_game;
		while (money_in_game > player1.money)
		{
			cout << "You don't have enough money!";
			cout << "How much money you want to bet?";
			cin >> money_in_game;
		}
		player1.money -= money_in_game;
		while (player1.hand_value < 21 && dealer.hand_value < 21 && choice != "stand")
		{
			cout << "Hit or stand?";
			cin >> choice;
			if (choice == "stand")
			{
				for (auto& card : dealer.cards)
				{
					card.hidden = 0;
				}
				dealer.calculate_hand();
				while (dealer.hand_value < 17)
				{
					card_picked = deck[rand() % deck.size()];
					while (find(dealer.cards.begin(), dealer.cards.end(), card_picked) != dealer.cards.end())
					{
						card_picked = deck[rand() % deck.size()];
					}
					dealer.cards.push_back(card_picked);
					dealer.calculate_hand();
						if (dealer.hand_value > 21)
						{
							result = 1;
								break;
						}
				}
				result = win_or_lose(player1, dealer);
			}
			else if (choice == "hit")
			{
				card_picked = deck[rand() % deck.size()];
				while (find(player1.cards.begin(), player1.cards.end(), card_picked) != player1.cards.end())
				{
					card_picked = deck[rand() % deck.size()];
				}
				player1.cards.push_back(card_picked);
				player1.calculate_hand();
				show_hands(player1, dealer);
			}
		}
		if (choice != "stand")
		{
			for (auto& card : dealer.cards)
			{
				card.hidden = 0;
			}
			result = win_or_lose(player1, dealer);
		}
		if (result == 1)
		{
			player1.money += money_in_game * 2;
			clear_hands(player1, dealer);
		}
		if (result == 2)
		{
			player1.money += money_in_game;
			clear_hands(player1, dealer);
		}
		else
		{
			clear_hands(player1, dealer);
		}
		cout << "Keep playing ?";
		cin >> play;
		if (player1.money <= 0 and play == "yes")
		{
			cout << "You are out of money !" << endl;
		}
	}
}
