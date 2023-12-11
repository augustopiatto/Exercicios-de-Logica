import pytest


#: Tem que tirar o nome desse método quando for colar no BeeCrowd
def arredondamento_por_valor_de_corte():
    while True:
        try:
            num = input()
            cutoff = input()
        except:
            break

        num_list = num.split(".")
        inteiro = num_list[0] if num_list[0] else 0
        decimal = "0." + num_list[1] if (len(num_list) == 2 and num_list[1]) else 0

        resultado = int(inteiro)
        if float(decimal) > float(cutoff):
            resultado += 1

        print(resultado)

        # #: somente para o teste
        return resultado


@pytest.mark.parametrize("input, expected", [
    (["003.656930", "0.5000"], 4),
    ([".001", "0.0001"], 1),
    (["1.99999999", "0.9999"], 2),
    (["135", "0.6531"], 135),
    (["135.", "0.6531"], 135),
    (["1356.13671", "0.1367"], 1357),
    (["0.00010001", "0.0001"], 1),
    (["2.06727476", "0.6701"], 2)
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = arredondamento_por_valor_de_corte()

    assert result == expected
