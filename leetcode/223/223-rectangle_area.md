# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

We can make use of collision-checking algorithm for axis-aligned bounded boxes to determine if the two shapes are colliding.

Ignoring our edge cases first, we'd have two scenarios:

1. **Shapes do not collide**
   This means we are able to return the sum of both shapes directly as they do not collide.

2. **Shapes collide**
   This means we need to find the area of the intersection and take that away from the sum of both shapes' areas.

# Approach

<!-- Describe your approach to solving the problem. -->

Firstly, I wrote a `findArea` function that takes the bottom-left and top-right points of a box and calculates its area.

Compute the area of both boxes and call them `areaA` and `areaB`.

Check for edge cases:

- If area of either shape is 0, return the area of the other (if both are 0 it is the same).
- If a shape is nested within the other, return the larger area.

Compute the `sum` of `areaA` and `areaB`.

Check if both boxes collide. The conditions are:

1. A's `min-x` is less than B's `max-x` AND A's `max-x` is more than B's `min-x`.
2. A's `min-y` is less than B's `max-y1` AND A's `max-y` is more than B's `min-y`.

If they do not collide, we can return the `sum` straight away.

If they collide, we need to find the area of their intersection. Because both shapes are boxes and they don't rotate, the shape of this intersection is always a box. We need to find the `x1x2y1y2` values of this intersection:

- `(ix1, iy1)`: check the `min-x` and `min-y` values of A and B to derive the coordinates of this point.
- `(ix2, iy2)`: check the `max-x` and `max-y` values of A and B to derive the coordinates of this point.

Now, we can plug these points into `findArea` and minus the result from our `sum`. We have successfully calculated the area of two intersecting rects.

# Code

```java
class Solution {
    private int findArea (int x1, int y1, int x2, int y2) {
        return Math.abs((x2 - x1) * (y2 - y1));
    }
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int areaA = findArea(ax1, ay1, ax2, ay2);
        int areaB = findArea(bx1, by1, bx2, by2);

        // if either is 0, we have nothing left to do
        if (areaA == 0) return areaB;
        if (areaB == 0) return areaA;

        // check if shapes are contained within each other
        if (ax1>bx1 && ax2<bx2 && ay1>by1 && ay2<by2) {
            return areaB;
        }
        if (bx1>ax1 && bx2<ax2 && by1>ay1 && by2<ay2) {
            return areaA;
        }

        int sum = areaA + areaB;

        // check collision
        if (ax1<bx2 && ax2>bx1 && ay1<by2 && ay2>by1) {
            // calculate collision box
            int ix1 = ax1 < bx1 ? bx1: ax1;
            int iy1 = ay1 > by1 ? ay1: by1;
            int ix2 = ax2 < bx2 ? ax2: bx2;
            int iy2 = ay2 > by2 ? by2: ay2;
            // take from total
            return sum - findArea(ix1, iy1, ix2, iy2);
        }

        return sum;
    }
}
```
