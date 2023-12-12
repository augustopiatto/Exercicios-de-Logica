def _check_if_dot(char):
    if char == ".":
        return False


def _check_if_symbol(char):
    try:
        int(char)
    except ValueError:
        return True


def get_symbols_positions(inputs):
    symbol_dict = {}
    for pos_x, line in enumerate(inputs):
        for pos_y, char in enumerate(line):
            _ = _check_if_dot(char)
            is_symbol = _check_if_symbol(char)
            if is_symbol:
                symbol_dict[(pos_x, pos_y)] = True
    
    return symbol_dict


def check_adjacent(x, y):
    # continuar aqui amanhã
    return


def gear_ratios(inputs):
    lines = inputs.splitlines()
    symbol_dict = get_symbols_positions(lines)
    for pos_x, line in enumerate(lines):
        for pos_y, char in enumerate(line):
            num_str = ""
            is_dot = _check_if_dot(char)
            is_symbol = _check_if_symbol(char)
            if is_dot:
                num_str = ""
                continue
            if not is_symbol:
                num_str += char
                check_adjacent(pos_x, pos_y)

    return "qualquer coisa, pra quebrar o teste"
