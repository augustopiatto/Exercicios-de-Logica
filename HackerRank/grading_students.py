def grading_students(grades):
    if len(grades) < 1 or len(grades) > 60:
        return

    result = []
    for grade in grades:
        if grade < 0 or grade > 100:
            continue
        missing = grade % 5
        if grade >= 38 and missing >= 3:
            result.append(grade - missing + 5)
        else:
            result.append(grade)

    return result


def test_grading_students():
    input = [84, 94, 21, 0, 18, 100, 18, 62, 30, 61, 53, 0, 43, 2, 29, 53, 61, 40, 14, 4, 29,
             98, 37, 23, 46, 9, 79, 62, 20, 38, 51, 99, 59, 47, 4, 86, 61, 68, 17, 45, 6, 1, 95, 95]

    result = grading_students(input)

    assert result == [85, 95, 21, 0, 18, 100, 18, 62, 30, 61, 55, 0, 45, 2, 29, 55, 61, 40, 14, 4,
                      29, 100, 37, 23, 46, 9, 80, 62, 20, 40, 51, 100, 60, 47, 4, 86, 61, 70, 17, 45, 6, 1, 95, 95]
