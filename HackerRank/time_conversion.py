def time_conversion(s):
    am_or_pm = s[-2:]
    minutes_and_seconds = s[2:-2]
    hours = s[:2]
    int_hours = int(hours)
    new_time = ""
    converted_hour = hours

    if int_hours == 12:
        converted_hour = "00" if am_or_pm == "AM" else "12"
    elif am_or_pm == "PM":
        converted_hour = int_hours + 12

    new_time = f"{converted_hour}{minutes_and_seconds}"

    return new_time


def test_time_conversion_1():
    input = "12:40:22AM"

    result = time_conversion(input)

    assert result == "00:40:22"


def test_time_conversion_2():
    input = "12:45:54PM"

    result = time_conversion(input)

    assert result == "12:45:54"


def test_time_conversion_3():
    input = "07:05:45PM"

    result = time_conversion(input)

    assert result == "19:05:45"


def test_time_conversion_4():
    input = "07:05:45AM"

    result = time_conversion(input)

    assert result == "07:05:45"
