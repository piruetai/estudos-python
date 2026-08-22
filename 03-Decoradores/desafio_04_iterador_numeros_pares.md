# Desafio 04 — Iterador Personalizado de Números Pares

## Enunciado

Um sistema precisa percorrer apenas os números pares dentro de um
intervalo, mas sem gerar antecipadamente uma lista gigante em memória —
os números devem ser calculados um a um, conforme forem sendo pedidos.

**Objetivo:** criar um programa que:

1. Defina uma classe `NumerosPares` que receba, no construtor, um valor
   `inicio` e um valor `fim`.
2. Implemente o método `__iter__`, retornando o próprio objeto, para que
   a classe seja reconhecida como um iterável.
3. Implemente o método `__next__`, que calcule e retorne o próximo
   número par dentro do intervalo, lançando `StopIteration` quando o
   intervalo for esgotado.
4. Utilize um laço `for` para iterar sobre uma instância de
   `NumerosPares(1, 20)`, imprimindo cada número par encontrado.
5. Utilize também a função `next()` manualmente, em outra instância,
   para mostrar dois ou três números pares sem usar o `for`.
