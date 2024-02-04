def bon_appetit(bill, k, b):
    sum = 0
    for index, food in enumerate(bill):
        if index == k:
            continue
        sum += food

    anna_should_pay = int(sum / 2)
    if anna_should_pay == b:
        return "Bon Appetit"
    else:
        return b - anna_should_pay


def test_bon_appetit():
    index = 8
    charged = 27
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = bon_appetit(input, index, charged)

    assert result == 4
