# Second day of my advent of code challenge#
def id_invalido(numero):
    string_numero = str(numero)
    if len(string_numero) % 2 != 0:
        return False  
    
    meio = len(string_numero) // 2
    metade = string_numero[:meio]
    return metade * 2 == string_numero  

soma_id = 0
with open(r'Day2\input.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()            

        intervalos = linha.split(',')     

        for  inter in intervalos:
            a, b = inter.split('-')   
            
            for n in range(int(a), int(b) + 1):
                if id_invalido(n):
                    soma_id += n

print( soma_id)
print("===Part one ===")  