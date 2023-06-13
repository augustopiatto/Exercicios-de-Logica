import pytest


def raiz_quadrada_de_2():
    while True:
        try:
            repeticoes = int(input())
        except EOFError:
            break

        divisor = 0
        while repeticoes:
            divisor += 2
            divisor = 1 / divisor

            repeticoes -= 1

        resultado = float(1 + divisor) if divisor else 1

        resultado_decimal = "{:.10f}".format(resultado)

        print(resultado_decimal)

        #: somente para o teste
        return resultado_decimal


@pytest.mark.parametrize("input, expected", [
    ("0", "1.0000000000"),
    ("1", "1.5000000000"),
    ("5", "1.4142857143")
])
def test(input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input)
    result = raiz_quadrada_de_2()

    assert result == expected
