import pytest

def escada_rolante():
    teste_array_num = []
    while True:
        qtd_pessoas = int(input())
        if not qtd_pessoas:
            #: somente para o teste
            return " ".join(teste_array_num)

        t_array = [int(t) for t in input().split(" ")]

        tempo_total = 10
        if qtd_pessoas == 1:
            print(tempo_total)
        else:
            for idx in range(0, len(t_array) - 1):
                if t_array[idx + 1] - t_array[idx] >= 10:
                    tempo_total += 10
                else:
                    tempo_total += (t_array[idx + 1] - t_array[idx])
                
            print(tempo_total)
        
        #: somente para o teste
        teste_array_num.append(str(tempo_total))


@pytest.mark.parametrize("input, expected", [
    (
        ["1", "5", "2", "12 25", "2", "13 16", "5", "15 20 29 31 50", "0"],
        "10 20 13 36"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = escada_rolante()

    assert result == expected
