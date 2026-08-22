# Desafio 02 — Pontos de Rota Únicos

## Enunciado

Um aplicativo de entregas registra, para cada corrida, as coordenadas
(latitude, longitude) visitadas pelo entregador ao longo do dia:

```
Corrida 1: (10, 20), (15, 25), (10, 20), (30, 40)
Corrida 2: (15, 25), (50, 60), (30, 40)
```

**Objetivo:** criar um programa que:

1. Represente cada coordenada como uma `tuple` (latitude, longitude).
2. Armazene as coordenadas de cada corrida em um `set`, de forma que
   pontos repetidos dentro da mesma corrida não sejam contados duas vezes.
3. Utilize `union` para descobrir todos os pontos visitados no dia
   (considerando as duas corridas).
4. Utilize `intersection` para descobrir quais pontos foram visitados em
   **ambas** as corridas.
5. Mostre no terminal o total de pontos únicos do dia e os pontos em
   comum entre as duas corridas.
