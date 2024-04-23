def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    l, r = min(search_space), max(
        search_space
    )  # could be [0, n], [1, n] etc. Depends on problem

    while l < r:
        mid = l + (r - l) // 2
        if condition(mid):
            r = mid
        else:
            l = mid + 1

    return l
