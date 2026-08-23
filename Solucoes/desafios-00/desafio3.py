def entrada():
    entrada = int(input("Entre um valor: "))
    return entrada

def valor_tabuada(numero):
    for n in range(1, 11):
        print(f"{numero} x {n} = {numero * n}")

#Função Limpadora de Tela independente de bibliotecas externas que encontrei
def clear_screen_ansi():
    # \033[H moves the cursor to the top left, \033[2J clears the screen
    print("\033[H\033[2J", end="")

execucao = True

while execucao:
    clear_screen_ansi()
    valor = entrada()
    valor_tabuada(valor)

    resposta = input("Inserir outro número?: ").lower().strip()
    if resposta == "sim":
        continue
    elif resposta == "não" or resposta == "nao":
        print("Encerrando o programa...")
        break
    else:
        print("Resposta inválida!")
        

 