def kangaroo(x1, v1, x2, v2):
    smallest = {}
    highest = {}
    if x1 < x2:
        smallest["pos"] = x1
        smallest["vel"] = v1
        highest["pos"] = x2
        highest["vel"] = v2
    else:
        smallest["pos"] = x2
        smallest["vel"] = v2
        highest["pos"] = x1
        highest["vel"] = v1

    if smallest["vel"] <= highest["vel"]:
        return "NO"
    while True:
        smallest["pos"] += smallest["vel"]
        highest["pos"] += highest["vel"]
        if smallest["pos"] == highest["pos"]:
            return "YES"
        elif smallest["pos"] > highest["pos"]:
            return "NO"


def test_kangaroo_1():
    input = [0, 2, 5, 3]

    result = kangaroo(input[0], input[1], input[2], input[3])

    assert result == "NO"


def test_kangaroo_2():
    input = [21, 6, 47, 3]

    result = kangaroo(input[0], input[1], input[2], input[3])

    assert result == "NO"


def test_kangaroo_3():
    input = [43, 2, 70, 2]

    result = kangaroo(input[0], input[1], input[2], input[3])

    assert result == "NO"
