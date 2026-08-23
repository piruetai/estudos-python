#Função Limpadora de Tela independente de bibliotecas externas que encontrei
def clear_screen_ansi():
    # \033[H moves the cursor to the top left, \033[2J clears the screen
    print("\033[H\033[2J", end="")

def usuario_inserir(list: list):
    list.append(input("Insira o nome do produto: "))
    return list

def usuario_exibir(list: list):
    if list == []: return print("A Lista está vazia!")
    print("Lista de Produtos:\n")
    list.sort()
    for ind, valores in enumerate(list):
        print(f"{ind}: {valores}\n")

def usuario_remover(list: list):
    if list == []:
        print("A Lista está vazia!")
    else:
        usuario_exibir(list)
        resp = int(input("Insira o índice do produto a ser removido: "))
        if resp not in range(len(list)): return print("Índice inválido")
        list.remove(list[resp])
        return list

lista = []

while True:
    print("""
    [1] Adicionar produto
    [2] Remover produto
    [3] Exibir lista
    [4] Sair
    """)
    opcao = input("Escolha uma opção: ")
    if opcao not in ["1", "2", "3", "4"]:
        clear_screen_ansi()
        print("Opção inválida. Tente novamente.")
        continue
    elif opcao == "1": usuario_inserir(lista), clear_screen_ansi()
    elif opcao == "2": clear_screen_ansi(), usuario_remover(lista)
    elif opcao == "3": clear_screen_ansi(), usuario_exibir(lista)
    elif opcao == "4": break