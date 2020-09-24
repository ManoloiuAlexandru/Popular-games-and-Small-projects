#include"Function.h"
#include<string>
#include <fstream>
#include<iostream>
using namespace std;
Item::Item(std::string data,int item_price)
{
    item_name = data;
    price = item_price;
}
Item::Item()
{
    item_name = "";
    price = 0;
}
BST::BST()
{
	item=Item();
	left = right = NULL;
}
BST::BST(Item data)
{
    item = Item(data.item_name, data.price);
	left = right = NULL;
}
BST* BST::Insert(BST* root,Item data)
{
	if (!root)
	{
		return new BST(data);
	}
    if (data.price > root->item.price)
    {
        root->right = Insert(root->right, data);
    }
    else
    {
        root->left = Insert(root->left, data);
    }
    return root;
}
BST* BST::Preorder(BST* root)
{
    if (root == NULL)
    {
        return NULL;
    }
    else
    {
        cout << root->item;
        Preorder(root->left);
        Preorder(root->right);
    }
}
BST* BST::search_for_item(BST* root, double price,std::string output)
{
    ofstream file_output;
    if (root == NULL)
    {
        return NULL;
    }
    else
    {
        if (root->item.price <= price)
        {
            file_output.open(output);
            file_output << "There is this item:"<<root->item;
            file_output.close();
            return root;
        }
        search_for_item(root->left,price,output);
        search_for_item(root->right,price,output);
    }
}
int* argument_parser(int nr_arguments,char** arguments)
{   
    int array_of_args [3],has_output_file=0,has_input_file=0;
    for (int i = 0; i < nr_arguments; i++)
    {
        if (strcmp(arguments[i], "-i")==0)
        {
            array_of_args[0]=i + 1;
            has_input_file = 1;
        }
        else if (strcmp(arguments[i], "-o") == 0)
        {
            array_of_args[1] = i + 1;
            has_output_file = 1;
        }
    }
    if (has_output_file==0)
    {
        cout<<"ERROR: missing output file";
        return NULL;
    }
    else if (has_input_file == 0)
    {
        cout << "ERROR: missing input file";
        return NULL;
    }
    return array_of_args;
}
