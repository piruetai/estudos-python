# Desafio 03 — Boletim de Turma

## Enunciado

Uma escola quer organizar as notas dos alunos de uma turma em um único
boletim:

| Aluno    | Nota 1 | Nota 2 | Nota 3 |
|----------|--------|--------|--------|
| Ana      | 8.0    | 7.5    | 9.0    |
| Bruno    | 5.0    | 6.0    | 4.5    |
| Carla    | 9.5    | 10.0   | 9.0    |

**Objetivo:** criar um programa que:

1. Armazene os dados em um dicionário aninhado, onde cada chave é o nome
   do aluno e o valor é outro dicionário com as notas.
2. Calcule a média de cada aluno e adicione essa informação ao
   dicionário do respectivo aluno usando `update` ou atribuição direta.
3. Utilize `items()` para percorrer o dicionário e identificar quais
   alunos estão aprovados (média maior ou igual a 6.0).
4. Utilize `get` para buscar a nota de um aluno específico informado pelo
   usuário, mostrando uma mensagem padrão caso o aluno não exista.
5. Mostre no terminal o boletim completo, com médias, e a lista de
   aprovados.
