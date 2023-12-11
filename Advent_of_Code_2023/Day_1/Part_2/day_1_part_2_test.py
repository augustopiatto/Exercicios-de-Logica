from Advent_of_Code_2023.Day_1.day_1_inputs import inputs
from Advent_of_Code_2023.Day_1.Part_2.day_1_part_2_solution import trebuchet


def test_day_1_part_2_simple_test():
    simple_inputs = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]

    sum = trebuchet(simple_inputs)

    assert sum == 142


def test_get_day_1_part_2_answer():
    sum = trebuchet(inputs)

    # resposta descoberta após envio no site
    assert sum == 1
