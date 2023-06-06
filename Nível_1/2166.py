# import pytest

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

# TODO

# pytest.mark.parametrize("input, output", [(["3 2"], "Total: R$ 10.00")])
# @parametrize(input, output)
# def test:
#     raiz_quadrada_de_2()
