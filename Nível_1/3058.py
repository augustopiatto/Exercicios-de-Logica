import pytest

def supermercado():
    while True:
        try:
            qtd_supermercados = int(input())
        except EOFError:
            break

        mais_barato = 10000000000000
        for _ in range(qtd_supermercados):
            valores = [t for t in input().split(" ")]
            preco = float(valores[0])
            gramas = float(valores[1])

            preco_por_kg = preco / (gramas / 1000)

            if preco_por_kg < mais_barato:
                mais_barato = preco_por_kg

        resultado = float(mais_barato)

        resultado_decimal = "{:.2f}".format(resultado)

        print(resultado_decimal)

        #: somente para o teste
        return resultado_decimal


# fonte: https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9
@pytest.mark.parametrize("input, expected", [
    (
        ["3", "3.0 100", "2.0 100", "5.0 100"],
        "20.00"
    ),
    (
        ["4", "100.00 500", "190.00 1000", "200.00 900", "110.00 550"],
        "190.00"
     ),
    (
        ["5", "46.50 794", "25.72 130", "66.00 800", "22.45 110", "38.99 453"],
        "58.56"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = supermercado()

    assert result == expected
