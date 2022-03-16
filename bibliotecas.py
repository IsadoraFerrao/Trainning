#math
import math
#print(math.sqrt(36))
math.sin(45) #seno
math.cos(45) #cosseno
m = math.log(1000,10) #logaritimo

#datetime
import datetime 
d= datetime.date.today() #saber a data de hoje
h = datetime.datetime.now() #saber o horario exato de agora
date = datetime.date(2020,7,10)
date.month #para extrair o ano
#print(h)


#random
import random

r = random.random()
r = random.randint(1,10) #gerar um rand entre 1 e 10 inteiro
m = random.randrange(0,10,2) #gerar numeros entre 0 e 10, pares = 2 e se quiser impar coloca 0 3
print(m)
x= ['x', 'd',13,4,'i']
b = random.choice(x) #random em uma lista
print(b)

#time
import time as tm #medir quanto o código levou pra executar
a= tm.time()
print(a)