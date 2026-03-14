#14.Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)
minutos = int(input("Digite a quantidade de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{horas}h{minutos_restantes}")