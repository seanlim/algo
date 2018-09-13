//
// Created by Sean Lim on 20/4/18.
//

#include <iostream>
#include <vector>

// An obvious bottom up O(n) solve for the classic fibonacci problem
// (Find the n-th number in the fibonacci sequence)

using namespace std;

int fib(int n) {
    // First two numbers are 1
    if (n == 1 || n == 2) {
        return 1;
    }
    // Memoisation
    vector<int> stack (n);
    stack.at(0) = 1;
    stack.at(1) = 1;

    for (int i = 2; i < n ; ++i) {
        stack.at(i) = stack[i - 1] + stack[i - 2];
    }

    return stack[n - 1];

}

int main () {
    cout << fib(17);
    return 0;
}