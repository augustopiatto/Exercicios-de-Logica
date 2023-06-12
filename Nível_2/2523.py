import pytest

def a_mensagem_de_will():
    teste_list_num = []
    while True:
        try:
            alfabeto = input()
            qtd_lampadas_piscadas = int(input())
            posicao_lampadas_list = input().split(" ")
        except:
            break
        
        mensagem_will = ""
        for num in range(qtd_lampadas_piscadas):
            posicao = int(posicao_lampadas_list[num])
            mensagem_will += alfabeto[posicao - 1]

        print(mensagem_will)

        #: somente para o teste
        teste_list_num.append(mensagem_will)
    
    #: somente para o teste
    return " ".join(teste_list_num)


@pytest.mark.parametrize("input, expected", [
    (
        ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "4", "8 5 12 16"],
        "HELP"
    ),
    (
        ["QWERTYUIOPASDFGHJKLZXCVBNM", "10", "16 3 19 19 9 2 9 4 19 13"],
        "HELLOWORLD"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = a_mensagem_de_will()

    assert result == expected
