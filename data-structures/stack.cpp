
#include <iostream>

template <class T> class stack {
  struct Node {
    Node *next;
    T item;
  };
  Node *top;
  int size;

public:
  stack() {
    top = nullptr;
    size = 0;
  }
  ~stack() {
    Node *tNode;

    while (top) {
      tNode = top;
      delete top;
      top = tNode->next;
    }
  }

  void push(T value) {
    Node *n = new Node;
    n->item = value;
    n->next = top;

    top = n;

    size++;
  }

  T pop() {
    if (!isEmpty()) {
      T val = top->item;
      Node *tNode = top;
      delete top;
      top = tNode->next;
      size -= 1;
      return val;
    } else {
      return 0;
    }
  }

  bool isEmpty() { return size == 0; }
};

int main() {
  stack<int> testStack = stack<int>();
  testStack.push(1);
  testStack.push(2);
  testStack.push(3);
  testStack.push(4);
  testStack.push(5);
  testStack.push(6);
  testStack.push(7);
  while (!testStack.isEmpty()) {
    std::cout << testStack.pop() << std::endl;
  }
}