import pytest


def media_2():
    while True:
        try:
            nota_a = float(input())
            nota_b = float(input())
            nota_c = float(input())
        except EOFError:
            break
        
        media = (nota_a * 0.2) + (nota_b * 0.3) + (nota_c * 0.5)
        media_str = "{:.1f}".format(media)

        print("MEDIA = " + media_str)

        #: somente para o teste
        return "MEDIA = " + media_str


@pytest.mark.parametrize("input, expected", [
    (
        ["5.0", "6.0", "7.0"],
        "MEDIA = 6.3"
    ),
    (
        ["5.0", "10.0", "10.0"],
        "MEDIA = 9.0"
     ),
    (
        ["10.0", "10.0", "5.0"],
        "MEDIA = 7.5"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = media_2()

    assert result == expected
