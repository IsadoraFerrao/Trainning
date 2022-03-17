import numpy as np

class Pilha:
    def __init__ (self, capacidade): 
        self.capacidade = capacidade
        self.topo = -1 #onde esta o topo da pilha
        self.valores = np.empty(capacidade, dtype=int) #os valores armazenados na pilha
    
    def pilha_cheia(self):
        if self.topo == self.capacidade -1:
            return True
        else
            return False