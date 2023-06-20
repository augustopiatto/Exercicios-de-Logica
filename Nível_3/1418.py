import pytest


def calcula_peticoes(subordinados_map, index, porcentagem_aumento, peticoes, soma):
    import math
    if not subordinados_map.get(index):
        peticoes += 1
        print('peticoes', peticoes)
    else:
        qtd_subordinados = math.ceil((len(subordinados_map[index]) * porcentagem_aumento) / 100)
        for num_funcionario in subordinados_map[index]:
            calcula_peticoes(subordinados_map, num_funcionario, porcentagem_aumento, peticoes, soma)
            if (peticoes / qtd_subordinados) > (porcentagem_aumento / 100):
                soma += 1
                print('soma', soma)
    

#: Tem que tirar o nome desse método quando for colar no BeeCrowd
def outra_crise():
    while True:
        input_1 = input().split(" ")
        if input_1[0] == "0" and input_1[1] == "0":
            break
        chefes = input().split(" ")

        qtd_empregados = int(input_1[0])
        porcentagem_aumento = int(input_1[1])

        subordinados_map = {}
        for index in range(len(chefes)):
            numero_do_funcionario = int(chefes[index])
            if not subordinados_map.get(numero_do_funcionario, False):
                subordinados_map[numero_do_funcionario] = [index + 1]
            else:
                subordinados_map[numero_do_funcionario].append(index + 1)
        # {0: [1, 2], 1: [3, 4], 2: [5, 6, 7], 5: [8, 10, 12, 14], 7: [9, 11, 13]}
        
        peticoes = 0
        soma = 0
        calcula_peticoes(subordinados_map, 0, porcentagem_aumento, peticoes, soma)

        # print(resultado)

        # # #: somente para o teste
        # return resultado


@pytest.mark.parametrize("input, expected", [
    # (["3 100", "0 0 0"], 3),
    # (["3 50", "0 0 0"], 2),
    (["14 60", "0 0 1 1 2 2 2 5 7 5 7 5 7 5"], 5),
    (["0 0"], None)
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = outra_crise()

    assert result == expected
