# First day part one of my advent of code challenge#
def dial(ponteiro_Atual, incremento):
         limite = 100
         novo_Valor = ponteiro_Atual + incremento
         valor_Final = novo_Valor % limite
         return valor_Final
    
    
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
    
    
     

     
         
         
          
