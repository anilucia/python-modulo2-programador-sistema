#13.Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input("Digite o salário: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))
novo_salario = salario + (salario * percentual_aumento / 100)
print(f"O novo salário é {novo_salario:.2f}.")

#output do programa será:S
# Digite o salário: 3500.0
# Digite o percentual de aumento: 20.0
# O novo salário é 4200.00.