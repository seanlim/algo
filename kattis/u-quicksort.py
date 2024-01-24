
# merge sort but count everytime we compare in the merge step

# returns (num_swap, arr)
def count_swap(nums):
    n = len(nums)

    if n <= 1:
        return 0, nums

    mid = len(nums)//2
    left_arr = nums[:mid]
    right_arr = nums[mid:]

    left_count, sorted_left = count_swap(left_arr)
    right_count, sorted_right = count_swap(right_arr)

    result_arr = []

    totalC = left_count + right_count

    left_cur = 0
    right_cur = 0

    left_done, right_done = False, False

    left_len = len(left_arr)

    while (len(result_arr) < n):
        if sorted_left[left_cur] > sorted_right[right_cur]:
            result_arr.append(sorted_right[right_cur])
            totalC += (left_len - left_cur)
            right_cur += 1
            if right_cur == len(sorted_right):
                right_done = True
                break
        else:
            result_arr.append(sorted_left[left_cur])
            left_cur += 1
            if left_cur == len(sorted_left):
                left_done = True
                break

    if left_done:
        for k in range(right_cur, len(sorted_right)):
            result_arr.append(sorted_right[k])
    elif right_done:
        for k in range(left_cur, left_len):
            result_arr.append(sorted_left[k])

    return totalC, result_arr


nums = []
for _ in range(int(input())):   # I use name _ if the variable isn't needed
    nums.append(int(input()))
print(count_swap(nums)[0])
