from Advent_of_Code_2023.Day_2.day_2_inputs import inputs
from Advent_of_Code_2023.Day_2.Part_1.day_2_part_1_solution import cube_conundrum


def test_day_2_part_1_simple_test():
    simple_inputs = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    sum = cube_conundrum(simple_inputs)

    assert sum == 8


def test_get_day_2_part_1_answer():
    sum = cube_conundrum(inputs)

    # resposta descoberta após envio no site
    assert sum == 2169
