import pytest

def lanche():
    input_list = [int(i) for i in input().split(" ")]
    codigo = input_list[0]
    qtd = input_list[1]

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

    #: somente para o teste
    return f"Total: R$ {total_decimal}"


@pytest.mark.parametrize("input, expected", [
    ("3 2", "Total: R$ 10.00"),
    ("4 3", "Total: R$ 6.00"),
    ("2 3", "Total: R$ 13.50")
])
def test(input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input)
    result = lanche()

    assert result == expected