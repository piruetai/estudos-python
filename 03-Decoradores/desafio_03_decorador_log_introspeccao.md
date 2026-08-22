# Desafio 03 — Decorador de Log com Introspecção

## Enunciado

Um sistema precisa registrar em log todas as chamadas de determinadas
funções: quais argumentos foram passados e qual foi o valor retornado —
mas sem perder as informações originais da função (como `__name__` e
`__doc__`), que são úteis para debug e documentação.

**Objetivo:** criar um programa que:

1. Crie um decorador `log_chamada(funcao)` que imprima, antes de
   executar a função, o nome dela e os argumentos recebidos (`*args` e
   `**kwargs`).
2. Utilize `functools.wraps` no wrapper para preservar `__name__` e
   `__doc__` da função original, e demonstre a diferença imprimindo
   `funcao.__name__` com e sem o uso de `wraps`.
3. Após a execução, imprima também o valor retornado pela função antes
   de repassá-lo para quem chamou.
4. Aplique `@log_chamada` em ao menos duas funções com assinaturas
   diferentes (uma com argumentos posicionais, outra com argumentos
   nomeados).
5. Mostre no terminal o log completo de cada chamada: nome da função,
   argumentos recebidos e valor retornado.
