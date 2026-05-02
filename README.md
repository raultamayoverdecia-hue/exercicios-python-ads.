# exercicios-python-ads.
# Exercícios de Lógica de Programação
Este repositório contém as soluções dos exercícios propostos na disciplina de Lógica de Programação (2026/2).

### Exercício 6: Cálculo de Venda de Bananas
**Enunciado:** Um supermercado vende bananas por R$ 3.50 o quilo. O programa lê o peso e imprime o valor total.

### Tecnologias Utilizadas:
* Python 3
* Pydroid 3 (Desenvolvimento via Mobile)
# Entradas
qtd_plastico = int(input("Caixas de plástico vendidas: "))
qtd_metal = int(input("Caixas de metal vendidas: "))

# Cálculos
valor_plastico = qtd_plastico * 5
valor_metal = qtd_metal * 10
total_geral = valor_plastico + valor_metal

# Resultados
print(f"Arrecadado com plástico: R$ {valor_plastico:.2f}")
print(f"Arrecadado com metal: R$ {valor_metal:.2f}")
print(f"Total geral: R$ {total_geral:.2f}")
