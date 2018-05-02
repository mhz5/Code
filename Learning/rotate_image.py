def rotate(mat):
    n = len(mat)

    for ring in range(n / 2):
        for i in range(ring, n - ring - 1):
            four_swap(ring, i, n, mat)


def rotate_coords(x, y, n):
    return y, n - x - 1


def four_swap(x, y, n, mat):
    prev_val = mat[x][y]
    for i in range(4):
        x2, y2 = rotate_coords(x, y, n)
        next_val = mat[x2][y2]
        mat[x2][y2] = prev_val

        x, y = x2, y2
        prev_val = next_val


t1 = [
         [5, 1, 9, 11],
         [2, 4, 8, 10],
         [13, 3, 6, 7],
         [15,14,12,16]
     ]

rotate(t1)
print t1

