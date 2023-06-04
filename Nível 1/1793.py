# import pytest

def escada_rolante():
    while True:
        qtd_pessoas = int(input())
        if not qtd_pessoas:
            break

        t_array = [int(t) for t in input().split(" ")]

        if qtd_pessoas == 1:
            print(10)
        else:
            tempo_total = 10
            for idx in range(0, len(t_array) - 1):
                if t_array[idx + 1] - t_array[idx] >= 10:
                    tempo_total += 10
                else:
                    tempo_total += (t_array[idx + 1] - t_array[idx])
                
            print(tempo_total)

# TODO

# pytest.mark.parametrize("input, output", [(["3 2"], "Total: R$ 10.00")])
# @parametrize(input, output)
# def test:
#     escada_rolante()
