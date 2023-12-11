import pytest


def organiza_times(qtd_duendes, qtd_times):
    lista_ordenada_duendes = []
    for _ in range(qtd_duendes):
        nome, idade = input().split()
        lista_ordenada_duendes.append((nome, int(idade)))
    
    lista_ordenada_duendes = sorted(
        lista_ordenada_duendes,
        key = lambda x: (-x[1], x[0]),
    )

    times = [[] for _ in range(qtd_times)]

    for i in range(0, qtd_duendes, qtd_times):
        for j in range(qtd_times):
            times[j].append(lista_ordenada_duendes[i + j])

    return times


def retorno_metodo(times):
    resultado_pytest = []
    for i in range(len(times)):
        contador = 0
        time = f'Time {i + 1}'
        print(time)

        #: somente para o teste
        resultado_pytest.append(time)

        for membro in times[i]:
            contador += 1
            resultado = f'{membro[0]} {membro[1]}'
            if contador == 3:
                #: Esse cara aqui é pra pular a linha de um jeito que o BeeCrowd entenda
                #: Se pular em um print separado, da "Presentation Error"
                print(f"{resultado}\n")
            else:
                print(resultado)

            #: somente para o teste
            resultado_pytest.append(resultado)

    #: somente para o teste
    return " ".join(resultado_pytest)


def time_de_duendes():
    while True:
        try:
            qtd_duendes = int(input())
        except:
            break

        qtd_times = int(qtd_duendes / 3)

        times = organiza_times(qtd_duendes, qtd_times)

        return retorno_metodo(times)


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
