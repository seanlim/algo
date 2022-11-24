```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        int head = 0;
        int tail = numbers.length - 1;

        while (head < tail) {
            int sum = numbers[head] + numbers[tail];
            if (sum == target) {
                res[0] = head + 1;
                res[1] = tail + 1;
            }
            if (sum > target) {
                tail--;
            } else {
                head++;
            }
        }

        return res;
    }
}
```
