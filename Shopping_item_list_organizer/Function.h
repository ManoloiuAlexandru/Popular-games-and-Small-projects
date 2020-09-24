#include<string>
#include <iostream>
using namespace std;
class Item
{
public:
	std::string item_name;
	int price;
	Item(std::string name, int price);
	Item();
	friend ostream& operator<<(ostream& output, Item& item)
	{
		output << item.item_name << " " << item.price << endl;
		return output;
	}
	
};
class BST
{
public:
	Item item;
	BST* left, * right;
	BST();
	BST(Item data);
	BST* Insert(BST*, Item data);
	BST* Preorder(BST*);
	BST* search_for_item(BST*, double price,std::string output);
};
int* argument_parser(int,char**);
