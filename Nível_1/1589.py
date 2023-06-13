import pytest


def bob_conduite():
    teste_list_num = []
    qtd_casos = int(input())
    while True:
        try:
            r_list = [int(r) for r in input().split(" ")]
        except:
            #: somente para o teste
            return " ".join(teste_list_num)

        r1 = r_list[0]
        r2 = r_list[1]
        
        resultado = r1 + r2
        qtd_casos -= 1

        print(resultado)

        #: somente para o teste
        teste_list_num.append(str(resultado))


@pytest.mark.parametrize("input, expected", [
    (
        ["3", "1 1", "2 8", "8 2"],
        "2 10 10"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = bob_conduite()

    assert result == expected
