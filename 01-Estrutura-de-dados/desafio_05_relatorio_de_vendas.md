# Desafio 05 — Relatório de Vendas por Vendedor

## Enunciado

Uma loja registrou as seguintes vendas do mês:

| Vendedor | Produto  | Valor   |
|----------|----------|---------|
| Marcos   | Teclado  | R$ 250  |
| Julia    | Mouse    | R$ 120  |
| Marcos   | Monitor  | R$ 900  |
| Julia    | Headset  | R$ 180  |
| Marcos   | Mouse    | R$ 120  |

**Objetivo:** criar um programa que:

1. Armazene as vendas em uma `list` de dicionários (vendedor, produto,
   valor).
2. Crie uma função que agrupe o total vendido por vendedor em um
   dicionário, onde a chave é o nome do vendedor e o valor é a soma das
   vendas.
3. Crie uma função que retorne uma tupla `(nome, total)` do vendedor com
   maior valor total vendido.
4. Utilize compreensão de lista para criar uma lista apenas com os nomes
   dos produtos vendidos, sem repetição (dica: combine com `set`).
5. Mostre no terminal o total vendido por cada vendedor, o vendedor
   destaque do mês e a lista de produtos distintos vendidos.
