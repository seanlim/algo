# [Leetcode 20: Valid parentheses](https://leetcode.com/problems/valid-parentheses/)

## Approach

Create a list/array and use it like a stack. Then for each character in the input string:

- if it is an opening brace, we push it onto the stack.
- if it is a closing brace, we check:
  - if the stack is empty, then the entire string is invalid
  - if the opening brace on the top of the stack does not map to the current closing brace, then the entire string is invalid

Once we are done with this, the stack will either be empty or nonempty. If the string is valid, the stack should be empty because all open/closing braces should balance out to an empty stack!

## Python Solution

```py
opener=["(","[","{"]
closer_map={
    "(":")",
    "[":"]",
    "{":"}"
}
class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in opener:
                stack.append(c)
                continue
            if not stack or c != closer_map[stack.pop(-1)]:
                return False
        return not stack
```

## JavaScript Solution

```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stackArr = [];
  for (let i = 0; i < s.length; i++) {
    const c = s.charAt(i);
    if (["(", "{", "["].includes(c)) {
      stackArr.push(c);
    } else {
      if (stackArr.length === 0) return false;
      if (
        stackArr[stackArr.length - 1] ===
        {
          "]": "[",
          ")": "(",
          "}": "{",
        }[c]
      ) {
        stackArr.pop();
      } else {
        return false;
      }
    }
  }
  return stackArr.length === 0;
};
```
