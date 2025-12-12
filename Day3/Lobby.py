# Third day of my advent of code challenge#
def  max_voltage_da_bateria(bateria: str) -> int:
    bateria = bateria.strip()
    digito = [int(ch) for ch in bateria]
    n = len(digito)
    maior = -1 
    for i in range(n):
        for j in range(i + 1, n):
            valor = digito[i] * 10 + digito[j]
            if valor > maior:
                maior = valor

    return maior

total_voltage = 0

with open(r"Day3\input.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if not linha:
            continue  
        total_voltage += max_voltage_da_bateria(linha)

print(total_voltage)