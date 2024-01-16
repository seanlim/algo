num_sets = int(input())


# insertion sort but count everytime we swap

def count_steps(set_num, arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            count += 1
            j -= 1
        arr[j+1] = key
    print(f"{set_num} {count}")


for _ in range(num_sets):
    set = [int(x) for x in input().split()]
    count_steps(set[0], set[1:])

# 1 0
# 2 190
# 3 19
# 4 171
