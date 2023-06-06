# import pytest

def volta_a_faculdade_de_fisica():
    while True:
        try:
            velocidade_array = [int(t) for t in input().split(" ")]
        except EOFError:
            break
        vel_inicial = velocidade_array[0]
        tempo_inicial = velocidade_array[1]

        # dobro do tempo fornecido
        deslocamento_final = vel_inicial * (2 * tempo_inicial)
                
        print(deslocamento_final)

# TODO

# pytest.mark.parametrize("input, output", [(["3 2"], "Total: R$ 10.00")])
# @parametrize(input, output)
# def test:
#     volta_a_faculdade_de_fisica()
