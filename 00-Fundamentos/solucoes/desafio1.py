registro = [
    {"horario": 6, "temperatura (°C)": 14.5},
    {"horario": 12, "temperatura (°C)": 27},
    {"horario": 18, "temperatura (°C)": 21.3},
    {"horario": 18, "temperatura (°C)": 21.3}
]


for dados in registro:
  dados["temperatura (°F)"] = dados["temperatura (°C)"] * 9/5 + 32

pico_f = max(dados["temperatura (°F)"] for dados in registro)
pico_c = max(dados["temperatura (°C)"] for dados in registro)

tabela = '''
| Horário | Temperatura (°C)  | Temperatura (°F)  |
|---------|-------------------|-------------------|
'''

for dados in registro:
   tabela += f"| {dados['horario']:02d}h     | {dados['temperatura (°C)']:.1f}              | {dados['temperatura (°F)']:.1f}              |\n"

print(tabela + f"\n Pico celsius: {pico_c}\n Pico fahrenheit: {pico_f}")