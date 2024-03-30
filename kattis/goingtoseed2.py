import sys

N = int(input())

# takes in two ranges, asks question and returns answer in integer value
def check(range1, range2):
    l1, r1 = range1
    l2, r2 = range2
    print(f'Q {l1 + 1} {r1 + 1} {l2 + 1} {r2 + 1}')
    sys.stdout.flush()
    return int(input().replace(" ", ""), 2)


def answer(t):
    print(f'A {t + 1}')
    sys.exit()


def search(start_index, n):
    # print(f's={start_index}, n={n}')

    # realise that binary search is not sufficient as log_2 10^9 is ~29
    # we need to do 4-way search
    part_size = round(n / 4)

    # define two searchers s1 and s2
    # we want s1 to cover p1 and p2, s2 to cover p2 and p3
    s1 = [start_index,  start_index + (2 * part_size - 1)]
    s2 = [start_index + part_size, start_index + (3 * part_size-1)]

    if (part_size == 1):
        s1 = [start_index,  start_index + 1]
        s2 = [start_index + 1, start_index + 2]

    # base cases
    if (n == 1):
        answer(start_index)
    if (n == 2):
        s1 = [start_index, start_index]
        s2 = [start_index+1, start_index+1]
        answer(start_index + (0 if check(s1, s2) == 2 else 1))
    elif (n == 3):
        s1 = [start_index, start_index+1]
        s2 = [start_index+1, start_index+2]
        answer({1: start_index + 2,
                2: start_index,
                3: start_index + 1}[check(s1, s2)])

    # check next partition to search
    check_result = check(s1, s2)

    # base case
    if n == 4:
        answer(start_index + [2, 3, 1, 0].index(check_result))

    # we need to carry on searching
    next_search_index = 0

    if check_result == 2:  # first partition
        # realise that if s1.start and end are next to each other,
        # we already found the answer
        if s1[1] - s1[0] == 1:
            answer(s1[0])

        # search first partition
        next_search_index = s1[0]

    elif check_result == 3:  # second parition
        # realise that if s1.end and s2.start are the same,
        # we already found the answer
        if s1[1] == s2[0]:
            answer(s1[1])

        # search second partition
        next_search_index = s2[0]

    elif check_result == 1:  # third partition
        # similar to before, if s2.start end end are next to each other,
        # we have our answer
        if s2[1] - s2[0] == 1:
            answer(s2[1])

        # search third partition
        next_search_index = s1[1] + 1

    elif check_result == 0:  # fourth partition
        # If the next element after s2.end is the right bound,
        # we have our answer
        if N == s2[1] + 1:
            answer(N)

        # search last partition
        next_search_index = s2[1] + 1
        # the partition size is not regular, and so we should calculate it
        part_size = n - (3 * part_size)

    # increase search space to the left
    next_search_index -= 1

    # if we have hit the left boundary, resize and continue.
    if next_search_index < 0:
        next_search_index = 0
        # increase search space to the right
        part_size += 1
    else:
        # increase search space to the left
        part_size += 1
        # increase search space to the right
        part_size += 1

    # if we have hit the right boundary, resize and continue
    if next_search_index + part_size >= N:
        part_size = N - next_search_index

    return search(next_search_index,
                  part_size)

search(0, N)
