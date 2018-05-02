LAND = 1

def size_of_largest_island(arr):
    m = len(arr)
    n = len(arr[0])
    seen = [[False for _ in range(n)]
            for _ in range(m)]

    max_size = 0
    for r, row in enumerate(arr):
        for c, val in enumerate(row):
            size = dfs(arr, seen, r, c)
            max_size = max(max_size, size)

    return max_size


def dfs(arr, seen, x, y):
    is_out_of_bounds = (x < 0 or x >= len(arr) or
                        y < 0 or y >= len(arr[0]))

    if is_out_of_bounds or seen[x][y]:
        return 0

    seen[x][y] = True

    if arr[x][y] != LAND:
        return 0

    increments = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    size = 1
    for (xi, yi) in increments:
        size += dfs(arr, seen, x + xi, y + yi)

    return size


arr = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
]
print(size_of_largest_island(arr))
