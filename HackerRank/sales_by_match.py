def sock_merchant(n, ar):
    # Write your code here
    import math

    sock_dict = {}
    for sock in ar:
        if sock_dict.get(sock):
            sock_dict[sock] += 1
        else:
            sock_dict[sock] = 1

    result = 0
    for key in sock_dict.keys():
        if sock_dict[key] >= 2:
            result += math.floor(sock_dict[key] / 2)

    return result


def test_sock_merchant():
    input = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]

    result = sock_merchant(len(input), input)

    assert result == 9
