import pytest

def numero_primo(numero):
    from math import sqrt
    prime_flag = 0
    if(numero > 1):
        for i in range(2, int(sqrt(numero)) + 1):
            if (numero % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False


def menor_num_primo(numero):
    if numero_primo(numero):
        return numero

    return menor_num_primo(numero - 1)

#: Tem que tirar o nome desse método quando for colar no BeeCrowd
def diversao_dos_alunos():
    while True:
        try:
            numero_1, numero_2 = input().split()
        except:
            break

        numero_1_primo = menor_num_primo(int(numero_1))
        numero_2_primo = menor_num_primo(int(numero_2))

        resultado = str(numero_1_primo * numero_2_primo)

        print(resultado)

        #: somente para o teste
        return resultado


@pytest.mark.parametrize("input, expected", [
    ("10 15", "91"),
    ("50 100", "4559"),
    ("936 177", "160717"),
    ("439 663", "290179")
])
def test(input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input)
    result = diversao_dos_alunos()

    assert result == expected
