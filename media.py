M1 = int(input('nota 01: '))
M2 = int(input('nota 02: '))
M3 = int(input('nota 02: '))

media= (M1+M2+M3)/3
if(media==0 or media<=4.0):
    print('reprovado')
elif(media==4.1 or media<=6.0):
    print('exame')
elif(media>6.0):
    print('aprovado')


