import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int) #empty é array vazio
    def imprimir(self):
        if self.ultima_posicao == -1:
            print('o vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1): #percorrer todos os elementos do vetor
                print(i, '-', self.valores[i])
    def insere(self,valor):
        if self.ultima_posicao == self.capacidade - 1: #se a capacidade for atingida, para pra n extourar a a capacidade do vetor
            print('Capacidade máxima atingida') 
        else:
            self.ultima_posicao += 1 
            self.valores[self.ultima_posicao] = valor
            
    def pesquisar(self, valor): #pesquisa linear, procurando posicao por posicao até encontrar
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
            return -1
    def excluir(self,valor):
        posicao = self.pesquisar(valor)
        if posicao
            
vetor = VetorNaoOrdenado(5)
vetor.insere(2)
vetor.insere(4)
vetor.insere(7)
vetor.imprimir()
a = vetor.pesquisar(4)
print(a)