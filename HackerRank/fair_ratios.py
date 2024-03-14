def fair_ratios(B):
    given_loaves = 0
    for index in range(len(B)):
        if B[index] % 2 != 0:
            if (index + 1) < len(B):
                B[index] += 1
                B[index + 1] += 1
                given_loaves += 2
            else:
                return "NO"

    return given_loaves


def test_fair_ratios():
    result = fair_ratios([2, 3, 4, 5, 6])

    assert result == 4
