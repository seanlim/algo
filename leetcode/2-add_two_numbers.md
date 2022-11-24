```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        boolean hasNext1 = l1.next != null;
        boolean hasNext2 = l2.next != null;
        ListNode next1 = !hasNext1 ? new ListNode(0): l1.next;
        ListNode next2 = !hasNext2 ? new ListNode(0): l2.next;
        int num1 = l1 == null ? 0: l1.val;
        int num2 = l2 == null ? 0: l2.val;
        int sum = num1 + num2;
        boolean carryForward = sum >= 10;
        // terminal case
        if (!hasNext1 && !hasNext2) {
            if (carryForward) {
                return new ListNode(sum - 10, new ListNode(1));
            }
            return new ListNode(sum);
        }
        // either 1 or 2 could be null
        // carry forward either through 1 or 2
        if (carryForward) {
            if (hasNext1) {
                next1.val += 1;
            } else {
                next2.val += 1;
            }
            sum -= 10;
        }
        return new ListNode(sum, addTwoNumbers(next1, next2));
    }
}
```
