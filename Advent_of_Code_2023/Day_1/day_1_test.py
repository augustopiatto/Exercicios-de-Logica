from day_1_inputs import inputs
from day_1_solution import trebuchet


def test_day_1_simple_test():
    simple_inputs = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    sum = trebuchet(simple_inputs)

    assert sum == 142


def test_get_day_1_answer():
    sum = trebuchet(inputs)

    # resposta descoberta após envio no site
    assert sum == 54390
