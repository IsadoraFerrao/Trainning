import numpy as np

class vetorOrdenado:
    def __init___(self,capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('o vetor está vazio')
        else:
            for i in range(self.ultima_posicao+1): #percorrer todas as posicoes
                print(i, '-', self.valores[i])
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return 
    #descobrir qual posicao inserir o novo elemento