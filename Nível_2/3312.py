import pytest


def verifica_num_primo(numero):
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
    

def fatorial(numero):
    fat = 0
    if numero == 1:
        return 1
    else:
        fat = numero * fatorial(numero - 1)
    
    return fat
 

#: Tem que tirar o nome desse método quando for colar no BeeCrowd
def imberbe_matematico():
    teste_list_num = []
    while True:
        try:
            qtd_numeros = int(input())
            numeros_list = input().split(" ")
        except:
            break
        
        for numero in numeros_list:
            numero_inteiro = int(numero) if numero else 0
            is_primo = verifica_num_primo(numero_inteiro)

            if is_primo:
                fat = fatorial(numero_inteiro)
                resultado = f"{numero}! = {fat}"
                print(resultado)
            
                #: somente para o teste
                teste_list_num.append(resultado)
    
    #: somente para o teste
    return " ".join(teste_list_num)


@pytest.mark.parametrize("input, expected", [
    (
        ["4", "1 2 3 4  "],
        "2! = 2 3! = 6"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = imberbe_matematico()

    assert result == expected
