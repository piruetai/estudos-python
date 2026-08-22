# Desafio 04 — Validador de Senha

## Enunciado

Um sistema de cadastro exige que toda senha atenda às seguintes regras de
segurança:

| Regra                         | Exemplo válido | Exemplo inválido |
|--------------------------------|-----------------|--------------------|
| Ter pelo menos 8 caracteres    | `Senha1234`     | `Se1`              |
| Conter ao menos um número      | `Senha1234`     | `SenhaForte`       |
| Conter ao menos uma letra maiúscula | `Senha1234` | `senha1234`        |
| Não conter espaços em branco   | `Senha1234`     | `Senha 1234`       |

**Objetivo:** criar um programa que:

1. Peça ao usuário para digitar uma senha.
2. Verifique cada uma das quatro regras separadamente, utilizando
   operadores de comparação, operadores lógicos e o operador de
   associação `in`.
3. Acumule em uma string as mensagens de erro para cada regra não
   atendida.
4. Mostre no terminal se a senha é válida ou, caso não seja, liste todos
   os motivos pelos quais ela foi recusada.
