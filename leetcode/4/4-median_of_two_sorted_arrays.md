## Solve by merging and sorting

```ts
function getMedianOfArray(sortedNums: number[], numOfItems: number): number {
  if (numOfItems % 2 == 0) {
    const med1 = sortedNums[numOfItems / 2 - 1];
    const med2 = sortedNums[numOfItems / 2];
    return (med1 + med2) / 2;
  }
  return sortedNums[(numOfItems - 1) / 2];
}
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const numOfItems = nums1.length + nums2.length;
  if (numOfItems == 0) {
    return 0;
  }
  if (nums1.length === 0) {
    return getMedianOfArray(nums2, numOfItems);
  }
  if (nums2.length === 0) {
    return getMedianOfArray(nums1, numOfItems);
  }

  if (nums2[0] >= nums1[nums1.length]) {
    return getMedianOfArray(nums1.concat(nums2), numOfItems);
  }
  if (nums1[0] >= nums2[nums2.length]) {
    return getMedianOfArray(nums2.concat(nums1), numOfItems);
  }
  const sortedArr = nums1.concat(nums2).sort((a, b) => a - b);
  return getMedianOfArray(sortedArr, numOfItems);
}
```

## Constructive solve

```ts
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const combined = [];
  const numOfItems = nums1.length + nums2.length;

  if (numOfItems == 0) {
    return 0;
  }

  const averagesNext = numOfItems % 2 === 0;
  const targetCount = averagesNext ? numOfItems / 2 : (numOfItems - 1) / 2;

  if (nums1.length === 0) {
    return averagesNext
      ? (nums2[targetCount - 1] + nums2[targetCount]) / 2
      : nums2[targetCount];
  }
  if (nums2.length === 0) {
    return averagesNext
      ? (nums1[targetCount - 1] + nums1[targetCount]) / 2
      : nums1[targetCount];
  }

  while (combined.length <= targetCount) {
    if (nums1.length === 0) {
      combined.push(nums2.shift());
      continue;
    }
    if (nums2.length === 0) {
      combined.push(nums1.shift());
      continue;
    }
    if (nums1[0] <= nums2[0]) {
      combined.push(nums1.shift());
    } else {
      combined.push(nums2.shift());
    }
  }
  if (averagesNext) {
    return (combined.pop() + combined.pop()) / 2;
  }
  return combined.pop();
}
```
