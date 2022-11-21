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
