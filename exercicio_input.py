# Entrada de dados
nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

# Saída de dados (Usando f-strings para facilitar a leitura)
print(f"{nome} trabalha na empresa {empresa}")
print(f"Possui: {qtde_funcionarios} funcionários.")
print(f"A média da mensalidade é de: {mediaMensalidade:.2f}")
