# import pytest

def palavrao():
    while True:
        try:
            palavra = input()
        except EOFError:
            break

        print("palavrao" if len(palavra) >= 10 else "palavrinha")

# TODO

# pytest.mark.parametrize("input, output", [(["3 2"], "Total: R$ 10.00")])
# @parametrize(input, output)
# def test:
#     palavrao()
