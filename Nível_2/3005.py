import pytest
 

def empilha(d1, d2):
    if (
        (d1[0] < d2[0] and d1[1] < d2[1])
        or
        (d1[0] < d2[1] and d1[1] < d2[0])
        or
        (d1[0] < d2[1] and d1[1] < d2[2])
        or
        (d1[0] < d2[2] and d1[1] < d2[1])
        or
        (d1[0] < d2[0] and d1[1] < d2[2])
        or
        (d1[0] < d2[2] and d1[1] < d2[0])
        or
        (d1[1] < d2[0] and d1[2] < d2[1])
        or
        (d1[1] < d2[1] and d1[2] < d2[0])
        or
        (d1[1] < d2[1] and d1[2] < d2[2])
        or
        (d1[1] < d2[2] and d1[2] < d2[1])
        or
        (d1[1] < d2[0] and d1[2] < d2[2])
        or
        (d1[1] < d2[2] and d1[2] < d2[0])
        or
        (d1[0] < d2[0] and d1[2] < d2[1])
        or
        (d1[0] < d2[1] and d1[2] < d2[0])
        or
        (d1[0] < d2[1] and d1[2] < d2[2])
        or
        (d1[0] < d2[2] and d1[2] < d2[1])
        or
        (d1[0] < d2[0] and d1[2] < d2[2])
        or
        (d1[0] < d2[2] and d1[2] < d2[0])
    ):
        return True

    return False


def pilhas_de_paralelepipedo():
    teste_list_num = []
    while True:
        try:
            qtd_testes = int(input())
        except:
            break
        
        for _ in range(qtd_testes):
            dimensoes_list = list(map(int, input().split()))

            dimensoes_tijolo_1 = dimensoes_list[:3]
            dimensoes_tijolo_2 = dimensoes_list[3:]

            if empilha(dimensoes_tijolo_1, dimensoes_tijolo_2) and empilha(dimensoes_tijolo_2, dimensoes_tijolo_1):
                resultado = "3"
                print(3)
            elif empilha(dimensoes_tijolo_2, dimensoes_tijolo_1):
                resultado = "2"
                print(2)
            elif empilha(dimensoes_tijolo_1, dimensoes_tijolo_2):
                resultado = "1"
                print(1)
            else:
                resultado = "0"
                print(0)

                #: somente para o teste
            teste_list_num.append(resultado)
    
    #: somente para o teste
    return " ".join(teste_list_num)


@pytest.mark.parametrize("input, expected", [
    (
        [
            "3",
            "10 10 10 10 20 10",
            "12 20 14 30 10 10",
            "8 20 14 20 10 10"
        ],
        "0 2 3"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = pilhas_de_paralelepipedo()

    assert result == expected
