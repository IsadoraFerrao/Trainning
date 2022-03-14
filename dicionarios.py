coleta = {'COVID': 32, 'GRIPE':23, 'dengue':10}
#print(coleta['COVID'])

coleta['catapora'] = 11 #adicionando elemento

del(coleta)['COVID']
#print(coleta)

#print(coleta.items()) #lista completa
#print(coleta.keys()) #busca somente as as chaves e não os valores
#print(coleta.values()) #somente os valores

coleta2 = {'jwiwji': 13, 'jeifejif': 14}
#print(coleta2)

coleta.update(coleta2) #juntando listas
#print(coleta)

#for doenca, problema in coleta.items():
    #print(doenca,problema)
    
#conjuntos 
biomoleculas = ('proteina', 'lipidio','carboidrat','carboidrat','carboidrat')
print(biomoleculas)
print(set(biomoleculas)) #set é utilizada para selecionar apenas os elementos q n se repetem

c1={1,2,3,4,5}
c2={3,4,5,6,7}
c3=c1.intersection(c2) #retorna apenas elementos dos dois conjuntos
print(c1)
