```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        ArrayList<Integer> numsCopy = new ArrayList<Integer>();
        for (int i: nums) {
            numsCopy.add(i);
        }
        int[] res = new int[2];

        Arrays.sort(nums);

        int head = 0;
        int tail = nums.length - 1;

        while (head < tail) {
            int sum = nums[head] + nums[tail];
            if (sum == target) {
                res[0] = numsCopy.indexOf(nums[head]);
                res[1] = numsCopy.lastIndexOf(nums[tail]);
                return res;
            }
            if (sum < target) {
                head++;
            } else {
                tail--;
            }
        }

        return res;
    }
}
```

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const n = nums.map((v, i) => ({ value: v, index: i }));
  n.sort((a, b) => a.value - b.value);
  let front = 0,
    back = n.length - 1;
  while (back > front) {
    const b = n[back];
    const f = n[front];
    if (b.value + f.value === target) {
      return [b.index, f.index];
    } else if (b.value + f.value > target) {
      back--;
      continue;
    } else if (b.value + f.value < target) {
      front++;
      continue;
    }
  }
};
```
