saldo = 0

#Função Limpadora de Tela independente de bibliotecas externas que encontrei
def clear_screen_ansi():
    # \033[H moves the cursor to the top left, \033[2J clears the screen
    print("\033[H\033[2J", end="")

def usuario_depositar():
    global saldo
    valor = float(input("Digite o valor a ser depositado: "))
    if valor <= 0:
        return "Valor inválido. O depósito deve ser maior que zero."
    else:
        saldo += valor
    return "Depósito realizado com Sucesso!"

def usuario_retirar():
    global saldo
    valor = float(input("Digite o valor a ser retirado: "))
    if valor <= 0:
        return "Valor inválido. A retirada deve ser maior que zero."
    else:
        if valor > saldo:
            return "Saldo insuficiente para retirada"
        else:
            saldo -= valor
        return "Retirada realizada com Sucesso!"

def usuario_extrato():
    global saldo
    return f"Saldo atual: R$ {saldo:.2f}"

while True:
    print("""
    [d] Depositar
    [r] Retirar
    [e] Extrato
    [q] Sair
    """)
    opcao = input("Escolha uma opção: ")
    if opcao not in ["d", "r", "e", "q"]:
        clear_screen_ansi()
        print("Opção inválida. Tente novamente.")
        continue

    if opcao == "d":
        resultado = usuario_depositar()
        clear_screen_ansi()
        print(resultado)
    elif opcao == "r":
        resultado = usuario_retirar()
        clear_screen_ansi()
        print(resultado)
    elif opcao == "e":
        resultado = usuario_extrato()
        clear_screen_ansi()
        print(resultado)
    elif opcao == "q":
        print("Saindo...")
        break