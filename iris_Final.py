# -*- coding: utf-8 -*-
"""
Created on:
https://gist.github.com/marcoscastro/491bd5837815fe11181dce6c50f457ee

@author: Marcos Castro
"""

"""
	Implementação da rede neural Perceptron
	w = w + N * (d(k) - y) * x(k)
"""
import numpy as np
#import matplotlib.pyplot as plt
import random, copy
from sklearn import datasets
iris = datasets.load_iris()

class Perceptron:
   def __init__(self, amostras, saidas, taxa_aprendizado = 0.1, epocas = 1000, limiar=-1):
      self.amostras = amostras # todas as amostras
      self.saidas = saidas # saídas respectivas de cada amostra
      self.taxa_aprendizado = taxa_aprendizado # taxa de aprendizado (entre 0 e 1)
      self.epocas = epocas # número de épocas
      self.limiar = limiar # limiar
      self.num_amostras = len(amostras) # quantidade de amostras
      self.num_amostra = len(amostras[0]) # quantidade de elementos por amostra
      self.pesos = [] # vetor de pesos
   # função para treinar a rede
   def treinar(self):
      # adiciona -1 para cada uma das amostras
      self.amostras = np.insert(self.amostras,0,-1,axis=1)  
         # inicia o vetor de pesos com valores aleatórios
      for i in range(self.num_amostra):
         self.pesos.append(random.random())
      # insere o limiar no vetor de pesos
      self.pesos.insert(0, self.limiar)
      
      # inicia o contador de epocas
      num_epocas = 0
      while True:
         erro = False # o erro inicialmente inexiste
         # para todas as amostras de treinamento
         for i in range(self.num_amostras):
            u = 0
            '''
					realiza o somatório, o limite (self.amostra + 1)
					é porque foi inserido o -1 para cada amostra
				'''
            for j in range(self.num_amostra + 1):
               u += self.pesos[j] * self.amostras[i][j]
               
            
            # obtém a saída da rede utilizando a função de ativação
            y = self.cpl(u)
 
            # verifica se a saída da rede é diferente da saída desejada
            if y != self.saidas[i]:
               # calcula o erro: subtração entre a saída desejada e a saída da rede
               erro_aux = self.saidas[i] - y
               # faz o ajuste dos pesos para cada elemento da amostra
               for j in range(self.num_amostra + 1):
                  self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
               erro = True # ainda existe erro
      # incrementa o número de épocas
         num_epocas += 1
      # critério de parada é pelo número de épocas ou se não existir erro
         if num_epocas > self.epocas or not erro:
            break
   # função utilizada para testar a rede
	# recebe uma amostra a ser classificada e os nomes das classes
	# utiliza a função cpl, se é -1 então é classe1, senão é classe2d
   def testar(self, amostra, classe1, classe2, classe3):
      # insere o -1
      amostra = np.insert(amostra,0,-1,axis=0)
      # utiliza o vetor de pesos que foi ajustado na fase de treinamento
      u = 0
      for i in range(self.num_amostra + 1):
         u += self.pesos[i] * amostra[i]
      # calcula a saída da rede
      y = self.cpl(u)
        
      # verifica a qual classe pertence
      if y == 0:
         print('A amostra pertence a classe %s' % classe1)
      elif y == 1:
         print('A amostra pertence a classe %s' % classe2)
      else:
         print('A amostra pertence a classe %s' % classe3)
      # função de ativação: degrau bipolar (cpl)
      return y
  
   def cpl(self, u):
      if(u <= 0):
          i = 0
      elif(u >= 2.986):
          i = 2
      else:
          i = 1
      return i
   
print('\nA ou B ou C?\n')

# iris flower

amostras = 0.1*iris.data[:150,:4]  # we only take the first two features.

h = np.vstack((amostras[:30,:], amostras[50:80,:], amostras[100:130,:]))
alien = np.vstack((amostras[30:50,:] ,amostras[80:100,:], amostras[130:150,:]))

saidas = iris.target[:150]
saidas[:50] = saidas[:50] 
#print(saidas)

g = np.hstack((saidas[:30], saidas[50:80], saidas[100:130]))
et = np.hstack((saidas[30:50], saidas[80:100], saidas[130:150]))

# conjunto de amostras de testes
testes = copy.deepcopy(alien)

# cria uma rede Perceptron
rede = Perceptron(amostras=h, saidas=g,	
						taxa_aprendizado=0.1, epocas=1000)

# treina a rede
rede.treinar()

# testando a rede
for teste in testes:
	rede.testar(teste, 'A', 'B', 'C')









