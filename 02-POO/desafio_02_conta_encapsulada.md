# Desafio 02 — Conta Bancária com Encapsulamento

## Enunciado

Um banco quer garantir que o saldo de uma conta nunca seja alterado
diretamente por fora da classe, apenas através de métodos controlados de
depósito e saque.

**Objetivo:** criar um programa que:

1. Defina uma classe `ContaBancaria` com um atributo privado `_saldo`,
   iniciado em 0, e um construtor que receba o nome do titular.
2. Utilize `@property` para criar uma propriedade `saldo` somente de
   leitura, que não permita alteração direta de fora da classe.
3. Implemente os métodos `depositar(valor)` e `sacar(valor)`, validando
   que o valor é positivo e que, no saque, há saldo suficiente.
4. Tente, no código principal, alterar `conta._saldo` diretamente e
   demonstre por que essa não é a forma correta de uso, preferindo os
   métodos da classe.
5. Mostre no terminal o extrato de operações realizadas e o saldo final.
