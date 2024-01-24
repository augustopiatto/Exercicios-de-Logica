def plus_minus(arr):
    arr_len = len(arr)
    if 0 > arr_len <= 101:
        return
    
    sum_pos = 0
    sum_neg = 0
    sum_zero = 0
    for num in arr:
        if -100 > num <= 100:
            continue
        if num > 0:
            sum_pos += 1
        elif num < 0:
            sum_neg += 1
        else:
            sum_zero += 1
    return ["{:.6f}".format(sum_pos / arr_len), "{:.6f}".format(sum_neg / arr_len), "{:.6f}".format(sum_zero / arr_len)]


def test_plus_minus():
    input = [0, -67, -74, -38, -72, -53, 0, -13, -95, -91, -100, -59, 0, -10, -68, -71, -62, -21, 0, -42, -57, -16, -66, -23, 0, -80, -63, -68, -65, -71, 0, -71, -15, -32, -26, -8, 0, -6, -51, -87, -19, -71, 0, -93, -26, -35, -56, -89, 0, -21, -74, -39, -57, -8, 0, -69, -29, -24, -99, -53, 0, -65, -42, -72, -18, -4, 0, -73, -46, -63, -78, -87]

    result = plus_minus(input)

    assert result == ["0.000000", "0.833333", "0.166667"]
