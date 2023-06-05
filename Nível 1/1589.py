# import pytest

def bob_conduite():
    qtd_casos = int(input())
    while qtd_casos > 0:
        r_array = [int(r) for r in input().split(" ")]
        r1 = r_array[0]
        r2 = r_array[1]
        
        print(r1+r2)
        
        qtd_casos -= 1

# TODO

# pytest.mark.parametrize("input, output", [(["3 2"], "Total: R$ 10.00")])
# @parametrize(input, output)
# def test:
#     bob_conduite()
