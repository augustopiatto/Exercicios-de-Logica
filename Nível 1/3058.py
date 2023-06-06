# import pytest

def supermercado():
    while True:
        try:
            qtd_supermercados = int(input())
        except EOFError:
            break

        mais_barato = 10000
        for supermercado in range(0, qtd_supermercados):
            valores = [t for t in input().split(" ")]
            preco = float(valores[0])
            gramas = float(valores[1])

            preco_por_kg = preco / (gramas / 1000)

            if preco_por_kg < mais_barato:
                mais_barato = preco_por_kg

        resultado = float(mais_barato)

        resultado_decimal = "{:.2f}".format(resultado)

        print(resultado_decimal)

# TODO

# pytest.mark.parametrize("input, output", [(["3 2"], "Total: R$ 10.00")])
# @parametrize(input, output)
# def test:
#     supermercado()
