import pytest

def divisibilidade_por_3():
    teste_list_num = []
    while True:
        try:
            _, numero = input().split(" ")
        except:
            break

        soma_digitos = sum(int(digito) for digito in str(numero))

        eh_divisivel = "sim" if soma_digitos % 3 == 0 else "nao"

        resultado = f"{soma_digitos} {eh_divisivel}"

        print(resultado)

        #: somente para o teste
        teste_list_num.append(resultado)
    
    #: somente para o teste
    return " ".join(teste_list_num)


@pytest.mark.parametrize("input, expected", [
    (
        ["3 111", "1 1", "2 24"],
        "3 sim 1 nao 6 sim"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = divisibilidade_por_3()

    assert result == expected
