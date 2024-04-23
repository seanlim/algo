import random

def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]

    # move pivot value to the end so it is out of the way
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    s_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[s_index] = arr[s_index], arr[i]
            s_index += 1

    # move pivot value back
    arr[right], arr[s_index] = arr[s_index], arr[right]
    return s_index

def quickselect(arr, left, right, k):
    if left == right:
        return arr[left]

    # select a random pivot
    pivot_index = random.randint(left, right)
    pivot_index = partition(arr, left, right, pivot_index)

    # select next partition (binary search)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, left, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, right, k)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
k = 4
kth_smallest = quickselect(arr, 0, len(arr) - 1, k)
print(f"The {k}th smallest element is: {kth_smallest}")