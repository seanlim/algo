
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = ListNode()
        curr = ans
        while l1 or l2:
            l=r=0
            if l1:
                l = l1.val
            if l2:
                r = l2.val
            s = l + r + curr.val
            res = s % 10
            carry = s // 10
            curr.val = res
            if (l1 and l1.next) or (l2 and l2.next) or carry > 0:
                curr.next = ListNode(carry)
                curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ans

```

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
