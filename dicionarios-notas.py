i=0
alunos = {}
while(i<3):
    nome=input('Digite o nome: ')
    nota=int(input('Digite a nota: '))
    alunos[nome]=nota
    i=i+1
soma=0
for x in alunos.values():
    soma=soma+x
    x=x+1
print(soma/3)