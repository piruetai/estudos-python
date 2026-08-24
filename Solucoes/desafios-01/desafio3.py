boletim = dict(
    Ana = {"nota1": 8, "nota2": 7.5, "nota3": 9.0},
    Bruno = {"nota1": 5, "nota2": 6, "nota3": 4.5},
    Carla = {"nota1": 9.5, "nota2": 10, "nota3": 9.0} 
)


for chave, valor in boletim.items():
    valor["media"] = round((valor["nota1"] + valor["nota2"] + valor["nota3"])/3, 1)
    print(chave)


resp = input("Insira o nome de um aluno: ").capitalize()
if resp not in boletim:
    print("Aluno inexistente!")
else:
    print(f"\nnota1: {boletim[resp]["nota1"]}, nota2: {boletim[resp]["nota2"]}, nota3: {boletim[resp]["nota3"]}")
    for chave, valor in boletim.items():
        if valor["media"] <= 6:
            print(f"{chave} Reprovado(a)! Média: {valor["media"]}")
        else:
            print(f"{chave} Aprovado(a)! Média: {valor["media"]}")
