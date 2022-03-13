idade = int(input('idade: '))

if(idade==0 or idade<13):
    print('criança')
elif (idade==13 or idade<18):
    print('adolescente')
elif (idade>18):
    print('adulto')
elif (idade<0):
    print('Idade inválida')

    