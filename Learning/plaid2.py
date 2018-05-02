# x, y < 100

SPACE = ' '
DIMENSION = 100


def draw_ascii_art(data_file):
    f = open(data_file, 'r')
    art = [[SPACE] * DIMENSION for _ in range(DIMENSION)]
    for line in f:
        if is_valid_line(line):
            nums = line[1:len(line) - 2]  # Remove trailing '\n'
            x, y, char_val = [int(x) for x in nums.split(',')]
            art[x][y] = chr(char_val)
    print_array(art)


def print_array(arr):
    for row in arr:
        print(''.join(row))







def is_valid_line(line):
    return True

data_file = 'data_file.txt'
draw_ascii_art(data_file)
