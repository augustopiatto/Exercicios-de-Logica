def diagonal_difference(arr):
    sum_d1 = 0
    sum_d2 = 0
    for ri, row in enumerate(arr):
        for ci, _ in enumerate(row):
            if ri == ci:
                sum_d1 += arr[ri][ri]
            if (ri + ci) == (len(arr[0]) - 1):
                sum_d2 += arr[ri][ci]
    return abs(sum_d1 - sum_d2)


def test_diagonal_difference():
    input = [
        [11, 2, 4], [4, 5, 6], [10, 8, -12]
    ]
    result = diagonal_difference(input)

    assert result == 15