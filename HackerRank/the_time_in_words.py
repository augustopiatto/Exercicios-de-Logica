def time_in_words(hours, minutes):
    hours_to_words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
    }
    minutes_to_words = {
        1: 'one minute',
        2: 'two minutes',
        3: 'three minutes',
        4: 'four minutes',
        5: 'five minutes',
        6: 'six minutes',
        7: 'seven minutes',
        8: 'eight minutes',
        9: 'nine minutes',
        10: 'ten minutes',
        11: 'eleven minutes',
        12: 'twelve minutes', 13: "thirteen minutes", 14: "fourteen minutes",
        15: "quarter", 16: "sixteen minutes", 17: "seventeen minutes", 18:
        "eighteen minutes", 19: "nineteen minutes", 20: "twenty minutes", 21: "twenty one minute",
        22: "twenty two minutes", 23: "twenty three minutes", 24: "twenty four minutes", 25: "twenty five minutes",
        26: "twenty six minutes", 27: "twenty seven minutes", 28: "twenty eight minutes", 29: "twenty nine minutes", 30: "half"}
    if minutes == 0:
        return hours_to_words[hours] + " o' clock"
    elif 0 < minutes <= 30:
        return minutes_to_words[minutes] + " past " + hours_to_words[hours]
    else:
        minutes_left = 60 - minutes
        if minutes == 45:
            return "quarter to " + hours_to_words[hours + 1]
        return minutes_to_words[minutes_left] + " to " + hours_to_words[hours + 1]


def test_time_in_words_1():
    result = time_in_words(5, 47)

    assert result == 'thirteen minutes to six'


def test_time_in_words_2():
    result = time_in_words(5, 0)

    assert result == "five o' clock"


def test_time_in_words_3():
    result = time_in_words(5, 21)

    assert result == "twenty one minute past five"


def test_time_in_words_4():
    result = time_in_words(7, 29)

    assert result == "twenty nine minutes past seven"


def test_time_in_words_5():
    result = time_in_words(5, 30)

    assert result == "half past five"


def test_time_in_words_6():
    result = time_in_words(5, 45)

    assert result == "quarter to six"
