# First day part one of my advent of code challenge#
def dial(ponteiroAtual, incremento):
         limite = 100
         novoValor = ponteiroAtual + incremento
         valorFinal = novoValor % limite
         return valorFinal
    
    
ponteiroInicial = 50;
incremento = 0 ; 
resultado = 0;
with open(r'Day1\input.txt', 'r', encoding='utf-8') as arquivo:
    combinacoes = arquivo.readlines();

for linha in combinacoes:
    linha = linha.strip('\n')
    primeiraLetra = linha[0]
    digito = int(linha[1:])
    if primeiraLetra == "L":
       incremento = digito * -1
       ponteiroInicial = dial(ponteiroInicial,incremento)
       if ponteiroInicial == 0:
            resultado +=1
    else:
        incremento = digito
        ponteiroInicial = dial(ponteiroInicial,incremento)
        if ponteiroInicial == 0:
            resultado +=1
            
print(resultado)      
print("===Part one ===")      
    
    
     

     
         
         
          
