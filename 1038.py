# import pytest

def lanche():
    input_array = [int(i) for i in input().split(" ")]
    codigo = input_array[0]
    qtd = input_array[1]

    valor_obj = {
        1: float(4),
        2: float(4.5),
        3: float(5),
        4: float(2),
        5: float(1.5)
    }

    total = float(valor_obj[codigo] * qtd)
    total_decimal = "{:.2f}".format(total)

    print(f"Total: R$ {total_decimal}")


# pytest.mark.parametrize("input, output", [(["3 2"], "Total: R$ 10.00")])
# @parametrize(input, output)
# def test:
#     lanche()
