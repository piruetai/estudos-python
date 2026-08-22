# Desafio 01 — Decorador de Cronômetro

## Enunciado

Um time de desenvolvimento quer medir, de forma reutilizável, quanto
tempo cada função do sistema leva para executar, sem precisar repetir o
mesmo código de medição de tempo dentro de cada função.

**Objetivo:** criar um programa que:

1. Crie uma função `cronometro(funcao)` que funcione como decorador,
   definindo uma função interna (`envelope` ou `wrapper`) que recebe
   `*args` e `**kwargs`.
2. Dentro do wrapper, registre o tempo antes e depois de executar a
   função original (utilizando o módulo `time`), e imprima o tempo total
   gasto.
3. Aplique o decorador `@cronometro` em pelo menos duas funções
   diferentes, uma rápida (ex.: uma soma simples) e uma mais lenta (ex.:
   um laço que percorre milhões de números).
4. Garanta que o wrapper retorne o valor original da função decorada,
   para que o comportamento da função não seja alterado, apenas
   observado.
5. Mostre no terminal o tempo de execução de cada função chamada.
