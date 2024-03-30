import sys; input = sys.stdin.readline

n_houses, n_friends = [int(i) for i in input().split(" ")]
house_anger = [int(i) for i in input().split(" ")]
friend_motivation = [int(i) for i in input().split(" ")]

n = max(friend_motivation)
ans = [0] * n

house_anger.sort()
ans[0] = house_anger[0]

for i in range(1, n+1):
  ans[i-1] = ans[i-2] + house_anger[i-1]

for i in friend_motivation:
  print(ans[i-1])
