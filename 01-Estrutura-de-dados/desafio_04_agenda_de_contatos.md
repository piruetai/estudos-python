# Desafio 04 — Agenda de Contatos com Funções

## Enunciado

Uma pequena agenda telefônica precisa de funções separadas para cadastrar,
buscar e listar contatos, evitando que a lógica fique toda misturada em um
único bloco de código.

**Objetivo:** criar um programa que:

1. Armazene os contatos em uma `list` de dicionários, cada um com nome,
   telefone e e-mail.
2. Crie uma função `cadastrar_contato(contatos, nome, telefone, **dados_extras)`
   que aceite argumentos nomeados adicionais (`**kwargs`), como e-mail ou
   apelido, e adicione o contato à lista.
3. Crie uma função `buscar_contato(contatos, nome)` que retorne o contato
   correspondente ou `None`, caso não seja encontrado.
4. Crie uma função `listar_contatos(contatos)` que percorra a lista e
   imprima cada contato de forma organizada.
5. No programa principal, cadastre pelo menos três contatos, busque um
   deles pelo nome e liste todos ao final.
