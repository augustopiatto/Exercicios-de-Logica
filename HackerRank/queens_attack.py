def queens_attack_not_optimized(n, k, r_q, c_q, obstacles):
    possible_attacks = 0
    # pra cima
    for step in range(1, n):
        if r_q + step > n or [r_q + step, c_q] in obstacles:
            break
        possible_attacks += 1
    # pra baixo
    for step in range(1, n):
        if r_q - step < 1 or [r_q - step, c_q] in obstacles:
            break
        possible_attacks += 1
    # pra direta
    for step in range(1, n):
        if c_q + step > n or [r_q, c_q + step] in obstacles:
            break
        possible_attacks += 1
    # pra esquerda
    for step in range(1, n):
        if c_q - step < 1 or [r_q, c_q - step] in obstacles:
            break
        possible_attacks += 1
    # pra diagonal cima direita
    for step in range(1, n):
        if r_q + step > n or c_q + step > n or [r_q + step, c_q + step] in obstacles:
            break
        possible_attacks += 1
    # pra diagonal cima esquerda
    for step in range(1, n):
        if r_q + step > n or c_q - step < 1 or [r_q + step, c_q - step] in obstacles:
            break
        possible_attacks += 1
    # pra diagonal baixo direita
    for step in range(1, n):
        if r_q - step < 1 or c_q + step > n or [r_q - step, c_q + step] in obstacles:
            break
        possible_attacks += 1
    # pra diagonal baixo esquerda
    for step in range(1, n):
        if r_q - step < 1 or c_q - step < 1 or [r_q - step, c_q - step] in obstacles:
            break
        possible_attacks += 1

    return possible_attacks


def test_queens_attack_not_optimized():
    board_size = 5
    obstacles_qtt = 3
    queen_row = 4
    queen_column = 3
    obstacles_positions = [[5, 5], [4, 2], [2, 3]]
    result = queens_attack_not_optimized(board_size, obstacles_qtt,
                                         queen_row, queen_column, obstacles_positions)

    assert result == 10


def diagonal_top_right(obstacle_row, obstacle_column, queen_row, queen_column):
    return (obstacle_row - queen_row) == (obstacle_column - queen_column)


def diagonal_top_left(obstacle_row, obstacle_column, queen_row, queen_column):
    return (obstacle_row - queen_row) == -(obstacle_column - queen_column)


def diagonal_bottom_right(obstacle_row, obstacle_column, queen_row, queen_column):
    return -(obstacle_row - queen_row) == (obstacle_column - queen_column)


def diagonal_bottom_left(obstacle_row, obstacle_column, queen_row, queen_column):
    return (obstacle_row - queen_row) == (obstacle_column - queen_column)


def queens_attack_optimized(board_size, obstacles_qtt,
                            queen_row, queen_column, obstacles_positions):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, -1), (1, 1), (-1, -1), (-1, 1)]
    possible_attacks = 0

    obstacles_set = set(map(tuple, obstacles_positions))

    for direction in directions:
        currX, currY = queen_row + direction[0], queen_column + direction[1]
        blocked = False

        while 1 <= currX <= board_size and 1 <= currY <= board_size and not blocked:
            if (currX, currY) in obstacles_set:
                blocked = True
            else:
                possible_attacks += 1

            currX += direction[0]
            currY += direction[1]

    return possible_attacks


def test_queens_attack_optimized_1():
    board_size = 5
    obstacles_qtt = 3
    queen_row = 4
    queen_column = 3
    obstacles_positions = [[5, 5], [4, 2], [2, 3]]

    result = queens_attack_optimized(board_size, obstacles_qtt,
                                     queen_row, queen_column, obstacles_positions)

    assert result == 10


def test_queens_attack_optimized_2():
    board_size = 100000
    obstacles_qtt = 100000
    queen_row = 6453
    queen_column = 3654
    path = "HackerRank/queens_attack.txt"
    with open(path, "r") as file:
        lines = file.readlines()
    obstacles_positions = [
        (int(line.split()[0]), int(line.split()[1])) for line in lines]

    result = queens_attack_optimized(board_size, obstacles_qtt,
                                     queen_row, queen_column, obstacles_positions)

    assert result == 307303
