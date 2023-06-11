import pytest

def time_de_duendes():
    teste_list_num = []
    while True:
        try:
            qtd_duendes = int(input())
        except:
            break

        lista_ordenada_duendes = []
        qtd_times = int(qtd_duendes / 3)

        for _ in range(0, qtd_duendes):
            nome, idade = input().split()
            lista_ordenada_duendes.append((nome, int(idade)))
        
        lista_ordenada_duendes = sorted(
            lista_ordenada_duendes,
            key = lambda x: (-x[1], x[0]),
        )

        for num in range(0, qtd_times):
            time = f"Time {num + 1}"
            print(f"Time {num + 1}")

            #: somente para o teste
            teste_list_num.append(time)
            contador = 0

            for index in range(num, len(lista_ordenada_duendes), qtd_times):
                contador += 1
                nome_duende = lista_ordenada_duendes[index][0]
                idade_duende = lista_ordenada_duendes[index][1]
                resultado = f"{nome_duende} {idade_duende}"
                if contador == 3:
                    #: Esse cara aqui é pra pular a linha de um jeito que o BeeCrowd entenda
                    #: Se pular em um print separado, da "Presentation Error"
                    print(f"{resultado}\n")
                else:
                    print(f"{resultado}")

                #: somente para o teste
                teste_list_num.append(resultado)
    
    #: somente para o teste
    return " ".join(teste_list_num)

def ordena_alfabeticamente(pair1, pair2):
    number1, word1 = pair1
    number2, word2 = pair2
    if number1 == number2:
        if word1 < word2:
            return -1
        else:
            return 1
    if number1 < number2:
        return -1
    else:
        return 1


@pytest.mark.parametrize("input, expected", [
    (
        ["6", "Josh 56", "Alfred 32", "Joshua 34", "Peggy 61", "Harley 61", "Jim 25"],
        "Time 1 Harley 61 Josh 56 Alfred 32 Time 2 Peggy 61 Joshua 34 Jim 25"
    ),
    (
        ["9", "Kepeumo 67", "Necoi 62", "Seies 77", "Ciule 49", "Gyun 99", "Finron 27", "Norandir 66", "Galvaindir 55", "Pinhuobor 70"],
        "Time 1 Gyun 99 Kepeumo 67 Galvaindir 55 Time 2 Seies 77 Norandir 66 Ciule 49 Time 3 Pinhuobor 70 Necoi 62 Finron 27"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = time_de_duendes()

    assert result == expected
