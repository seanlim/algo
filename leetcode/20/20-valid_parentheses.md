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
