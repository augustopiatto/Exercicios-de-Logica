import math


def chocolate_feast(dinheiro_inicial, preco_chocolate, qtt_embalagem_para_troca):
    chocolates_comprados = int(dinheiro_inicial / preco_chocolate)
    embalagens = chocolates_comprados
    soma_chocolates_da_troca = 0
    while embalagens >= qtt_embalagem_para_troca:
        chocolates_da_troca = int(math.floor(embalagens /
                                             qtt_embalagem_para_troca))
        soma_chocolates_da_troca += chocolates_da_troca
        embalagens = embalagens % qtt_embalagem_para_troca
        embalagens += chocolates_da_troca

    return chocolates_comprados + soma_chocolates_da_troca


def test_chocolate_feast_1():
    result = chocolate_feast(6, 2, 2)

    assert result == 5


def test_chocolate_feast_2():
    result = []
    path = "HackerRank/chocolate_feast.txt"
    with open(path, "r") as file:
        lines = file.readlines()
    for line in lines:
        money = int(line.split()[0])
        price = int(line.split()[1])
        qtt_to_trade = int(line.split()[2])

        result.append(chocolate_feast(money, price, qtt_to_trade))

    path = "HackerRank/chocolate_feast_result.txt"
    with open(path, "r") as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        assert result[index] == int(line.split()[0])


def test_chocolate_feast_3():
    result = chocolate_feast(43203, 60, 5)

    assert result == 899
