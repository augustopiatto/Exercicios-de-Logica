import math


def squares(a, b):
    sqrt_first_number = 0
    sqrt_last_number = 0
    for number in range(a, b + 1):
        if math.sqrt(number) % 1 == 0:
            sqrt_first_number = math.ceil(math.sqrt(a))
            break
    number = b
    while number >= a:
        if math.sqrt(number) % 1 == 0:
            sqrt_last_number = math.floor(math.sqrt(b))
            break
        number -= 1

    square_integers_qtt = len(range(sqrt_first_number, sqrt_last_number + 1)) if sqrt_first_number and sqrt_last_number else 0
    
    return square_integers_qtt


def test_squares_1():
    result = squares(3, 9)

    assert result == 2


def test_squares_2():
    result = squares(17, 24)

    assert result == 0


def test_squares_3():
    result = squares(4, 4)

    assert result == 1
