def encryption(s):
    import math

    no_space = []
    for letter in s:
        if letter != " ":
            no_space.append(letter)
    string_length = len(no_space)
    rows = math.floor(math.sqrt(string_length))
    columns = math.ceil(math.sqrt(string_length))
    if rows * columns < string_length:
        if rows != columns:
            rows += 1
        else:
            columns += 1

    rows_and_columns = []
    row = []
    for index, letter in enumerate(no_space):
        row.append(letter)
        if (index + 1) % columns == 0 or index + 1 == string_length:
            rows_and_columns.append(row)
            row = []

    result = ""
    for index_c in range(columns):
        for index_r in range(rows):
            if len(rows_and_columns[index_r]) >= index_c + 1:
                result += rows_and_columns[index_r][index_c]
        if index_c + 1 != columns:
            result += " "

    return result


def test_encryption_1():
    result = encryption("have a nice day")

    assert result == "hae and via ecy"


def test_encryption_2():
    result = encryption("feedthedog")

    assert result == "fto ehg ee dd"


def test_encryption_3():
    result = encryption("roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp")

    assert result == "rlyzatp oxqkps quthvx fyegue qxrvdp ejinnr yfzgzf"
