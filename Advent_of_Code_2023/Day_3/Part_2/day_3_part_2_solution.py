from string import digits


def _check_adjacencies(numbers, xg, yg):
    adjacent_numbers = []
    adjs = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    for number, positions in numbers:
        for pos_x, pos_y in adjs:
            if (xg + pos_x, yg + pos_y) in positions:
                adjacent_numbers.append(int(number))
                break

    return adjacent_numbers


def gears_list(lines, gears):
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '*':
                gears.append((i, j))


def gear_ratios(inputs):
    sum = 0
    gears = []
    numbers = []
    num_str = ""
    positions = []
    lines = inputs.splitlines()

    gears_list(lines, gears)
    for pos_x, line in enumerate(lines):
        for pos_y, char in enumerate(line):
            if num_str and char not in digits:
                numbers.append((num_str, list(positions)))
                num_str = ""
                positions = []
            if char in digits:
                num_str += char
                positions.append((pos_x, pos_y))

    for gear in gears:
        adjacent_numbers_qtt = _check_adjacencies(numbers, *gear)
        if len(adjacent_numbers_qtt) == 2:
            sum += (adjacent_numbers_qtt[0] * adjacent_numbers_qtt[1])

    return sum
