```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private TreeNode tree = null;
    public boolean searchTree(TreeNode root, int val, TreeNode exclude) {
        if (root.val == val)  {
            if (root == exclude) {
                return false;
            }
            return true;
        }
        if (val < root.val) {
            if (root.left == null) {
                return false;
            }
            return searchTree(root.left, val, exclude);
        }
        if (root.right == null) {
            return false;
        }
        return searchTree(root.right, val, exclude);
    }
    public boolean findTarget(TreeNode root, int k) {
        if (this.tree == null) this.tree = root;
        // determine which direction to go
        int diff = k - root.val;
        // search for a node than can fill this.
        boolean treeHasNode = searchTree(this.tree, diff, root);
        if (treeHasNode) {
            return true;
        }
        // if no where left to go, let's give up
        if (root.left == null && root.right == null) {
            return false;
        }
        // no matches found, walk left or right or left and right
        if (root.left != null && root.right != null) {
            return findTarget(root.left, k) || findTarget(root.right, k);
        } else if (root.left == null) {
            return findTarget(root.right, k);
        }
        return findTarget(root.left, k);
    }
}
```
