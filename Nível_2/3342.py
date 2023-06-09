import pytest

def keanu():
    import math
    while True:
        try:
            lado_tabuleiro = int(input())
        except EOFError:
            break

        total = lado_tabuleiro * lado_tabuleiro
        casa_preta = math.floor(total / 2)
        casa_branca = total - casa_preta

        print(f"{casa_branca} casas brancas e {casa_preta} casas pretas")

        #: somente para o teste
        return f"{casa_branca} casas brancas e {casa_preta} casas pretas"


@pytest.mark.parametrize("input, expected", [
    ("2", "2 casas brancas e 2 casas pretas"),
    ("3", "5 casas brancas e 4 casas pretas"),
    ("4", "8 casas brancas e 8 casas pretas"),
    ("5", "13 casas brancas e 12 casas pretas")
])
def test(input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input)
    result = keanu()

    assert result == expected
