import pytest

def a_biblioteca_do_senhor_severino():
    teste_array_num = []
    while True:
        try:
            qtd_livros = int(input())
        except:
            #: somente para o teste
            return " ".join(teste_array_num)

        array_numeros = []
        for _ in range(0, qtd_livros):
            array_numeros.append(str(input()))

        array_numeros.sort()
    
        for num in array_numeros:
            print(num)

        #: somente para o teste
        teste_array_num.extend(array_numeros)


# fonte: https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9
@pytest.mark.parametrize("input, expected", [
    (
        ["3", "1233", "0015", "0100", "7", "0752", "1110", "0001", "6322", "8000", "6321", "0000"],
        "0015 0100 1233 0000 0001 0752 1110 6321 6322 8000"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = a_biblioteca_do_senhor_severino()
    print("result", result)

    assert result == expected
