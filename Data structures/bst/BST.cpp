#include <string>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

/*
 * Implementation of a node-based Binary Search Tree.
 * Binary search trees allow fast lookup and min max.
 * Creates the following tree
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 
*/

struct Node
{
    int key;
    struct Node *left, *right;
};

// Create new node
struct Node *newNode(int i)
{
    struct Node *foo = (struct Node *)malloc(sizeof(struct Node));
    foo->key = i;
    foo->left = NULL;
    foo->right = NULL;
    return foo;
};

// Inorder traversal
void inorder(struct Node *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        printf("%d \n", root->key);
        inorder(root->right);
    }
}

// Create new node
struct Node *insert(struct Node *node, int key)
{
    // Create new node
    if (node == NULL)
        return newNode(key);

    // Recur
    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);

    return node;
}

int main()
{
    struct Node *tree = NULL;
    tree = insert(tree, 10);
    insert(tree, 20);
    insert(tree, 30);
    insert(tree, 40);
    insert(tree, 50);
    insert(tree, 60);
    insert(tree, 25);
    insert(tree, 23);
    insert(tree, 61);

    inorder(tree);
    return 0;
};