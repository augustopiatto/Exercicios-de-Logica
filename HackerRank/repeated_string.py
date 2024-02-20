def repeated_string(s, n):
    a_counter = 0
    for letter in s:
        if letter == 'a':
            a_counter += 1

    repeated_string_qtt = n // len(s)
    a_counter = a_counter * repeated_string_qtt
    letters_missing = n % len(s)

    if letters_missing:
        for letter in s[:letters_missing]:
            if letter == 'a':
                a_counter += 1

    return a_counter


def test_repeated_string():
    result = repeated_string('aab', 882787)

    assert result == 588525
