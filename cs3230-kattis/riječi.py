# represent number of As and Bs as a tuple (no. A, no. B)
# solve bottom up
arr = [None] * 46
k = int(input(""))
for x in range(k+1):
    if x == 0:
        arr[x] = (1, 0)
        continue
    if x == 1:
        arr[x] = (0, 1)
        continue
    arr[x] = tuple(map(sum, zip(arr[x-1], arr[x-2])))
a, b = arr[k]
print(f"{a} {b}")
