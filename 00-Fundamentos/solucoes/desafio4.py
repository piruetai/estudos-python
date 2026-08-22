# Código funcional, porém sem uso de funções nativas do python.
# def senha_entrada():
#     senha = str(input("Digite sua senha: "))
#     return senha

# def senha_tamanho(senha):
#     tamn = len(senha)
#     return f"{tamn} Válido!" if tamn >= 8 else f"{tamn} Inválido"

# def senha_digito(senha):
#     numeros = 0
#     for char in senha:
#         if char.isdigit():
#             numeros += 1
#     return f"{numeros} Válido!"  if numeros > 0 else f"{numeros} Inválido"
    
# def senha_maisculo(senha):
#     numeros = 0
#     for char in senha:
#         if char.isupper():
#             numeros += 1
#         return "Válido!" if numeros >= 1 else "Inválido"

# def senha_espaco(senha):
#     return "Válido!" if " " not in senha else "Inválido"

# senha = senha_entrada()
# resultado = f"Tamanho: {senha_tamanho(senha)}, Digito: {senha_digito(senha)}, Maiusculo: {senha_maisculo(senha)}, Espaco: {senha_espaco(senha)}"
# print(resultado)

def senha_entrada():
    senha = str(input("Digite sua senha: "))
    return senha

def senha_tamanho(senha):
    return True if len(senha) >= 8 else False

def senha_digito(senha):
    return any(char.isdigit() for char in senha)
    
def senha_maisculo(senha):
    return any(char.isupper() for char in senha)

def senha_espaco(senha):
    return True if " " not in senha else False

def validar_senha(senha):
    return {
        "tamanho": senha_tamanho(senha),
        "digito": senha_digito(senha),
        "maiusculo": senha_maisculo(senha),
        "espaco": senha_espaco(senha)
    }

senha = senha_entrada()
resultado = validar_senha(senha)

for chave, valor in resultado.items():
    print(f"Critério {chave}: {'Válido!' if valor else 'Inválido!'}")
