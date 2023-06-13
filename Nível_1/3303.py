import pytest


def palavrao():
    while True:
        try:
            palavra = input()
        except EOFError:
            break

        print("palavrao" if len(palavra) >= 10 else "palavrinha")

        #: somente para o teste
        return "palavrao" if len(palavra) >= 10 else "palavrinha"


@pytest.mark.parametrize("input, expected", [
    ("paralelepipedo", "palavrao"),
    ("carro", "palavrinha")
])
def test(input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input)
    result = palavrao()

    assert result == expected
