# Desafio 05 — Cofre de Fichas do Cassino

## Enunciado

Um cassino fictício quer um terminal simples para controlar o cofre de
fichas de um caixa. O caixa começa o dia com 0 fichas em cofre e segue as
seguintes regras:

| Operação   | Regra                                              |
|------------|-----------------------------------------------------|
| Depositar  | Sempre permitido, desde que o valor seja positivo   |
| Retirar    | Só é permitido se houver fichas suficientes no cofre|
| Extrato    | Mostra o total de depósitos, retiradas e o saldo    |
| Sair       | Encerra o programa                                  |

**Objetivo:** criar um programa que:

1. Exiba um menu com as opções `[d] Depositar`, `[r] Retirar`,
   `[e] Extrato` e `[q] Sair`, utilizando um laço `while` para manter o
   menu em execução.
2. Trate cada opção com estruturas condicionais, validando se o valor
   informado é válido (positivo) e, no caso de retirada, se o cofre tem
   saldo suficiente.
3. Utilize `break` para encerrar o laço quando o usuário escolher sair.
4. Mostre mensagens claras de sucesso ou falha para cada operação, e no
   extrato mostre o total depositado, total retirado e saldo atual.
