import numpy as np

class Pilha:
    def __init__ (self, capacidade): 
        self.__capacidade = capacidade
        self.__topo = -1 #onde esta o topo da pilha
        self.__valores = np.empty(capacidade, dtype=int) #os valores armazenados na pilha
    
    def __pilha_cheia(self): #por medida de segurança é importante deixar o método privado
        if self.__topo == self.__capacidade - 1 :
            return True
        else:
            return False
    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False
    def empilhar(self,valor):
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor #adiciona o valor para a pilha
    def desempilhar(self):
        if self.__pilha_vazia():
            print('Pilha vazia')
        else:
            self.__topo -=1 #retira o primeiro elemento
            
    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1
pilha = Pilha(5)
pilha.empilhar(5)
print(pilha.ver_topo())


