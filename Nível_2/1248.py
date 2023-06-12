import pytest

def plano_de_dieta():
    teste_list_num = []
    while True:
        try:
            qtd_testes = int(input())
        except:
            break
        
        for _ in range(qtd_testes):
            alim_dieta = input()
            cafe_manha = input()
            almoco = input()

            refeicoes_ate_agr = cafe_manha + almoco

            comer_na_janta = alim_dieta
            for index in range(len(refeicoes_ate_agr)):
                if refeicoes_ate_agr[index] in alim_dieta:
                    comer_na_janta = comer_na_janta.replace(refeicoes_ate_agr[index], "")
                else:
                    comer_na_janta = "CHEATER"
                    break
            
            resultado = "".join(sorted(comer_na_janta)) if comer_na_janta != "CHEATER" else "CHEATER"
            print(resultado)

            #: somente para o teste
            teste_list_num.append(resultado)
    
    #: somente para o teste
    return " ".join(teste_list_num)


@pytest.mark.parametrize("input, expected", [
    (
        ["5", "ABCD", "AB", "C", "ABEDCS", "", "", "EDSMB", "MSD", "A", "", "", "", "IWANTSODER", "SOW", "RAT"],
        "D ABCDES CHEATER  DEIN"
    )
])
def test(input, expected, monkeypatch):
    inputs = iter(input)
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    result = plano_de_dieta()

    assert result == expected
