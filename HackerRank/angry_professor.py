def angry_professor(threshold, arrival_times):
    on_time_students = 0
    for arrival_time in arrival_times:
        if arrival_time <= 0:
            on_time_students += 1

    if on_time_students >= threshold:
        return "NO"
    return "YES"


def test_angry_professor_1():
    threshold = 4
    arrival_times = [-93, -86, 49, -62, -90, -63, 40, 72, 11, 67]

    result = angry_professor(threshold, arrival_times)

    assert result == "NO"


def test_angry_professor_2():
    threshold = 10
    arrival_times = [23, -35, -2, 58, -67, -56, -42, -73, -19, 37]

    result = angry_professor(threshold, arrival_times)

    assert result == "YES"


def test_angry_professor_3():
    threshold = 9
    arrival_times = [13, 91, 56, -62, 96, -5, -84, -36, -46, -13]

    result = angry_professor(threshold, arrival_times)

    assert result == "YES"


def test_angry_professor_4():
    threshold = 8
    arrival_times = [45, 67, 64, -50, -8, 78, 84, -51, 99, 60]

    result = angry_professor(threshold, arrival_times)

    assert result == "YES"


def test_angry_professor_5():
    threshold = 7
    arrival_times = [26, 94, -95, 34, 67, -97, 17, 52, 1, 86]

    result = angry_professor(threshold, arrival_times)

    assert result == "YES"
