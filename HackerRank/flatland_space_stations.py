import math


def flatland_space_stations(n, c):
    max_distance = 0
    c.sort()
    distance_to_first = math.floor(c[0])
    if distance_to_first > max_distance:
        max_distance = distance_to_first
    distance_to_last = math.floor(((n - 1) - c[-1]))
    if distance_to_last > max_distance:
        max_distance = distance_to_last
    for index in range(0, len(c) - 1):
        distance = math.floor((c[index + 1] - c[index]) / 2)
        if distance > max_distance:
            max_distance = distance

    return max_distance


def test_flatland_space_stations():
    cities_qtt = 20
    space_stations = [13, 11, 1, 10, 6]
    result = flatland_space_stations(cities_qtt, space_stations)

    assert result == 6
