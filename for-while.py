#quant = 0
#prova = 0

#while(quant < 5):
#    notas=int(input('Digite sua nota: '))
#    quant+=1
#    prova=notas+prova
#    media_final=prova/5
#sprint(media_final)

prova=0

for qnt in range(0,5):
    nota = int(input('Digite sua nota: '))
    prova=nota+prova
media=prova/5
print(media)
