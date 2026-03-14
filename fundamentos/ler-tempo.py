#11.Leia a distância (km) e o tempo (h), calcule a velocidade média.
distancia = float(input("Digite a distância em km: "))
tempo = float(input("Digite o tempo em horas: "))
velocidade_media = distancia / tempo
print(f"A velocidade média é {velocidade_media:.2f} km/h.")