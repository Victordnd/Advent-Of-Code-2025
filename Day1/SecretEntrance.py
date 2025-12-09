# First day(but took two)  of my advent of code challenge#
def dial(ponteiro_Atual, incremento):
         limite = 100
         novo_Valor = ponteiro_Atual + incremento
         valor_Final = novo_Valor % limite
         return valor_Final
   
quociente = 0    
ponteiro_Inicial = 50
resultado = 0
with open(r'Day1\input.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip('\n')

        
        primeira_Letra = linha[0]
        digito = int(linha[1:])
        
        if primeira_Letra == "L":
             incremento = -digito 
        else:
            incremento = digito
        
        ponteiro_Inicial = dial(ponteiro_Inicial,incremento)
        
        if ponteiro_Inicial == 0:
            resultado +=1 
                     
print(resultado)      
print("===Part one ===")      
    
def contar_zeros(ponteiro_atual, incremento):
    
    if incremento == 0:
        return 0

    inicio = ponteiro_atual
    fim = ponteiro_atual + incremento

    if incremento > 0:
       
        return fim // 100 - inicio // 100
    else:
        
        return (inicio - 1) // 100 - (fim - 1) // 100 
     
total_zeros = 0
ponteiro_inicial = 50

with open(r'Day1\input.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip('\n')

        primeira_letra = linha[0]
        digito = int(linha[1:])

        if primeira_letra == "L":
            incremento = -digito
        else:
            incremento = digito
     
        total_zeros += contar_zeros(ponteiro_inicial, incremento)
        ponteiro_inicial = dial(ponteiro_inicial, incremento)

print(total_zeros)
print("=== Part Two ===")
     
         
         
          
