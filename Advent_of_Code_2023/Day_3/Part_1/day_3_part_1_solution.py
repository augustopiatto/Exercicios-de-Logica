def _check_if_dot(char):
    return char == "."


def _check_if_symbol(char):
    symbols = {'#', '$', '%', '&', '*', '+', '-', '/', '=', '@'}
    if char in symbols:
        return True
    # try:
    #     int(char)
    # except ValueError:
    #     return True

    return False


def convert_to_position_dict(inputs):
    position_dict = {}
    for pos_x, line in enumerate(inputs):
        for pos_y, char in enumerate(line):
            position_dict[(pos_x, pos_y)] = char
    
    return position_dict


def check_adjacent(position_dict, x, y):
    adjacent_positions = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),
    ]

    for position in adjacent_positions:
        try:
            checked_value = position_dict[(x + position[0], y + position[1])]
        except KeyError:
            continue

        if _check_if_symbol(checked_value):
            return True

    return False


def gear_ratios(inputs):
    num_str = ""
    sum = 0
    part_numbers = []
    is_part_number = False
    lines = inputs.splitlines()
    position_dict = convert_to_position_dict(lines)
    for pos_x, line in enumerate(lines):
        for pos_y, char in enumerate(line):
            is_dot = _check_if_dot(char)
            is_symbol = _check_if_symbol(char)
            if (is_dot or is_symbol) and num_str != "":
                if is_part_number:
                    part_numbers.append(int(num_str))
                    is_part_number = False
                num_str = ""
                continue
            elif not is_dot and not is_symbol:
                num_str += char
                any_adjacent_symbol = check_adjacent(position_dict, pos_x, pos_y)
                if any_adjacent_symbol:
                    is_part_number = True
                else:
                    continue

    for number in part_numbers:
        sum += number

    return sum
