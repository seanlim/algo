```java
class Solution {
    int[] parents = new int[0];

    public void union(int a, int b) {
        int parentA = findParent(a);
        int parentB = findParent(b);
        if (parentA != parentB) {
            parents[parentB-1] = parentA;
        }
        return;
    }

    public int findParent(int a) {
        if (parents[a-1] == 0) return a;
        parents[a-1] = findParent(parents[a-1]);
        return parents[a-1];
    }

    public int minScore(int n, int[][] roads) {
        parents = new int[n];
        for (int[] road: roads) {
            union(road[0], road[1]);
        }
        int parent = findParent(n);
        int minCost = Integer.MAX_VALUE;
        for (int[] road: roads) {
            if (findParent(road[0]) == parent) {
                minCost = Math.min(minCost, road[2]);
            }
        }
        return minCost;
    }

}
```
