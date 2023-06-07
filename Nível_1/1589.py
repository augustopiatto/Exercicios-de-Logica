import pytest

def bob_conduite():
    teste_array_num = []
    qtd_casos = int(input())
    while True:
        try:
            r_array = [int(r) for r in input().split(" ")]
        except:
            #: somente para o teste
            return " ".join(teste_array_num)

        r1 = r_array[0]
        r2 = r_array[1]
        
        resultado = r1 + r2
        qtd_casos -= 1

        print(resultado)

        #: somente para o teste
        teste_array_num.append(str(resultado))


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
