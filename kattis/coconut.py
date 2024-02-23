s, n = map(lambda x: int(x), input().split(" "))

# (id, FOLDED)
FOLDED = "FOLDED"

# (id, HAND, lives_int)
HAND = "HAND"

players = []

for i in range(n):
    players.append((i, FOLDED))

victim = 0
while len(players) > 1:
    victim = (s + victim - 1) % len(players)
    victim_id = players[victim][0]
    victim_state = players[victim][1]
    if victim_state == FOLDED:
        # spawn hands
        players[victim:victim+1] = ((victim_id, HAND, 2), (victim_id, HAND, 2))
    if victim_state == HAND:
        hand_lives = players[victim][2]
        if hand_lives > 1:
            # spill
            players[victim] = (victim_id, HAND, hand_lives-1)
            victim += 1
        else:
            # kill
            del players[victim]

print(players[0][0] + 1)
