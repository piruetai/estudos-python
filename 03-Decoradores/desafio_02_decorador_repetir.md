# Desafio 02 — Decorador com Argumentos: Repetir Execução

## Enunciado

Durante testes manuais, um desenvolvedor quer poder executar uma mesma
função várias vezes seguidas, apenas anotando quantas repetições deseja,
sem alterar o corpo da função original.

**Objetivo:** criar um programa que:

1. Crie um decorador `repetir(vezes)` que receba um argumento (o número
   de repetições) e retorne o decorador de fato — ou seja, uma função que
   recebe a função a ser decorada.
2. Dentro do wrapper, execute a função original o número de vezes
   indicado em `vezes`, utilizando `*args` e `**kwargs` para repassar os
   parâmetros originais.
3. Aplique `@repetir(3)` em uma função que envia uma mensagem simulada
   (ex.: `print(f"Enviando mensagem para {destinatario}")`).
4. Aplique `@repetir(5)` em outra função diferente, demonstrando que o
   mesmo decorador pode ser reutilizado com valores distintos.
5. Mostre no terminal a saída de cada chamada, confirmando visualmente
   que a função foi executada o número correto de vezes.
