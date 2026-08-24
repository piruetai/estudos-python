def cadastrar_contato(contatos, nome, telefone, **dados_extras):
    dic = dict()
    dic["nome"] = nome
    dic["telefone"] = telefone 
    dic["dados_extras"] = dados_extras
    contatos.append(dic)

def buscar_contato(contatos, nome):
    if contatos == []:
        print("Os contatos estão vazios!")
    else:
        for contato in contatos:
            if contato["nome"] == nome:
                return contato
        return False
    
def listar_contatos(contato):
    if contato == []:
        print("Os contatos estão vazios!")
    else:
        
        for linhas in contato:
            linha = f"Nome: {linhas['nome']} Telefone: {linhas['telefone']} Email: {linhas['dados_extras']['email']}"
            print(linha)
            print("-" * len(linha))

clientes_contatos = []

while True:
    print("""
    [d] Cadastrar
    [r] Buscar
    [e] Listar
    [q] Sair
    """)

    opcao = input("Escolha uma opção: ").lower()

    if opcao not in ["d", "r", "e", "q"]:
        print("Opção inválida. Tente novamente.")
        continue

    if opcao == "d":
        cadas1 = input("Insira o nome: ")
        cadas2 = input("Insira o telefone: ")
        cadas3 = input("Insira os dados adicionais (email/endereço): ")
        cadastrar_contato(clientes_contatos, cadas1, cadas2, email = cadas3)
        print(clientes_contatos)

    if opcao == "r":
        if clientes_contatos == []: 
            print("Lista vazia!!")
        else:
            nome = input("Digite o nome do contato que deseja procurar: ")
            resultado = buscar_contato(clientes_contatos, nome)
            if resultado == False:
                print("Contato inexistente")
            else:
                print(f"nome: {resultado['nome']}, telefone: {resultado['telefone']}, email: {resultado['dados_extras']['email']}")
    
    if opcao == "e":
        listar_contatos(clientes_contatos)

    if opcao == "q":
        print("Encerrando o programa...")
        break

