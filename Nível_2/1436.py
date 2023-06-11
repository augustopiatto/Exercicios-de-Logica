import pytest

def jogo_do_tijolo():
    import math
    teste_list_num = []
    while True:
        try:
            qtd_casos = int(input())
        except:
            break

        for case in range(1, qtd_casos + 1):
            jogadores_list = input().split(" ")
            qtd_jogadores = jogadores_list.pop(0)
            tamanho_lista = len(jogadores_list)
            idade_capitao = jogadores_list[math.floor(tamanho_lista / 2)]

            resultado = f"Case {case}: {idade_capitao}"

            print(resultado)

            #: somente para o teste
            teste_list_num.append(resultado)
    
    #: somente para o teste
    return " ".join(teste_list_num)


@pytest.mark.parametrize("input, expected", [
    (
        ["2", "5 19 17 16 14 12", "5 12 14 16 17 18"],
        "Case 1: 16 Case 2: 16"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = jogo_do_tijolo()

    assert result == expected
