mes_vendas = [
    {"Vendedor": "Marcos", "Produto": "Teclado", "Valor": 250},
    {"Vendedor": "Julia", "Produto": "Mouse", "Valor": 120},
    {"Vendedor": "Marcos", "Produto": "Monitor", "Valor": 900},
    {"Vendedor": "Julia", "Produto": "Headset", "Valor": 180},
    {"Vendedor": "Marcos", "Produto": "Mouse", "Valor": 120}
]

def maisvendido(vendas):
    arm = {}
    arm["Teclado"] = 0 
    arm["Mouse"] = 0
    arm["Headset"] = 0
    for valor in vendas:
        if valor["Produto"] =="Teclado":
            arm["Teclado"] += 1
        elif valor["Produto"] =="Mouse":
            arm["Mouse"] += 1
        elif valor["Produto"] =="Headset":
            arm["Headset"] += 1
    return arm

    
def mes_soma(total, vendas):
    total["Total_Marcos"] = 0 
    total["Total_Julia"] = 0
    for valor in vendas:
        if valor["Vendedor"] =="Marcos":
            total["Total_Marcos"] += valor["Valor"]
        elif valor["Vendedor"] =="Julia":
            total["Total_Julia"] += valor["Valor"]
    return total

def mes_compare(dic_vendas, dic_total):
    tupla = (dic_vendas, dic_total)
    return tupla


mes_total = dict()
produtos = set([linha["Produto"] for linha in mes_vendas])

dict = mes_soma(mes_total, mes_vendas)
tupla1 = mes_compare(mes_vendas[0]["Vendedor"], mes_total["Total_Marcos"])
tupla2 = mes_compare(mes_vendas[1]["Vendedor"], mes_total["Total_Julia"])
qtde = maisvendido(mes_vendas)

print(dict)
print(tupla1)
print(tupla2)
print(produtos)
print(qtde)
