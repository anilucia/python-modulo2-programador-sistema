#8.Leia um número como string e imprima o seu tipo antes e depois de converter para int.
numero_str = input("Digite um número: ")
print(f"Tipo antes da conversão: {type(numero_str)}")
numero_int = int(numero_str)
print(f"Tipo depois da conversão: {type(numero_int)}")