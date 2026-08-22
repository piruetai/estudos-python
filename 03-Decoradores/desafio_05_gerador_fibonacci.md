# Desafio 05 — Gerador da Sequência de Fibonacci

## Enunciado

Um professor de matemática quer gerar quantos termos da sequência de
Fibonacci forem necessários, sem precisar calcular e guardar todos os
valores em memória de uma vez, especialmente quando o número de termos
pedido for muito grande.

**Objetivo:** criar um programa que:

1. Crie uma função geradora `fibonacci(quantidade)` que utilize `yield`
   para produzir, um de cada vez, os termos da sequência de Fibonacci
   (0, 1, 1, 2, 3, 5, 8, ...) até atingir a quantidade solicitada.
2. Utilize um laço `for` para consumir o gerador e imprimir cada termo
   gerado, chamando `fibonacci(10)`.
3. Combine o gerador com um decorador simples (`@cronometro` ou similar,
   reaproveitando a ideia do Desafio 01) para medir quanto tempo leva
   para consumir totalmente o gerador.
4. Compare, em comentário no código, a diferença de uso de memória entre
   gerar os valores com `yield` e gerar uma lista completa com todos os
   valores de uma vez.
5. Mostre no terminal os termos gerados e o tempo total de execução.
