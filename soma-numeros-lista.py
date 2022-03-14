i=0
numeros = []
while(i<5):
    num=int(input('Digite um número: '))
    numeros.append(num)
    i=i+1
soma=0
i=0
for x in numeros:
    soma=soma+x
    x=x+1
print(soma)
