lis = []
neighbours_list = []
for i in range(0, 32):
    neighbours_list.append([])


def find_direction(x, y):
    if 0 <= x <= 1 and 0 <= y <= 1:
        return [-1, -1]
    if 0 <= x <= 1 and y >= 10:
        return [-1, 1]
    if 0 <= x <= 1:
        return [-1, 0]
    if x > 5 and 0 <= y <= 1:
        return [1, -1]
    if 0 <= y <= 1:
        return [0, -1]
    if x > 5 and y >= 10:
        return [1, 1]
    if y >= 10:
        return [0, 1]
    if x > 5:
        return [1, 0]
    return [0, 0]


def neighbourCalculation():
    for char in range(0, 32):
        lis.append([])

    neighbour_utils = [
        ['q', 'r', '2', '3', '6', '7', 'k', 'm', 'q', 'r', '2', '3'],
        ['n', 'p', '0', '1', '4', '5', 'h', 'j', 'n', 'p', '0', '1'],
        ['y', 'z', 'b', 'c', 'f', 'g', 'u', 'v', 'y', 'z', 'b', 'c'],
        ['w', 'x', '8', '9', 'd', 'e', 's', 't', 'w', 'x', '8', '9'],
        ['q', 'r', '2', '3', '6', '7', 'k', 'm', 'q', 'r', '2', '3'],
        ['n', 'p', '0', '1', '4', '5', 'h', 'j', 'n', 'p', '0', '1'],
        ['y', 'z', 'b', 'c', 'f', 'g', 'u', 'v', 'y', 'z', 'b', 'c'],
        ['w', 'x', '8', '9', 'd', 'e', 's', 't', 'w', 'x', '8', '9']
    ]
    index = -1
    for row in range(2, 6):
        for col in range(2, 10):
            index = index + 1
            for curr_row in range(0, 8):
                for curr_col in range(0, 12):
                    if row == curr_row and col == curr_col:
                        continue
                    dx = abs(row - curr_row)
                    dy = abs(col - curr_col)
                    direction = find_direction(curr_row, curr_col)
                    lis[index].append((max(dx, dy), min(dx, dy), neighbour_utils[curr_row][curr_col], direction))

    for char in range(0, 32):
        lis[char].sort()
        for j in range(len(lis[char])):
            neighbours_list[char].append([lis[char][j][2], lis[char][j][3]])


neighbourCalculation()
