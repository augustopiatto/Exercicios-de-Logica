import pytest


def formula_de_binet(numero):
    from math import pow, sqrt
    parte_1 = pow(((1 + sqrt(5)) / 2), numero)
    parte_2 = pow(((1 - sqrt(5)) / 2), numero)
    num = (parte_1 - parte_2) / sqrt(5)

    return float(num)

#: Tem que tirar o nome desse método quando for colar no BeeCrowd
def fibonacci_rapido():
    while True:
        try:
            numero = int(input())
        except:
            break

        num_fibonacci = formula_de_binet(numero)

        resultado = "{:.1f}".format(num_fibonacci)

        print(resultado)

        #: somente para o teste
        return resultado


@pytest.mark.parametrize("input, expected", [
    ("1", "1.0"),
    ("2", "1.0"),
    ("3", "2.0")
])
def test(input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input)
    result = fibonacci_rapido()

    assert result == expected
