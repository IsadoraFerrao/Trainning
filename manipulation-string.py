a = 'casaco'
#print(a.upper()) #tudo A

maiuscula = a.upper() #tudo A
#print(maiuscula)

minuscula = a.lower() #tudo a
#print(minuscula)

capital = a.capitalize() #apenas a primeira letra maiscula
#print(capital)

metade_palavra = a[0:3]
#print(metade_palavra)

ultimas_letras = a[3:]
#print(ultimas_letras)

b = a.replace('casaco', 'cca')
#print(a)
#print(b)

print(b.find('a')) #procurar dentro da string
print(len(a)) #tamanho da string

n1 = int(14)
n2 = int(16)
n= n1/n2
print(n)