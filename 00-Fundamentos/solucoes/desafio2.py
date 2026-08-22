def inserir_idade():
    try:
        idade_visitante = int(input("Informe sua idade: "))
        return idade_visitante
    except TypeError:
        print("Erro: insira uma idade válida!")
        inserir_idade()

idade_visitante = inserir_idade()
classificacao = "Criança pequena" if idade_visitante <= 5 else ("Criança" if idade_visitante <= 12 else ("Adulto" if idade_visitante <= 59 else "Idoso"))
valor_ingresso = 0 if classificacao == "Criança pequena" else (20 if classificacao == "Criança" else (45 if classificacao == "Adulto" else 22.50))

print(f"idade: {idade_visitante}")
print(f"classificação: {classificacao}")
print(f"valor do ingresso: {'Gratuito' if valor_ingresso == 0 else valor_ingresso}")

#if idade_visitante <= 5:
#    classificacao = "Criança pequena"
#elif idade_visitante <= 12:
#    classificacao = "Criança"
#elif idade_visitante <= 59:
#    classificacao = "Adulto"
#elif idade_visitante > 60:
#    classificacao = "Idoso"
