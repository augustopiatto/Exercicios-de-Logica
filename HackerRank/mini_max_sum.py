def mini_max_sum(arr):
    max = {
        "value": 0,
        "index": -2
    }
    min = {
        "value": pow(10, 9),
        "index": -2
    }
    for index, num in enumerate(arr):
        if num > max["value"]:
            max["value"] = num
            max["index"] = index
        if num < min["value"]:
            min["value"] = num
            min["index"] = index

    sum_max = 0
    sum_min = 0
    for index, num in enumerate(arr):
        if index != max["index"]:
            sum_min += num
        if index != min["index"]:
            sum_max += num

    return (f"{sum_min} {sum_max}")


def test_mini_max_sum():
    input = [5, 5, 5, 5, 5]

    result = mini_max_sum(input)

    assert result == "20 20"
