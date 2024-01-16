import sys

# binary search

l = 1
r = 1000

for _ in range(10):
    mid = l + ((r-l) // 2)
    print(mid, flush=True)
    status = input()
    if status == "correct":
        sys.exit(0)
    if status == "lower":
        r = mid - 1
    if status == "higher":
        l = mid + 1
sys.exit(0)
