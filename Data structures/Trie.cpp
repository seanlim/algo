#include <string>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

/*
 * The Trie data structure is a search tree that is made out of
 * a dynamic array of associated nodes.
 *
 * O(n) Insertion and lookup
 */

struct Node {
    bool isComplete;
    unordered_map<char, Node*> children;

    Node() : isComplete(false) { };
};

Node *root;

// Insert a node
void insert(Node *node, string s, int index) {
    // Set complete
    if (s.length() == index) node->isComplete = true;
    else {
        // Traverse
        char cur = s[index];
        if (node->children[cur] == NULL) node->children[cur] = new Node();
        insert(node->children[cur], s, index + 1);
    }
}

// Check if node exists
bool exists(Node *node, string s, int index) {
    // Check last node
    if (s.length() == index) return (node->isComplete);
    // Check child exists
    if (node->children[s[index]] == NULL) return false;
    else {
        // Recursive case
        return exists(node->children[s[index]], s, index + 1);
    }
}

// Check if node is at fork
bool isFork(Node *node) {
    return (node->children.size() > 2) | (node->isComplete);
}

// Remove a node
bool remove(Node *node, string s, int index, vector<Node*> stk = vector<Node*>(), Node* fork = new Node(), char split_char = char()) {
    if (s.length() == index) {
        // Base Case
        // Delete all nodes in stack
        for (Node *n : stk) {
            delete n;
        }
        fork->children.erase(split_char); // Remove reference to deleted pointer
    }
    else if (node->children[s[index]] == NULL) return false;
    else {
        // Recursive case
        // Define temp variables
        // TODO: more elegant implementation of this block
        vector<Node*> stk_t = stk;
        Node* fork_t = fork;
        char split_t = split_char;

        if (isFork(node)) {
            fork_t = node; // Update fork node
            split_t = s[index]; // Update split character
            stk_t.clear(); // Clear stack
        }

        stk_t.push_back(node->children[s[index]]); // Add current node to stack
        return remove(node->children[s[index]], s, index + 1, stk_t, fork_t, split_t);
    }
}

int main() {
    root = new Node();

    string data [] = {"cat", "bat", "gat", "mat", "batman", "catman"};

    // Build Radix tree
    cout << "Inserted ";
    for (string s: data) {
        insert(root, s, 0);
        cout << s << ", ";
    }
    cout << "into tree" << endl << endl;

    // Setup test
    string test [] = {"cat", "bat", "gat", "ma", "batman", "catman", "gatman"};

    for (string t: test) {
        cout << t << (exists(root, t, 0) ? " Exists": " Does not Exist") << endl;
    }
    cout << endl;
    cout << "Deleting 'catman' ..." << endl << endl;
    // Delete catman
    remove(root, "catman", 0);

    for (string t: test) {
        cout << t << (exists(root, t, 0) ? " Exists": " Does not Exist") << endl;
    }

    return 0;
};