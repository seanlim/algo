#include <stdio.h>

// Circular queue
template <typename T> struct Queue {
  int rear, front;
  int size;
  T *arr;
  Queue(int _size) {
    front = rear = -1;
    size = _size;
    arr = new T[_size];
  }
  void enQueue(T value);
  T deQueue();
  void displayQueue(); // Debug
};

template <typename T> void Queue<T>::enQueue(T value) {
  if ((front == 0 && rear == size - 1) || (rear == (front - 1))) {
    printf("\nQueue is Full");
    return;
  }

  else if (front == -1) {
    // Insert first
    front = rear = 0;
    arr[rear] = value;
  }

  else if (rear == size - 1 && front != 0) {
    rear = 0;
    arr[rear] = value;
  }

  else {
    rear++;
    arr[rear] = value;
  }
}

template <typename T> T Queue<T>::deQueue() {
  if (front == -1) {
    printf("\nQueue is Empty");
    return nullptr;
  }

  T data = arr[front];
  arr[front] = nullptr;
  if (front == rear) {
    front = -1;
    rear = -1;
  } else if (front == size - 1)
    front = 0;
  else
    front++;

  return data;
}

template <typename T> void Queue<T>::displayQueue() {
  if (front == -1) {
    printf("\nQueue is Empty");
    return;
  }
  printf("\nElements in Circular Queue are: ");
  if (rear >= front) {
    for (int i = front; i <= rear; i++)
      printf("%s ", arr[i]);
  } else {
    for (int i = front; i < size; i++)
      printf("%s ", arr[i]);

    for (int i = 0; i <= rear; i++)
      printf("%s ", arr[i]);
  }
}

int main() {
  Queue<const char *> q(5);

  q.enQueue("test 1 ");
  q.enQueue("man");
  q.enQueue("queue");
  q.enQueue("test");

  q.displayQueue();

  printf("\nDeleted value = %s", q.deQueue());
  printf("\nDeleted value = %s", q.deQueue());

  q.displayQueue();

  q.enQueue("hello");
  q.enQueue("world");
  q.enQueue("Test");

  q.displayQueue();

  q.enQueue("day");
  return 0;
}
