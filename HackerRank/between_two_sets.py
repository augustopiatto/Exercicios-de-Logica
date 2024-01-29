def get_total_x(first_array, second_array):
    # Write your code here
    highest_number_first_array = 0
    lowest_number_second_array = 101
    for number in first_array:
        if number > highest_number_first_array:
            highest_number_first_array = number

    for number in second_array:
        if number < lowest_number_second_array:
            lowest_number_second_array = number

    result = []
    for ideal_number in range(highest_number_first_array, lowest_number_second_array + 1):
        include_ideal_number = True
        for num in first_array:
            include_ideal_number = include_ideal_number and ideal_number % num == 0

        if include_ideal_number:
            for num in second_array:
                include_ideal_number = include_ideal_number and num % ideal_number == 0

        if include_ideal_number:
            result.append(ideal_number)

    return len(result)


def test_get_total_x_1():
    input1 = [2, 4]
    input2 = [16, 32, 96]

    result = get_total_x(input1, input2)

    assert result == 3


def test_get_total_x_2():
    input1 = [2]
    input2 = [20, 30, 12]

    result = get_total_x(input1, input2)

    assert result == 1
