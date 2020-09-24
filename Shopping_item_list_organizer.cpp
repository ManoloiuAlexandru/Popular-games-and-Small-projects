#include<iostream>
#include<string>
#include <fstream>
#include"Function.h"
using namespace std;
int main(int argc, char* argv[])
{
	BST b, * root = NULL;
	ofstream output;
	if (argument_parser(argc, argv) == NULL)
	{
		return 0;
	}
	ifstream myfile(argv[argument_parser(argc, argv)[0]]);
	int file_exist = 1;
	string line, word = "", item_name;
	if (myfile.fail()==false && myfile.is_open())
	{
		while (getline(myfile, line))
		{
			word = "";
			for (int i = 0; i < line.size(); i++)
			{
				if (line[i] == ' ')
				{
					item_name = word;
					word = "";
				}
				else
				{
					word += line[i];
				}
			}
			root = b.Insert(root, Item(item_name, stoi(word)));
		}
	}
	else
	{
		output.open(argv[argument_parser(argc, argv)[1]]);
		output << "File doesn't exist.";
		output.close();
		file_exist = 0;
	}
	if (file_exist == 1)
	{
		myfile.close();
		double lower_price;
		cout << "What is the lowest price you are looking for ?" << endl;
		cin >> lower_price;
		auto result = root->search_for_item(root, lower_price, argv[argument_parser(argc, argv)[1]]);
		if (result == NULL)
		{
			output.open(argv[argument_parser(argc, argv)[1]]);
			output << "There are no items lower than that price";
			output.close();
		}
	}
}
