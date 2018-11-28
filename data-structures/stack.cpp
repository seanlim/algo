
#include <iostream>

template <class T> class stack {
  template <class F> struct Node {
    Node *next;
    F item;
  };
  Node<T> *top;
  int size;

public:
  stack() {
    top = nullptr;
    size = 0;
  }
  ~stack() {
    Node<T> *tNode;

    while (top) {
      tNode = top;
      delete top;
      top = tNode->next;
    }
  }

  void push(T value) {
    Node<T> *n = new Node<T>;
    n->item = value;
    n->next = top;

    top = n;

    size++;
  }

  T pop() {
    if (!isEmpty()) {
      T val = top->item;
      Node<T> *tNode = top;
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