import pytest


def volta_a_faculdade_de_fisica():
    while True:
        try:
            velocidade_list = [int(t) for t in input().split(" ")]
        except EOFError:
            break
        vel_inicial = velocidade_list[0]
        tempo_inicial = velocidade_list[1]

        # dobro do tempo fornecido
        deslocamento_final = vel_inicial * (2 * tempo_inicial)
                
        print(deslocamento_final)

        #: somente para o teste
        return str(deslocamento_final)


@pytest.mark.parametrize("input, expected", [
    ("0 0", "0"),
    ("5 12", "120")
])
def test(input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input)
    result = volta_a_faculdade_de_fisica()

    assert result == expected
