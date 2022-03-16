with open('operador-matematico.txt') as tex:
    for linha in tex:
        print(linha)
        
with open('operador-matematico.txt') as tex:
    r = tex.readlines() #lendo o arquivo e jogando pra variavel r
    
with open('text2.txt', 'w') as texto: #criando um arquivo de texto
    texto.write('ola a todos')