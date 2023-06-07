import pytest

def procurando_nessy():
    teste_array_num = []
    import math
    while True:
        try:
            qtd_testes = int(input())
        except:
            #: somente para o teste
            return " ".join(teste_array_num)

        for _ in range(0, qtd_testes):
            valores = [t for t in input().split(" ")]
            linhas = int(valores[0])
            colunas = int(valores[1])

            #: desconsiderar as bordas, pois nessie não consegue se enconder nelas
            resultado = int(math.ceil((linhas - 2) / 3) * math.ceil((colunas - 2) / 3))

            print(resultado)

            #: somente para o teste
            teste_array_num.append(str(resultado))


@pytest.mark.parametrize("input, expected", [
    (
        ["3", "6 6", "7 7", "9 13"],
        "4 4 12"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = procurando_nessy()

    assert result == expected
