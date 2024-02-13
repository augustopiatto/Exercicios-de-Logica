def save_the_prisoner(prisoner_qtt, sweets_qtt, start_position):
    position = (sweets_qtt + start_position - 1) % prisoner_qtt
    if position == 0:
        return prisoner_qtt
    else:
        return position


def test_save_the_prisoner_1():
    prisoner_qtt = 7
    sweets_qtt = 19
    current_chair = 2

    result = save_the_prisoner(prisoner_qtt, sweets_qtt, current_chair)

    assert result == 6


def test_save_the_prisoner_2():
    prisoner_qtt = 352926151
    sweets_qtt = 380324688
    current_chair = 94730870

    result = save_the_prisoner(prisoner_qtt, sweets_qtt, current_chair)

    assert result == 122129406


def test_save_the_prisoner_3():
    prisoner_qtt = 7
    sweets_qtt = 7
    current_chair = 2

    result = save_the_prisoner(prisoner_qtt, sweets_qtt, current_chair)

    assert result == 1


def test_save_the_prisoner_4():
    prisoner_qtt = 9
    sweets_qtt = 7
    current_chair = 8

    result = save_the_prisoner(prisoner_qtt, sweets_qtt, current_chair)

    assert result == 5


def test_save_the_prisoner_5():
    prisoner_qtt = 9
    sweets_qtt = 7
    current_chair = 1

    result = save_the_prisoner(prisoner_qtt, sweets_qtt, current_chair)

    assert result == 7
