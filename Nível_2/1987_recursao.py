# Teste feito com recursão para aprendizado próprio
import pytest

def divisibilidade_por_3():
    teste_list_num =[]
    while True:
        try:
            _, numero = input().split()
        except:
            break

        soma_digitos = sum(int(digito) for digito in str(numero))

        eh_divisivel = "sim" if verifica_divisao(numero) else "nao"

        resultado = f"{soma_digitos} {eh_divisivel}"

        print(resultado)

        #: somente para o teste
        teste_list_num.append(resultado)
    
    #: somente para o teste
    return " ".join(teste_list_num)


def verifica_divisao(numero):
    soma_digitos = sum(int(digito) for digito in str(numero))

    qtd_digitos_resultado = len(str(soma_digitos))
    print(qtd_digitos_resultado)
    if qtd_digitos_resultado >= 2:
        return verifica_divisao(soma_digitos)
    else:
        # vou fazer assim pra nao usar o "%" e poder usar recursao
        return soma_digitos / 3 in (3, 2, 1) 


@pytest.mark.parametrize("input, expected", [
    (
        ["3 111", "1 1", "2 24", "7 2791035"],
        "3 sim 1 nao 6 sim 27 sim"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = divisibilidade_por_3()

    assert result == expected
