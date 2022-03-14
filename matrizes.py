import numpy as np
matriz = np.array([[2,3,1],[4,3,1]]) #linha e coluna
#print(matriz)

#print(matriz.shape) #mostra a qntd de linhas e colunas
#print(matriz[0])

#print(matriz[1])
#print(matriz[0][1])

for i in range(matriz.shape[0]): #posicao 0 linhas e 1 colunas
    print(matriz[i])
    for j in range(matriz.shape[1]): #posicao 0 linhas e 1 colunas
        print(matriz[i][j])


