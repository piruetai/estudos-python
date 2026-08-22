# Desafio 05 — Contador de Instâncias

## Enunciado

Uma fábrica de produtos quer saber, a qualquer momento, quantas unidades
de um determinado item já foram produzidas, sem depender de uma variável
solta fora das classes.

**Objetivo:** criar um programa que:

1. Defina uma classe `Produto` com um atributo de classe
   `total_produzido`, compartilhado por todas as instâncias, iniciado em 0.
2. No construtor (`__init__`), receba um atributo de instância `codigo`
   (único para cada produto) e incremente `total_produzido` a cada novo
   objeto criado.
3. Implemente um método de classe (`@classmethod`) chamado
   `quantidade_produzida(cls)` que retorne o valor atual de
   `total_produzido`.
4. Implemente um método estático (`@staticmethod`) chamado
   `codigo_valido(codigo)` que valide se um código segue um padrão
   simples (ex.: começar com a letra "P" seguida de números).
5. Instancie vários produtos e mostre no terminal, ao final, quantos
   produtos foram criados no total, utilizando o método de classe.
