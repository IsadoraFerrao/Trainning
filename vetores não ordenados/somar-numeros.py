#import math
#def solution(n):
#    soma = 0
#    n = str(n)
#    for i in range(len(n)):
#        soma = soma+int(n[i])
#    print(soma)    

#solution(22)

#import math
#def solution(n):
#    value = str(n)
#    n = map(int, tuple(value[0::2]))
#    s = map(int, tuple(value[1::2]))
#    print(sum(n) - sum(s))
#solution(52134)

import numpy as np
import collections
def solution(a):
    abit = np.array([0,1,2])
    print(np.bincount(abit))