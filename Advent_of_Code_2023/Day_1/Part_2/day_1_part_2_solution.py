from string import digits


word_to_number = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def extract_numbers(string_with_numbers):
    numbers = []
    for digit in digits:
        idx = string_with_numbers.find(digit)
        if idx != -1:
            numbers.append((idx, digit))
        idx = string_with_numbers.rfind(digit)
        if idx != -1:
            numbers.append((idx, digit))

    for digit, value in word_to_number.items():
        idx = string_with_numbers.find(digit)
        if idx != -1:
            numbers.append((idx, value))
        idx = string_with_numbers.rfind(digit)
        if idx != -1:
            numbers.append((idx, value))

    numbers.sort()
    result = int(f"{numbers[0][1]}{numbers[-1][1]}")

    return result


def trebuchet(inputs):
    sum = 0
    for input in inputs:
        number = extract_numbers(input)
        sum += number

    return sum
