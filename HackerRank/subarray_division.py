def birthday(s, d, m):
    result = 0
    for array_pos in range(0, len(s) - m + 1):
        first_number = s[array_pos]
        target = d - first_number
        numbers_sum = [first_number]
        if m == 1 and target == 0:
            return 1

        for index in range(array_pos + 1, array_pos + m):
            second_number = s[index]
            target = target - second_number
            numbers_sum.append(second_number)
            if len(numbers_sum) == m and target == 0:
                result += 1

    return result


def test_birthday_1():
    chocolate = [2, 2, 1, 3, 2]
    day_birthday = 4
    month_birthday = 2

    result = birthday(chocolate, day_birthday, month_birthday)

    assert result == 2


def test_birthday_2():
    chocolate = [1, 1, 1, 1, 1]
    day_birthday = 3
    month_birthday = 2

    result = birthday(chocolate, day_birthday, month_birthday)

    assert result == 0


def test_birthday_3():
    chocolate = [4]
    day_birthday = 4
    month_birthday = 1

    result = birthday(chocolate, day_birthday, month_birthday)

    assert result == 1


def test_birthday_4():
    chocolate = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
    day_birthday = 18
    month_birthday = 7

    result = birthday(chocolate, day_birthday, month_birthday)

    assert result == 3
