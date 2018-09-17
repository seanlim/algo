#include <iostream>
#include <vector>

using namespace std;

// Finding the n-th number in the fibonacci sequence.

// Recursion (unoptimized)
int fib(int n) {
  if (n <= 1)
    return n;
  return fib(n - 1) + fib(n - 2);
}

// Memoized recursive solve
int fib_memoized(int n) {
  static vector<int> memo(n);
  memo.at(0) = 1, memo.at(1) = 1;

  if (memo[n - 1])
    return memo[n - 1];

  int res = fib_memoized(n - 1) + fib_memoized(n - 2);
  memo[n - 1] = res;
  return res;
}

// O(n) bottom-up solve
int fib_bottom_up(int n) {
  // First two numbers are 1
  if (n == 1 || n == 2) {
    return 1;
  }
  // Storing all fib numbers calculated
  vector<int> stack(n);
  stack.at(0) = 1;
  stack.at(1) = 1;

  for (int i = 2; i < n; ++i) {
    stack.at(i) = stack[i - 1] + stack[i - 2];
  }

  return stack[n - 1];
}

// Space-optimized bottom-up solve
// Stores the previous two numbers only
int fib_bottom_up2(int n) {
  int a = 0, b = 1, c;
  for (int i = 2; i <= n; i++) {
    c = a + b;
    a = b;
    b = c;
  }
  return b;
}

int main() {
  cout << fib(17) << endl;
  cout << fib_memoized(17) << endl;
  cout << fib_bottom_up(17) << endl;
  cout << fib_bottom_up2(17) << endl;
  return 0;
}
