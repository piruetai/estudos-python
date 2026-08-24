Corrida1 =  (10, 20), (15, 25), (10, 20), (30, 40)
Corrida2 = (15, 25), (50, 60), (30, 40)

def corrida_exibir(corri):
    return (set(corri))

def corrida_uniao(corri1, corri2):
    return set(corri1).union(set(corri2))

def corrida_intersecao(corri1, corri2):
    return set(corri1).intersection(set(corri2))

print(f"Primeira Corrida: {corrida_exibir(Corrida1)})")
print(f"Segunda Corrida: {corrida_exibir(Corrida2)}")

corrida_uniao_resultado = corrida_uniao(Corrida1, Corrida2)
corrida_intersecao_resultado = corrida_intersecao(Corrida1, Corrida2)

print(f"Pontos únicos do dia (União): {corrida_uniao_resultado}")
print(f"Pontos em comum do dia (Interseção): {corrida_intersecao_resultado}")


