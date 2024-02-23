NORTH = "N"
SOUTH = "S"
BOTH = "B"

TOP = 0
BOTTOM = 1

crossings = input()
n = len(crossings)


# realise that we can think of the map as a grid with n rows and 2 columns

# it is very costly to keep re-calculating from right to left, so we want to memoise the number of crosses needed to get to (x, y)
dp = {}

# cross_to calculates the cost of crossing from x-1 to x


def cross_to(x: int, y: int) -> int:
    crossing = crossings[x-1]
    if crossing == BOTH:
        return 1
    # if we are on the top, check for crossings above
    if y == TOP:
        return 1 if crossing == NORTH else 0
    # if we are on the bottom, check for crossings below
    return 1 if crossing == SOUTH else 0


# solve is a recursive function to calculate the number of crosses needed to get to (x, y)
def solve(x: int, y: int) -> int:
    # base case
    if x == 0:
        return 0 if y == TOP else 1

    # check to see if we already figured this out, and don't recurse if we did
    if (x, y) in dp:
        return dp[(x, y)]

    # solve for the previous column and add the number of crosses neeeded to get to the current position from the previous column.
    # realise that there is a horizontal road— going between top and bottom incurs a cross as well
    cost = min(
        solve(x-1, TOP) + cross_to(x, TOP) + (1 if y == BOTTOM else 0),
        solve(x-1, BOTTOM) + cross_to(x, BOTTOM) + (1 if y == TOP else 0))

    # memoise solution
    dp[(x, y)] = cost
    return cost


print(solve(n, TOP))
