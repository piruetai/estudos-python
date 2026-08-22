# Desafio 04 — Formas Geométricas Polimórficas

## Enunciado

Uma calculadora de áreas precisa suportar diferentes formas geométricas,
todas seguindo o mesmo "contrato": todo objeto deve saber calcular sua
própria área.

| Forma      | Dados necessários      |
|------------|--------------------------|
| Círculo    | Raio                     |
| Retângulo  | Base e altura            |
| Triângulo  | Base e altura            |

**Objetivo:** criar um programa que:

1. Defina uma classe abstrata `FormaGeometrica` (usando `ABC`), com um
   método abstrato `calcular_area()`.
2. Crie as classes `Circulo`, `Retangulo` e `Triangulo`, cada uma
   herdando de `FormaGeometrica` e implementando seu próprio
   `calcular_area()`.
3. Tente instanciar `FormaGeometrica` diretamente e observe (ou capture)
   o erro, demonstrando por que uma classe abstrata não pode ser
   instanciada.
4. Armazene diferentes formas em uma mesma lista e percorra essa lista
   calculando a área de cada uma, aproveitando o polimorfismo (o mesmo
   método `calcular_area()` chamado, com comportamentos diferentes).
5. Mostre no terminal a área de cada forma e a soma total das áreas.
