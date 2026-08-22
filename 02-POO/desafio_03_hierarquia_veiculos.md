# Desafio 03 — Hierarquia de Veículos

## Enunciado

Uma locadora quer modelar diferentes tipos de veículos da sua frota,
reaproveitando o máximo de código possível entre eles.

| Veículo | Tipo   | Rodas | Combustível |
|---------|--------|-------|-------------|
| Fusca   | Carro  | 4     | Gasolina    |
| CG 160  | Moto   | 2     | Gasolina    |
| Tesla Y | Carro  | 4     | Elétrico    |

**Objetivo:** criar um programa que:

1. Defina uma classe base `Veiculo` com atributos comuns (marca, modelo,
   número de rodas) e um método `descrever()`.
2. Crie as classes `Carro` e `Moto`, que herdam de `Veiculo` (herança
   simples), cada uma sobrescrevendo `descrever()` para incluir
   informações específicas.
3. Crie uma classe `VeiculoEletrico` e utilize herança múltipla para
   criar uma classe `CarroEletrico`, combinando `Carro` e
   `VeiculoEletrico`.
4. Utilize `super()` para reaproveitar a lógica das classes-mãe sempre
   que fizer sentido.
5. Instancie ao menos um veículo de cada tipo e mostre a descrição de
   todos no terminal.
