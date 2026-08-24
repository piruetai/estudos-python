

def cadastrar_contato(contatos, nome, telefone, **dados_extras):
    for valor in contatos:
        valor["nome"] = nome, 
        valor["telefone"] = telefone 
        valor["dados_extras"] = dados_extras


clientes_contatos = [
    {}

]

while True:
    print("""
    [d] Cadastrar
    [r] Buscar
    [e] Listar
    [q] Sair
    """)
    opcao = input("Escolha uma opção: ")
    if opcao not in ["d", "r", "e", "q"]:
        print("Opção inválida. Tente novamente.")
        continue

    if opcao == "d":
        cadas1 = input("Insira o nome: ")
        cadas2 = input("Insira o telefone: ")
        cadas3 = input("Insira os dados adicionais (email/endereço): ")
        cadastrar_contato(clientes_contatos, cadas1, cadas2, email = cadas3)
        print(clientes_contatos)

