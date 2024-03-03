def bigger_is_greater(w):
    list_w = list(w)
    w_dict = {}

    for i in range(len(w) - 1, 0, -1):
        if ord(w[i]) not in w_dict:
            w_dict[ord(list_w[i])] = i
        if ord(list_w[i]) > ord(list_w[i-1]):
            swap = ord(list_w[i - 1]) + 1
            while swap not in w_dict:
                swap += 1
            j_index = w_dict[swap]
            list_w[i-1], list_w[j_index] = list_w[j_index], list_w[i-1]
            list_w[i:] = list_w[i:][::-1]
            return ''.join(list_w)

    return 'no answer'


def test_bigger_is_greater():
    result = bigger_is_greater("dkhc")

    assert result == "hcdk"
