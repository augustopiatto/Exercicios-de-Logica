import re


def extract_numbers(string_with_numbers):
    numbers_pattern = re.compile(r'\d')
    numbers_found = numbers_pattern.findall(string_with_numbers)
    first_number = numbers_found[0]
    last_number = numbers_found[-1]
    final_number = int(first_number + last_number)

    return final_number


def trebuchet(inputs):
    sum = 0
    for input in inputs:
        number = extract_numbers(input)
        sum += number

    return sum
