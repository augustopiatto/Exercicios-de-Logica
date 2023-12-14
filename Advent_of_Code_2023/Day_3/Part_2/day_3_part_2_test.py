from Advent_of_Code_2023.Day_3.day_3_inputs import inputs
from Advent_of_Code_2023.Day_3.Part_2.day_3_part_2_solution import gear_ratios


def test_day_3_part_2_simple_test():
    simple_inputs = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    sum = gear_ratios(simple_inputs)

    assert sum == 467835


def test_get_day_3_part_2_answer():
    sum = gear_ratios(inputs)

    # resposta descoberta após envio no site
    assert sum == 91622824
