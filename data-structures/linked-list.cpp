#include <cstdlib>
#include <iostream>

template <class T> struct Node {
  Node *next;
  T item;
};

template <class T> class List {
  Node<T> *head;
  int length;

public:
  List();
  // ~List();

  void add(T);
  void print();
};

template <class T> List<T>::List() { this->length = 0; }

template <class T> void List<T>::add(T object) {
  Node<T> *node = new Node<T>();
  node->item = object;
  node->next = this->length == 0 ? nullptr : this->head;
  this->head = node;
  this->length++;
  return;
}

// Integer impl
template <class T> void List<T>::print() {
  Node<T> *head = this->head;
  while (head) {
    std::cout << head->item << std::endl;
    head = head->next;
  }
  return;
}

// template <class T> List<T>::~List() {}

int main() {
  List<int> list = List<int>();
  list.add(1);
  list.add(2);
  list.add(3);
  list.print();
}
