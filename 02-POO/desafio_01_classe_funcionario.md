# Desafio 01 — Classe Funcionário

## Enunciado

Uma empresa quer padronizar o cadastro de seus funcionários usando
Orientação a Objetos, em vez de dicionários soltos.

| Nome    | Cargo        | Salário  |
|---------|--------------|----------|
| Renata  | Analista     | R$ 4.500 |
| Diego   | Desenvolvedor| R$ 6.200 |

**Objetivo:** criar um programa que:

1. Defina uma classe `Funcionario` com um construtor (`__init__`) que
   receba nome, cargo e salário.
2. Implemente um método `aplicar_reajuste(percentual)` que aumente o
   salário do funcionário de acordo com o percentual informado.
3. Implemente um método `__str__` que retorne uma descrição legível do
   funcionário (nome, cargo e salário atual).
4. Instancie ao menos dois objetos `Funcionario`, aplique um reajuste em
   um deles e mostre o estado de ambos no terminal antes e depois do
   reajuste.
